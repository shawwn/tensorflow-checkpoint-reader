from . import errors
from . import core
import struct

# kTableMagicNumber was picked by running
#    echo http://code.google.com/p/leveldb/ | sha1sum
# and taking the leading 64 bits.
kTableMagicNumber = 0xdb4775248b80fb57


class BlockHandle:
  kMaxEncodedLength = 10 + 10

  def __init__(self):
    self._offset = 0
    self._size = 0

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

  def decode_from(self, input: core.StringPiece):
    magic = core.decode_fixed_64(input.data, Footer.kEncodedLength - 8)
    if magic != kTableMagicNumber:
      raise errors.DataLoss("not an sstable (bad magic number)");
    self._metaindex_handle.decode_from(input)
    self._index_handle.decode_from(input)
    # We skip over any leftover data (just padding for now) in "input"
    #end = Footer.kEncodedLength


class Table:
  @classmethod
  def open(cls, file: core.RandomAccessFile, size: int):
    if size < Footer.kEncodedLength:
      raise errors.DataLoss("file is too short to be an sstable")
    footer_input = file.read(size - Footer.kEncodedLength, Footer.kEncodedLength)
    footer = Footer()
    footer.decode_from(footer_input)
    breakpoint()
    
