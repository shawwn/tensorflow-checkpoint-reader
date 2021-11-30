from . import errors
from . import core
from . import file_system
from . import iterator
import struct
from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple

# kTableMagicNumber was picked by running
#    echo http://code.google.com/p/leveldb/ | sha1sum
# and taking the leading 64 bits.
kTableMagicNumber = 0xdb4775248b80fb57

# 1-byte type + 32-bit crc
kBlockTrailerSize = 5


# DB contents are stored in a set of blocks, each of which holds a
# sequence of key,value pairs.  Each block may be compressed before
# being stored in a file.  The following enum describes which
# compression method (if any) is used to compress a block.
class CompressionType(Enum):
  # NOTE: do not change the values of existing entries, as these are
  # part of the persistent format on disk.
  kNoCompression = 0x0
  kSnappyCompression = 0x1


class BlockHandle:
  kMaxEncodedLength = 10 + 10

  def __init__(self):
    self._offset = 0
    self._size = 0

  @property
  def offset(self) -> int:
    return self._offset

  @property
  def size(self) -> int:
    return self._size

  def decode_from(self, input: core.StringPiece):
    ok, self._offset = core.get_varint_64(input)
    if ok:
      ok, self._size = core.get_varint_64(input)
      if ok:
        return
    raise errors.DataLoss("bad block handle")


class Footer:
  kEncodedLength = 2 * BlockHandle.kMaxEncodedLength + 8

  def __init__(self):
    self._metaindex_handle = BlockHandle()
    self._index_handle = BlockHandle()

  @property
  def index_handle(self) -> BlockHandle:
    return self._index_handle

  @property
  def metaindex_handle(self) -> BlockHandle:
    return self._metaindex_handle

  def decode_from(self, input: core.StringPiece):
    magic = core.decode_fixed_64(input.slice(), Footer.kEncodedLength - 8)
    if magic != kTableMagicNumber:
      raise errors.DataLoss("not an sstable (bad magic number)");
    self._metaindex_handle.decode_from(input)
    self._index_handle.decode_from(input)
    # We skip over any leftover data (just padding for now) in "input"
    #end = Footer.kEncodedLength


class BlockContents:
  data: core.StringPiece # Actual contents of data
  cacheable: bool        # True iff data can be cached
  heap_allocated: bool   # True iff caller should delete[] data.data()


def read_block(file: file_system.RandomAccessFile, handle: BlockHandle) -> BlockContents:
  result = BlockContents()
  # result.data = core.StringPiece(b'')
  # result.cacheable = False
  # result.heap_allocated = False
  n = handle.size
  contents = errors.raise_if_error(file.read(handle.offset, n + kBlockTrailerSize))
  if contents.size() != n + kBlockTrailerSize:
    raise errors.DataLoss("truncated block read")

  # // Check the crc of the type and the block contents
  # const char* data = contents.data();  // Pointer to where Read put the data
  # // This checksum verification is optional.  We leave it on for now
  # const bool verify_checksum = true;
  # if (verify_checksum) {
  #   const uint32 crc = crc32c::Unmask(core::DecodeFixed32(data + n + 1));
  #   const uint32 actual = crc32c::Value(data, n + 1);
  #   if (actual != crc) {
  #     delete[] buf;
  #     s = errors::DataLoss("block checksum mismatch");
  #     return s;
  #   }
  # }
  data = contents.slice()
  if data[n] == CompressionType.kNoCompression.value:
    result.data = core.StringPiece(data, n)
    result.cacheable = False
    result.heap_allocated = False
  else:
    raise NotImplementedError()
  return result


def decode_entry(data: bytes, p, limit):
  if limit - p < 3:
    return None
  shared = data[p + 0]
  non_shared = data[p + 1]
  value_length = data[p + 2]
  if (shared | non_shared | value_length) < 128:
    # Fast path: all three values are encoded in one byte each
    p += 3
  else:
    p, shared = core.get_varint_32_ptr(data, p, limit)
    if p is not None:
      p, non_shared = core.get_varint_32_ptr(data, p, limit)
    if p is not None:
      p, value_length = core.get_varint_32_ptr(data, p, limit)
    # if ((p = core::GetVarint32Ptr(p, limit, shared)) == nullptr) return nullptr;
    # if ((p = core::GetVarint32Ptr(p, limit, non_shared)) == nullptr)
    #   return nullptr;
    # if ((p = core::GetVarint32Ptr(p, limit, value_length)) == nullptr)
    #   return nullptr;
  return p, shared, non_shared, value_length


class Block:
  class Iter(iterator.Iterator):
    def __init__(self, data, restarts: int, num_restarts: int):
      self._data = data
      self._restarts = restarts
      self._num_restarts = num_restarts
      self._current = self._restarts
      self._restart_index = self._num_restarts
      self._key = b""
      self._value = core.StringPiece()
      self._status = None
      assert self._num_restarts > 0

    def next_entry_offset(self) -> int:
      # return (value_.data() + value_.size()) - data_;
      return self._value._offset + self._value.size()

    def get_restart_point(self, index: int) -> int:
      assert index < self._num_restarts
      # return core::DecodeFixed32(data_ + restarts_ + index * sizeof(uint32));
      return core.decode_fixed_32(self._data, self._restarts + index * 4)

    def seek_to_restart_point(self, index: int):
      self._Key = b""
      self._restart_index = index
      # current_ will be fixed by ParseNextKey()

      # ParseNextKey() starts at the end of value_, so set value_ accordingly
      offset = self.get_restart_point(index)
      self._value = core.StringPiece(self._data, 0, offset)

    def status(self):
      if self._status is not None:
        raise self._status

    def valid(self) -> bool:
      return self._current < self._restarts

    def key(self) -> core.StringPiece:
      assert self.valid()
      return core.StringPiece(self._key)

    def value(self) -> core.StringPiece:
      assert self.valid()
      return self._value

    def next(self):
      assert self.valid()
      self.parse_next_key()

    def seek(self, target: core.StringPiece):
      # Binary search in restart array to find the last restart point
      # with a key < target
      raise NotImplementedError()

    def seek_to_first(self):
      self.seek_to_restart_point(0)
      self.parse_next_key()

    def corruption_error(self):
      breakpoint()
      self._current = self._restarts
      self._restart_index = self._num_restarts
      self._status = errors.DataLoss("bad entry in block")
      self._key = b''
      self._value = core.StringPiece()

    def parse_next_key(self) -> bool:
      self._current = self.next_entry_offset()
      p = self._current
      limit = self._restarts  # Restarts come right after data
      if p >= limit:
        # No more entries to return.  Mark as invalid.
        self._current = self._restarts
        self._restart_index = self._num_restarts
        return False
      # Decode next entry
      p, shared, non_shared, value_length = decode_entry(self._data, p, limit)
      # breakpoint()
      if p is None:
        self.corruption_error()
        return False
      elif len(self._key) < shared:
        self.corruption_error()
        return False
      else:
        # key_.resize(shared);
        if len(self._key) < shared:
          self._key = b' ' * shared
        elif len(self._key) > shared:
          self._key = self._key[0:shared]
        # key_.append(p, non_shared)
        self._key += self._data[p:p + non_shared]
        self._value = core.StringPiece(self._data, value_length, p + non_shared)
        while self._restart_index + 1 < self._num_restarts and \
                self.get_restart_point(self._restart_index + 1) < self._current:
          self._restart_index += 1
        return True


  def __init__(self, contents: BlockContents):
    self._data = contents.data.slice()
    self._size = contents.data.size()
    self._owned = contents.heap_allocated
    if self._size < 4:
      breakpoint()
      self._size = 0 # Error marker
    else:
      max_restarts_allowed = (self._size - 4) // 4
      if self.num_restarts() > max_restarts_allowed:
        # The size is too small for NumRestarts()
        breakpoint()
        self._size = 0
      else:
        self._restart_offset = self._size - (1 + self.num_restarts()) * 4

  def num_restarts(self):
     return core.decode_fixed_32(self._data, self._size - 4)

  def new_iterator(self) -> iterator.Iterator:
    if self._size < 4:
      return iterator.new_error_iterator(errors.DataLoss("bad block contents"))
    num_restarts = self.num_restarts()
    if num_restarts <= 0:
      return iterator.new_empty_iterator()
    else:
      return Block.Iter(self._data, self._restart_offset, num_restarts)


class Table:
  class Rep(NamedTuple):
    file: file_system.RandomAccessFile
    metaindex_handle: BlockHandle
    index_block: Block

  def __init__(self, rep: Rep):
    self._rep = rep

  @classmethod
  def open(cls, file: file_system.RandomAccessFile, size: int):
    if size < Footer.kEncodedLength:
      raise errors.DataLoss("file is too short to be an sstable")
    footer_input = errors.raise_if_error(file.read(size - Footer.kEncodedLength, Footer.kEncodedLength))
    footer = Footer()
    footer.decode_from(footer_input)

    contents: BlockContents = read_block(file, footer.index_handle)
    # We've successfully read the footer and the index block: we're
    # ready to serve requests.
    index_block = Block(contents)

    rep = Table.Rep(file, footer.metaindex_handle, index_block)
    return cls(rep)
    
