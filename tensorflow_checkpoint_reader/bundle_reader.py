from . import table
from . import core
import os

def meta_filename(prefix: str):
  return '%s.index' % prefix

class BundleReader:
  def __init__(self, prefix: str):
    filename = meta_filename(prefix)
    file_size = os.path.getsize(filename)
    self._metadata = core.RandomAccessFile(open(filename, 'rb'))
    self._table = table.Table.open(self._metadata, file_size)
    breakpoint()

