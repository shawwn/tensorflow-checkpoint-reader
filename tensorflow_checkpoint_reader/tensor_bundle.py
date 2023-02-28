from . import table
from . import env
from . import core
from . import errors
from . import naming
from . import tensor
from . import tensor_shape
from . import file_system
from . import file_system_helper
from . import random
from . import port
from . import table_options
from . import table_builder
from .tensorflow.python.platform import tf_logging as logging
from .pb.tensorflow.core.protobuf import tensor_bundle_pb2
from .pb.tensorflow.core.framework import types_pb2

from typing import Tuple, Optional, List, Dict
import time
import sys
import dataclasses

# // Versioning of the tensor bundle format.
# const int kTensorBundleMinProducer = 0;
# const int kTensorBundleMinConsumer = 0;
# const int kTensorBundleVersion = 1;
kTensorBundleMinProducer = 0
kTensorBundleMinConsumer = 0
kTensorBundleVersion = 1

# // Size of our input buffer for streaming reads
# static const int kBufferSize = 1024 * 1024;
kBufferSize = 1024 * 1024

# // Key to the special BundleHeaderProto entry.  Do not change this, as clients
# // can make the assumption that the header is always the first entry in the
# // bundle.
# const char* const kHeaderEntryKey = "";
kHeaderEntryKey = b""

def _memcpy(dst: core.StringPiece, data: core.StringPiece, size: int):
  dst[:size] = data[:size]

def AlignedMalloc(size: int) -> core.StringPiece:
  return core.StringPiece(bytearray(size))

class FileOutputBuffer:
  """A buffering wrapper for a WritableFile.  Useful if the caller wishes to issue
  small writes to a file (e.g. writing out a list of small varints).
  External synchronization must be used in the presence of concurrent callers."""
  def __init__(self, file: file_system.WritableFile, buffer_size: int):
    assert buffer_size > 0
    self._file = file
    self._position = 0
    self._buffer_size = buffer_size
    # Checksum of all appended bytes since construction or last clear_crc32c().
    self._crc32c = 0
    self._buffer_ptr = AlignedMalloc(buffer_size)

  # // Buffered append.
  # Status Append(StringPiece data);
  def append(self, data: core.StringPiece) -> errors.Status:
    # In the below, it is critical to calculate the checksum on the actually
    # copied bytes, not the source bytes.  This is because "data" typically
    # points to tensor buffers, which may be concurrently written.
    if data.size() + self._position <= self._buffer_size:
      # Can fit into the current buffer.
      _memcpy(self._buffer_ptr + self._position, data.data(), data.size())
      self._crc32c = core.crc32c.extend(self._crc32c, data.data(), data.size())
    elif data.size() <= self._buffer_size:
      # Cannot fit, but can fit after flushing.
      errors.raise_if_error(self._flush_buffer(closing=False))
      _memcpy(self._buffer_ptr, data.data(), data.size())
      self._crc32c = core.crc32c.extend(self._crc32c, self._buffer_ptr, data.size())
    else:
      # Cannot fit even after flushing.  So we break down "data" by chunk, and
      # flush/checksum each chunk.
      errors.raise_if_error(self._flush_buffer(closing=False))
      for i in range(0, data.size(), self._buffer_size):
        nbytes = min(data.size() - i, self._buffer_size)
        _memcpy(self._buffer_ptr, data.data() + i, nbytes)
        self._crc32c = core.crc32c.extend(self._crc32c, self._buffer_ptr, nbytes)
        self._position = nbytes
        errors.raise_if_error(self._flush_buffer(closing=False))
      return errors.Status.OK()
    self._position += data.size()
    return errors.Status.OK()

  def crc32c(self):
    """Returns the running crc32c checksum of all currently appended bytes."""
    return self._crc32c

  def clear_crc32c(self):
    """Clears the running crc32c checksum."""
    self._crc32c = 0

  def close(self) -> errors.Status:
    """Appends the buffered data, then closes the underlying file."""
    status = self._flush_buffer(closing=False)
    if not status.ok():
      return status
    return self._file.close()

  def _flush_buffer(self, closing: bool) -> errors.Status:
    """Appends the buffered data to the underlying file. Does NOT flush the file."""
    if self._position > 0:
      # Use Cord to avoid extra data copy for some WritableFile implementations.
      # absl::Cord buffer = absl::MakeCordFromExternal(
      #     StringPiece(buffer_ptr_, position_),
      #     [ptr = buffer_ptr_](StringPiece) { port::AlignedFree(ptr); });
      buffer = core.StringPiece(self._buffer_ptr, self._position)
      self._buffer_ptr = None if closing else AlignedMalloc(self._buffer_size)
      errors.raise_if_error(self._file.append(buffer))
      self._position = 0
    return errors.Status.OK()


# // Serializes the data bytes of the non-string tensor "val".  Discards the
# // original content of "bytes_written", and on OK updates it with number of
# // bytes written.
# // REQUIRES: val.dtype() != DT_STRING
# Status WriteTensor(const Tensor& val, FileOutputBuffer* out,
#                    size_t* bytes_written) {
#   DCHECK_NE(val.dtype(), DT_STRING);
#   DCHECK_NE(val.dtype(), DT_VARIANT);
#   *bytes_written = val.TotalBytes();
#   char* buf = GetBackingBuffer(val);
#   VLOG(1) << "Appending " << *bytes_written << " bytes to file";
#   return out->Append(StringPiece(buf, *bytes_written));
# }
def WriteTensor(val: tensor.Tensor, out: FileOutputBuffer) -> Tuple[errors.Status, int]:
  """Serializes the data bytes of the non-string tensor "val".  Returns the number
  of bytes.

  REQUIRES: val.dtype() != DT_STRING"""
  assert val.dtype() != types_pb2.DT_STRING
  assert val.dtype() != types_pb2.DT_VARIANT
  bytes_written = val.total_bytes()
  buf = GetBackingBuffer(val)
  return out.append(core.StringPiece(buf, bytes_written)), bytes_written

# char* GetBackingBuffer(const Tensor& val) {
#   CHECK(DataTypeCanUseMemcpy(val.dtype())) << val.dtype();
#   return const_cast<char*>(val.tensor_data().data());
# }
def GetBackingBuffer(val: tensor.Tensor) -> core.StringPiece:
  return val.tensor_data().data()

# // Writes zeros to output buffer to align the next write to the requested
# // alignment. "size" is the current size of the buffer and is updated to the
# // new size.
# Status PadAlignment(FileOutputBuffer* out, int alignment, int64* size) {
#   int bytes_over = *size % alignment;
#   if (bytes_over == 0) {
#     return Status::OK();
#   }
#   int bytes_to_write = alignment - bytes_over;
#   Status status = out->Append(string(bytes_to_write, '\0'));
#   if (status.ok()) {
#     *size += bytes_to_write;
#   }
#   return status;
# }
def PadAlignment(out: FileOutputBuffer, alignment: int, size: int) -> Tuple[errors.Status, int]:
  bytes_over = size % alignment
  if bytes_over == 0:
    return errors.Status.OK(), size
  bytes_to_write = alignment - bytes_over
  status = out.append(core.string_view(bytearray(bytes_to_write)))
  if status.ok():
    size += bytes_to_write
    return status, size
  return status, size

class BundleWriter:
  """Builds a string-string table of tensor names to BundleEntryProto (metadata).

  On construction, attempts to create a directory given by the dirname of
  "prefix", so "status()" must be checked before calling any member functions.

  All threads accessing the same BundleWriter must synchronize.
  """
  @dataclasses.dataclass(frozen=True)
  class Options:
    data_alignment: int = 1
    """
    Alignment, in bytes, for tensor data.
    Must be >= 1. The default size of 1 densely packs tensors.
    """

  def __init__(self, env_: env.Env, prefix: core.StringPiece, options: Options = None):
    if options is None:
      options = self.Options()
    self._env = env_
    prefix = core.string_view(prefix)
    self._prefix = prefix.bytes()
    self._options = options
    self._out = None
    self._size = 0
    self._status = errors.Status.OK()
    self._entries: Dict[bytes, tensor_bundle_pb2.BundleEntryProto] = {}
    self._use_temp_file = errors.raise_if_error(env_.has_atomic_move(prefix.bytes()))

    # data_path_ = DataFilename(prefix_, 0, 1);
    # metadata_path_ = MetaFilename(prefix_);
    self._data_path = naming.data_filename(self._prefix, 0, 1)
    self._metadata_path = naming.meta_filename(self._prefix)
    # if (use_temp_file_) {
    #   data_path_ = strings::StrCat(data_path_, ".tempstate", random::New64());
    #   metadata_path_ =
    #       strings::StrCat(metadata_path_, ".tempstate", random::New64());
    # }
    if self._use_temp_file:
      self._data_path += f".tempstate{random.new_64()}".encode('utf-8')
      self._metadata_path += f".tempstate{random.new_64()}".encode('utf-8')

    # status_ = env_->CreateDir(string(io::Dirname(prefix_)));
    # if (!status_.ok() && !errors::IsAlreadyExists(status_)) {
    #   return;
    # }

    # std::unique_ptr<WritableFile> wrapper;
    # status_ = env_->NewWritableFile(data_path_, &wrapper);
    # if (!status_.ok()) return;
    wrapper = errors.raise_if_error(env_.new_writable_file(self._data_path))
    # out_ = std::unique_ptr<FileOutputBuffer>(
    #     new FileOutputBuffer(wrapper.release(), 8 << 20 /* 8MB write buffer */));
    self._out = FileOutputBuffer(wrapper, 8 << 20) # 8MB write buffer

    # VLOG(1) << "Writing to file " << data_path_;
    logging.info("Writing to file %s", self._data_path)

  # Status Add(StringPiece key, const Tensor& val);
  def add(self, key: core.StringPiece, val: tensor.Tensor):
    """Adds the tensor "val" under key "key".

    Across calls "key" must be unique but can be added in any order."""
    # if (!status_.ok()) return status_;
    if not self._status.ok():
      return self._status
    # CHECK_NE(key, kHeaderEntryKey);
    assert key != kHeaderEntryKey
    key = core.string_view(key)
    if not isinstance(val, tensor.Tensor):
      # try to convert to Tensor from a numpy array.
      val = tensor.Tensor.from_array(val)
    # const string key_string(key);
    key_string = key.bytes()
    # if (entries_.find(key_string) != entries_.end()) {
    #   status_ = errors::InvalidArgument("Adding duplicate key: ", key);
    #   return status_;
    # }
    if key_string in self._entries:
      self._status = errors.InvalidArgument("Adding duplicate key: ", key)
      return self._status
    # BundleEntryProto* entry = &entries_[key_string];
    entry = self._entries.setdefault(key_string, tensor_bundle_pb2.BundleEntryProto())
    entry: tensor_bundle_pb2.BundleEntryProto
    # entry->set_dtype(val.dtype());
    entry.dtype = val.dtype()
    # val.shape().AsProto(entry->mutable_shape());
    val.shape().as_proto(entry.shape)
    # entry->set_shard_id(0);
    # entry->set_offset(size_);
    entry.shard_id = 0
    entry.offset = self._size

    # // Updates the data file.
    # size_t data_bytes_written = 0;
    # uint32 crc32c = 0;
    # out_->clear_crc32c();
    self._out.clear_crc32c()
    # if (val.dtype() == DT_STRING) {
    #   status_ = WriteStringTensor(val, out_.get(), &data_bytes_written, &crc32c);
    # } else if (val.dtype() == DT_VARIANT) {
    #   status_ = WriteVariantTensor(val, out_.get(), &data_bytes_written, &crc32c);
    # } else {
    #   status_ = WriteTensor(val, out_.get(), &data_bytes_written);
    #   crc32c = out_->crc32c();
    # }
    if val.dtype() == types_pb2.DT_STRING:
      raise NotImplementedError("TODO: support string tensors")
      self._status, data_bytes_written, crc32c = WriteStringTensor(val, self._out)
    elif val.dtype() == types_pb2.DT_VARIANT:
      raise NotImplementedError("TODO: support variant tensors")
      self._status, data_bytes_written, crc32c = WriteVariantTensor(val, self._out)
    else:
      self._status, data_bytes_written = WriteTensor(val, self._out)
      crc32c = self._out.crc32c()

    # if (status_.ok()) {
    #   entry->set_size(data_bytes_written);
    #   entry->set_crc32c(crc32c::Mask(crc32c));
    #   size_ += data_bytes_written;
    #   status_ = PadAlignment(out_.get(), options_.data_alignment, &size_);
    # }
    if self._status.ok():
      entry.size = data_bytes_written
      entry.crc32c = core.crc32c.mask(crc32c)
      self._size += data_bytes_written
      self._status, self._size = PadAlignment(self._out, self._options.data_alignment, self._size)
    return self._status

  # // Partitioned variables support.
  # // A slice of a full tensor is stored in two entries in the metadata table:
  # //
  # //   full_tensor_key   -> BundleEntryProto, describing all stored slices
  # //                        of this full tensor.  Does not append to the data
  # //                        file.
  # //   encoded slice key -> BundleEntryProto, describing one particular slice.
  # //                        Appends values of this slice to the data file.
  # //
  # // Slices of a full tensor can be added in any order.
  # //
  # // If a full tensor has slices placed on N devices and N BundleWriter's are
  # // concurrently used, the caller must use MergeBundles() to ensure that a
  # // consistent entry for "full_tensor_key" is produced.
  # //
  # // Returns an error if the same slice is added the second time.
  # Status AddSlice(StringPiece full_tensor_key,
  #                 const TensorShape& full_tensor_shape,
  #                 const TensorSlice& slice_spec, const Tensor& slice_tensor);
  #
  # // Finishes the writer and flushes.
  # Status Finish() TF_MUST_USE_RESULT;
  def finish(self) -> errors.Status:
    """Finishes the writer and flushes."""
    # if (out_) {
    #   status_.Update(out_->Close());
    #   out_ = nullptr;
    #   if (status_.ok()) {
    #     if (use_temp_file_) {
    #       status_ =
    #           Env::Default()->RenameFile(data_path_, DataFilename(prefix_, 0, 1));
    #     }
    #   } else {
    #     Env::Default()->DeleteFile(data_path_).IgnoreError();
    #   }
    # }
    if self._out is not None:
      self._status.update(self._out.close())
      self._out = None
      if self._status.ok():
        if self._use_temp_file:
          self._status = self._env.rename_file(self._data_path, naming.data_filename(self._prefix, 0, 1))
        else:
          self._env.delete_file(self._data_path) # ignore error
    # if (!status_.ok()) return status_;
    if not self._status.ok():
      return self._status
    # // Build key -> BundleEntryProto table.
    # std::unique_ptr<WritableFile> file;
    # status_ = env_->NewWritableFile(metadata_path_, &file);
    self._status, file = self._env.new_writable_file(self._metadata_path)
    # if (!status_.ok()) return status_;
    if not self._status.ok():
      return self._status
    # {
    if True:
      # // N.B.: the default use of Snappy compression may not be supported on all
      # // platforms (e.g. Android).  The metadata file is small, so this is fine.
      # table::Options options;
      # options.compression = table::kNoCompression;
      options = table_options.Options(compression=table_options.kNoCompression)
      # table::TableBuilder builder(options, file.get());
      builder = table_builder.TableBuilder(options, file)
      # // Header entry.
      # BundleHeaderProto header;
      header = tensor_bundle_pb2.BundleHeaderProto()
      # header.set_num_shards(1);
      header.num_shards = 1
      # header.set_endianness(BundleHeaderProto::LITTLE);
      header.endianness = tensor_bundle_pb2.BundleHeaderProto.LITTLE
      # if (!port::kLittleEndian) header.set_endianness(BundleHeaderProto::BIG);
      if not port.kLittleEndian:
        header.endianness = tensor_bundle_pb2.BundleHeaderProto.BIG
      # VersionDef* version = header.mutable_version();
      # version->set_producer(kTensorBundleVersion);
      header.version.producer = kTensorBundleVersion
      # version->set_min_consumer(kTensorBundleMinConsumer);
      header.version.min_consumer = kTensorBundleMinConsumer
      #
      # builder.Add(kHeaderEntryKey, header.SerializeAsString());
      builder.add(kHeaderEntryKey, header.SerializeToString())
      #
      # // All others.
      # for (const auto& p : entries_) {
      #   builder.Add(p.first, p.second.SerializeAsString());
      # }
      for name, value in self._entries.items():
        builder.add(name, value.SerializeToString())
      # status_ = builder.Finish();
      self._status = builder.finish()
    # }
    # status_.Update(file->Close());
    self._status.update(file.close())
    # if (!status_.ok()) {
    #   Env::Default()->DeleteFile(metadata_path_).IgnoreError();
    #   return status_;
    if not self._status.ok():
      self._env.delete_file(self._metadata_path) # ignore error
      return self._status
    # } else if (use_temp_file_) {
    #   status_ = Env::Default()->RenameFile(metadata_path_, MetaFilename(prefix_));
    #   if (!status_.ok()) return status_;
    # }
    elif self._use_temp_file:
      self._status = self._env.rename_file(self._metadata_path, naming.meta_filename(self._prefix))
      if not self._status.ok():
        return self._status
    # status_ = errors::Internal("BundleWriter is closed");
    self._status = errors.Internal("BundleWriter is closed")
    # return Status::OK();
    return errors.Status.OK()

  # Status status() const { return status_; }
  def status(self):
    return self._status
