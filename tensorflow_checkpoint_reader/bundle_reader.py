from . import table
from . import env
from . import core
from . import errors
from . import naming
from . import tensor
from . import tensor_shape
from . import file_system
from .pb.tensorflow.core.protobuf import tensor_bundle_pb2

from typing import Tuple, Optional, List

class BundleReader:
  _data: List[Optional[file_system.RandomAccessFile]]

  def __init__(self, env_: env.Env, prefix):
    self._prefix = core.string_view(prefix).bytes()
    self._env = env_
    filename = naming.meta_filename(self._prefix)
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
    header = tensor_bundle_pb2.BundleHeaderProto()
    header.ParseFromString(iter2.value().bytes())
    iter2.next()
    self._data = [None for _ in range(header.num_shards)]
    self._tensors = []
    self._num_shards = header.num_shards
    while iter2.valid():
      key = iter2.key().bytes()
      print(key)
      val = tensor_bundle_pb2.BundleEntryProto()
      val.ParseFromString(iter2.value().bytes())
      arr = errors.raise_if_error(self.get_value(val)).to_py()
      self._tensors.append((key, arr))
      print(arr.shape)
      iter2.next()
    breakpoint()

  def get_value(self, entry: tensor_bundle_pb2.BundleEntryProto) -> Tuple[errors.Status, Optional[tensor.Tensor]]:
    stored_shape = tensor_shape.TensorShape.from_proto(entry.shape)
    ret = tensor.Tensor(entry.dtype, stored_shape)
    # Open the data file if it has not been opened.
    file = self._data[entry.shard_id]
    if file is None:
      s, file = self._env.new_random_access_file(naming.data_filename(self._prefix, entry.shard_id, self._num_shards))
      if not s.ok():
        return s, None
      self._data[entry.shard_id] = file
    assert file is not None
    s, sp = file.read(entry.offset, entry.size)
    if not s.ok():
      return s, None
    ret.set_data(tensor.TensorBuffer(sp.bytes()))
    return errors.Status.OK(), ret


