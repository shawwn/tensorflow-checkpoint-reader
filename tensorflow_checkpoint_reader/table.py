from . import errors
from . import core
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
    magic = core.decode_fixed_64(input.data, Footer.kEncodedLength - 8)
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


def read_block(file: core.RandomAccessFile, handle: BlockHandle) -> BlockContents:
  result = BlockContents()
  # result.data = core.StringPiece(b'')
  # result.cacheable = False
  # result.heap_allocated = False
  n = handle.size
  contents = file.read(handle.offset, n + kBlockTrailerSize)
  if contents.size != n + kBlockTrailerSize:
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
  data = contents.data
  if data[n] == CompressionType.kNoCompression.value:
    result.data = core.StringPiece(data, n)
    result.cacheable = False
    result.heap_allocated = False
  else:
    raise NotImplementedError()
  return result


class Block:
  def __init__(self, contents: BlockContents):
    self._data = contents.data.data
    self._size = contents.data.size
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


class Table:
  class Rep(NamedTuple):
    file: core.RandomAccessFile
    metaindex_handle: BlockHandle
    index_block: Block

  def __init__(self, rep: Rep):
    self._rep = rep

  @classmethod
  def open(cls, file: core.RandomAccessFile, size: int):
    if size < Footer.kEncodedLength:
      raise errors.DataLoss("file is too short to be an sstable")
    footer_input = file.read(size - Footer.kEncodedLength, Footer.kEncodedLength)
    footer = Footer()
    footer.decode_from(footer_input)

    contents: BlockContents = read_block(file, footer.index_handle)
    # We've successfully read the footer and the index block: we're
    # ready to serve requests.
    index_block = Block(contents)

    rep = Table.Rep(file, footer.metaindex_handle, index_block)
    return cls(rep)
    
