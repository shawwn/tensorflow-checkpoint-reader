from . import table
from . import core
from . import env
from . import errors
from .pb.tensorflow.core.protobuf import tensor_bundle_pb2
import os

def meta_filename(prefix: str):
  return '%s.index' % prefix

class BundleReader:
  def __init__(self, env_: env.Env, prefix: str):
    filename = meta_filename(prefix)
    file_size = errors.raise_if_error(env_.get_file_size(filename))
    self._metadata = errors.raise_if_error(env_.new_random_access_file(filename))
    self._table = table.Table.open(self._metadata, file_size)
    iter = self._table._rep.index_block.new_iterator()
    iter.seek_to_first()
    #proto = tensor_bundle_pb2.BundleHeaderProto()
    #proto.ParseFromString(iter._value._data[iter._value.offset + iter._value.size:])
    handle = table.BlockHandle()
    handle.decode_from(iter.value())
    zz = table.Block(table.read_block(self._metadata, handle))
    iter2 = zz.new_iterator()
    iter2.seek_to_first()
    while iter2.valid():
      iter2.next()
      if iter2.valid():
        print(iter2.key().bytes())
    breakpoint()

