from . import core
from . import file_system
from . import table_options
from . import block_builder
from . import errors
from . import table
from . import coding
from . import strings
from copy import copy

# void FindShortestSeparator(string* start, const StringPiece& limit) {
def find_shortest_separator(start: bytearray, limit: core.StringPiece):
  # // Find length of common prefix
  # size_t min_length = std::min(start->size(), limit.size());
  min_length = min(len(start), limit.size())
  # size_t diff_index = 0;
  diff_index = 0
  # while ((diff_index < min_length) &&
  #        ((*start)[diff_index] == limit[diff_index])) {
  while ((diff_index < min_length) and
         (start[diff_index] == limit[diff_index])):
    # diff_index++;
    diff_index += 1
  # }

  # if (diff_index >= min_length) {
  if diff_index >= min_length:
    # // Do not shorten if one string is a prefix of the other
    pass
  # } else {
  else:
    # uint8 diff_byte = static_cast<uint8>((*start)[diff_index]);
    diff_byte = start[diff_index]
    # if (diff_byte < static_cast<uint8>(0xff) &&
    #     diff_byte + 1 < static_cast<uint8>(limit[diff_index])) {
    if (diff_byte < 0xFF and
        diff_byte + 1 < limit[diff_index]):
      # (*start)[diff_index]++;
      start[diff_index] += 1

      # start->resize(diff_index + 1);
      strings.resize(start, diff_index + 1)
      # assert(StringPiece(*start).compare(limit) < 0);
      assert core.StringPiece(start).compare(limit) < 0
    # }
  # }
# }
#
# void FindShortSuccessor(string* key) {
def find_short_successor(key: bytearray):
  # // Find first character that can be incremented
  # size_t n = key->size();
  n = len(key)
  # for (size_t i = 0; i < n; i++) {
  for i in range(n):
    # const uint8 byte = (*key)[i];
    byte = key[i]
    # if (byte != static_cast<uint8>(0xff)) {
    if byte != 0xFF:
      # (*key)[i] = byte + 1;
      key[i] = byte + 1
      # key->resize(i + 1);
      strings.resize(key, i + 1)
      # return;
      return
    # }
  # }
  # // *key is a run of 0xffs.  Leave it alone.
# }

class Rep:
  def __init__(self, opt: table_options.Options, f: file_system.WritableFile):
    self.options = copy(opt)
    self.index_block_options = copy(opt)
    self.file = f
    self.offset = 0
    self.status = errors.Status.OK()
    self.data_block = block_builder.BlockBuilder(self.options)
    self.index_block = block_builder.BlockBuilder(self.index_block_options)
    self.last_key = bytearray()
    self.num_entries = 0
    self.closed = False  # Either Finish() or Abandon() has been called.

    # We do not emit the index entry for a block until we have seen the
    # first key for the next data block.  This allows us to use shorter
    # keys in the index block.  For example, consider a block boundary
    # between the keys "the quick brown fox" and "the who".  We can use
    # "the r" as the key for the index block entry since it is >= all
    # entries in the first block and < all entries in subsequent
    # blocks.
    #
    # Invariant: r->pending_index_entry is true only if data_block is empty.
    self.pending_index_entry = False
    self.pending_handle = table.BlockHandle()  # Handle to add to index block

    self.compressed_output = bytearray()

    self.index_block_options.block_restart_interval = 1

# class TableBuilder {
#  public:
class TableBuilder:
  """TableBuilder provides the interface used to build a Table
  (an immutable and sorted map from keys to values).

  Multiple threads can invoke const methods on a TableBuilder without
  external synchronization, but if any of the threads may call a
  non-const method, all threads accessing the same TableBuilder must use
  external synchronization.
  """
  # // Create a builder that will store the contents of the table it is
  # // building in *file.  Does not close the file.  It is up to the
  # // caller to close the file after calling Finish().
  # TableBuilder(const Options& options, WritableFile* file);
  def __init__(self, options: table_options.Options, file: file_system.WritableFile):
    """Create a builder that will store the contents of the table it is
    building in *file.  Does not close the file.  It is up to the
    caller to close the file after calling Finish()."""
    self.rep_ = Rep(options, file)

  # // REQUIRES: Either Finish() or Abandon() has been called.
  # ~TableBuilder();
  #
  # // Add key,value to the table being constructed.
  # // REQUIRES: key is after any previously added key in lexicographic order.
  # // REQUIRES: Finish(), Abandon() have not been called
  # void Add(const StringPiece& key, const StringPiece& value);
  def add(self, key: core.StringPiece, value: core.StringPiece):
    key = core.string_view(key)
    value = core.string_view(value)
    # Rep* r = rep_;
    r = self.rep_
    # assert(!r->closed);
    assert not r.closed
    # if (!ok()) return;
    errors.raise_if_error(self.status())
    # if (r->num_entries > 0) {
    if r.num_entries > 0:
      # assert(key.compare(StringPiece(r->last_key)) > 0);
      assert key.compare(core.StringPiece(r.last_key)) > 0
      # // See if this key+value would make our current block overly large.  If
      # // so, emit the current block before adding this key/value
      # const int kOverlyLargeBlockRatio = 2;
      kOverlyLargeBlockRatio = 2
      # const size_t this_entry_bytes = key.size() + value.size();
      this_entry_bytes = key.size() + value.size()
      # if (this_entry_bytes >= kOverlyLargeBlockRatio * r->options.block_size) {
      if this_entry_bytes >= kOverlyLargeBlockRatio * r.options.block_size:
        # Flush();
        self.flush()
      # }
    # }

    # if (r->pending_index_entry) {
    if r.pending_index_entry:
      # assert(r->data_block.empty());
      assert r.data_block.empty()
      # FindShortestSeparator(&r->last_key, key);
      find_shortest_separator(r.last_key, key)
      # string handle_encoding;
      # r->pending_handle.EncodeTo(&handle_encoding);
      handle_encoding = r.pending_handle.encode_to()
      # r->index_block.Add(r->last_key, StringPiece(handle_encoding));
      r.index_block.add(r.last_key, core.StringPiece(handle_encoding))
      # r->pending_index_entry = false;
      r.pending_index_entry = False
    # }
    #
    # r->last_key.assign(key.data(), key.size());
    r.last_key[:] = key.bytes()
    # r->num_entries++;
    r.num_entries += 1
    # r->data_block.Add(key, value);
    r.data_block.add(key, value)
    #
    # const size_t estimated_block_size = r->data_block.CurrentSizeEstimate();
    estimated_block_size = r.data_block.current_size_estimate()
    # if (estimated_block_size >= r->options.block_size) {
    if estimated_block_size >= r.options.block_size:
      # Flush();
      self.flush()
    # }


  # // Advanced operation: writes any buffered key/value pairs to file.
  # // Can be used to ensure that two adjacent entries never live in
  # // the same data block.  Most clients should not need to use this method.
  # // Does not flush the file itself.
  # // REQUIRES: Finish(), Abandon() have not been called
  # void Flush();
  def flush(self):
    """Advanced operation: writes any buffered key/value pairs to file.
    Can be used to ensure that two adjacent entries never live in
    the same data block.  Most clients should not need to use this method.
    Does not flush the file itself.

    REQUIRES: self.finish(), self.abandon() have not been called
    """
    # Rep* r = rep_;
    r = self.rep_
    # assert(!r->closed);
    assert not r.closed
    # if (!ok()) return;
    if not self.ok():
      return
    # if (r->data_block.empty()) return;
    if r.data_block.empty():
      return
    # assert(!r->pending_index_entry);
    assert not r.pending_index_entry
    # WriteBlock(&r->data_block, &r->pending_handle);
    self.write_block(r.data_block, r.pending_handle)
    # if (ok()) {
    if self.ok():
      # r->pending_index_entry = true;
      r.pending_index_entry = True
      # // We don't flush the underlying file as that can be slow.
    # }


  # // Return non-ok iff some error has been detected.
  # Status status() const;
  def status(self):
    """Return non-ok iff some error has been detected."""
    return self.rep_.status

  # // Finish building the table.  Stops using the file passed to the
  # // constructor after this function returns.
  # // REQUIRES: Finish(), Abandon() have not been called
  # Status Finish();
  def finish(self) -> errors.Status:
    """Finish building the table.  Stops using the file passed to the
    constructor after this function returns.

    REQUIRES: Finish(), Abandon() have not been called
    """
    # Rep* r = rep_;
    r = self.rep_
    # Flush();
    self.flush()
    # assert(!r->closed);
    assert not r.closed
    # r->closed = true;
    r.closed = True

    # BlockHandle metaindex_block_handle, index_block_handle;
    metaindex_block_handle = table.BlockHandle()
    index_block_handle = table.BlockHandle()

    # // Write metaindex block
    # if (ok()) {
    if self.ok():
      # BlockBuilder meta_index_block(&r->options);
      meta_index_block = block_builder.BlockBuilder(r.options)
      # // TODO(postrelease): Add stats and other meta blocks
      # WriteBlock(&meta_index_block, &metaindex_block_handle);
      self.write_block(meta_index_block, metaindex_block_handle)
    # }

    # // Write index block
    # if (ok()) {
    if self.ok():
      # if (r->pending_index_entry) {
      if r.pending_index_entry:
        # FindShortSuccessor(&r->last_key);
        find_short_successor(r.last_key)
        # string handle_encoding;
        # r->pending_handle.EncodeTo(&handle_encoding);
        handle_encoding = r.pending_handle.encode_to()
        # r->index_block.Add(r->last_key, StringPiece(handle_encoding));
        r.index_block.add(r.last_key, core.StringPiece(handle_encoding))
        # r->pending_index_entry = false;
        r.pending_index_entry = False
      # }
      # WriteBlock(&r->index_block, &index_block_handle);
      self.write_block(r.index_block, index_block_handle)
    # }

    # // Write footer
    # if (ok()) {
    if self.ok():
      # Footer footer;
      footer = table.Footer()
      # footer.set_metaindex_handle(metaindex_block_handle);
      footer.set_metaindex_handle(metaindex_block_handle)
      # footer.set_index_handle(index_block_handle);
      footer.set_index_handle(index_block_handle)
      # string footer_encoding;
      # footer.EncodeTo(&footer_encoding);
      footer_encoding = footer.encode_to()
      # r->status = r->file->Append(footer_encoding);
      r.status = r.file.append(footer_encoding)
      # if (r->status.ok()) {
      if r.status.ok():
        # r->offset += footer_encoding.size();
        r.offset += len(footer_encoding)
      # }
    # }
    # return r->status;
    return r.status

  #
  # // Indicate that the contents of this builder should be abandoned.  Stops
  # // using the file passed to the constructor after this function returns.
  # // If the caller is not going to call Finish(), it must call Abandon()
  # // before destroying this builder.
  # // REQUIRES: Finish(), Abandon() have not been called
  # void Abandon();
  #
  # // Number of calls to Add() so far.
  # uint64 NumEntries() const;
  #
  # // Size of the file generated so far.  If invoked after a successful
  # // Finish() call, returns the size of the final generated file.
  # uint64 FileSize() const;

  #private:
  # bool ok() const { return status().ok(); }
  def ok(self):
    return self.status().ok()

  # void WriteBlock(BlockBuilder* block, BlockHandle* handle);
  def write_block(self, block: block_builder.BlockBuilder, handle: table.BlockHandle):
    # // File format contains a sequence of blocks where each block has:
    # //    block_data: uint8[n]
    # //    type: uint8
    # //    crc: uint32
    # assert(ok());
    assert self.ok()
    # Rep* r = rep_;
    r = self.rep_
    # StringPiece raw = block->Finish();
    raw = block.finish()

    # StringPiece block_contents;
    # CompressionType type = r->options.compression;
    type = r.options.compression
    # // TODO(postrelease): Support more compression options: zlib?
    # switch (type) {
    #   case kNoCompression:
    if type == table_options.kNoCompression:
      # block_contents = raw;
      block_contents = raw
      # break;
    #
    #   case kSnappyCompression: {
    elif type == table_options.kSnappyCompression:
      # string* compressed = &r->compressed_output;
      # if (port::Snappy_Compress(raw.data(), raw.size(), compressed) &&
      #     compressed->size() < raw.size() - (raw.size() / 8u)) {
      #   block_contents = *compressed;
      # } else {
      #   // Snappy not supported, or compressed less than 12.5%, so just
      #   // store uncompressed form
      #   block_contents = raw;
      #   type = kNoCompression;
      # }
      # break;
      raise NotImplementedError("TODO: Support SnappyCompression")
    #   }
    # }
    # WriteRawBlock(block_contents, type, handle);
    self.write_raw_block(block_contents, type, handle)
    # r->compressed_output.clear();
    r.compressed_output.clear()
    # block->Reset();
    block.reset()

  # void WriteRawBlock(const StringPiece& data, CompressionType,
  #                    BlockHandle* handle);
  def write_raw_block(self, block_contents: core.StringPiece, type: table_options.CompressionType, handle: table.BlockHandle):
    # Rep* r = rep_;
    r = self.rep_
    # handle->set_offset(r->offset);
    handle.set_offset(r.offset)
    # handle->set_size(block_contents.size());
    handle.set_size(block_contents.size())
    # r->status = r->file->Append(block_contents);
    r.status = r.file.append(block_contents)
    # if (r->status.ok()) {
    if r.status.ok():
      # char trailer[kBlockTrailerSize];
      trailer = bytearray(table.kBlockTrailerSize)
      # trailer[0] = type;
      trailer[0] = type
      # uint32 crc = crc32c::Value(block_contents.data(), block_contents.size());
      crc = core.crc32c.value(block_contents.data(), block_contents.size())
      # crc = crc32c::Extend(crc, trailer, 1);  // Extend crc to cover block type
      crc = core.crc32c.extend(crc, trailer, 1)  # Extend crc to cover block type
      # core::EncodeFixed32(trailer + 1, crc32c::Mask(crc));
      trailer[1:5] = coding.encode_fixed32(core.crc32c.mask(crc))
      # r->status = r->file->Append(StringPiece(trailer, kBlockTrailerSize));
      r.status = r.file.append(core.StringPiece(trailer, table.kBlockTrailerSize))
      # if (r->status.ok()) {
      if r.status.ok():
        # r->offset += block_contents.size() + kBlockTrailerSize;
        r.offset += block_contents.size() + table.kBlockTrailerSize
      # }
    # }

  #
  # struct Rep;
  # Rep* rep_;
  #
  # // No copying allowed
  # TableBuilder(const TableBuilder&);
  # void operator=(const TableBuilder&);
# };
