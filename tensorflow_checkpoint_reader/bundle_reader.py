from . import table
from . import env
from . import core
from . import errors
from . import naming
from . import tensor
from . import tensor_shape
from . import file_system
from . import file_system_helper
from .pb.tensorflow.core.protobuf import tensor_bundle_pb2
from .pb.tensorflow.core.framework import types_pb2

from typing import Tuple, Optional, List
import time
import sys

import numpy as np
import mmap

class BundleReader:
  _data: List[Optional[file_system.RandomAccessFile]]
  _mmap: List[Optional[mmap.mmap]]

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
    self._mmap = [None for _ in range(header.num_shards)]
    self._entries = []
    self._tensors = []
    self._num_shards = header.num_shards
    now = time.time()
    while iter2.valid():
      key = iter2.key().bytes()
      # print(key)
      val = tensor_bundle_pb2.BundleEntryProto()
      val.ParseFromString(iter2.value().bytes())
      self._entries.append((key, val))
      # arr = errors.raise_if_error(self.get_value(val)).to_py()
      arr = errors.raise_if_error(self.get_numpy(val))
      self._tensors.append((key, arr))
      # print(key, arr.shape)
      # print(arr.reshape((-1,))[0])
      # print(arr)
      # print(arr.sum(axis=-1))
      iter2.next()
    # file_system_helper.for_each(0, len(self._tensors), lambda i: print(self._env.get_current_thread_id(), self._tensors[i][0], self._tensors[i][1].sum()))
    elapsed = time.time() - now
    print('%0.2f msec' % (elapsed * 1000.0), file=sys.stderr)

  def get_file(self, entry: tensor_bundle_pb2.BundleEntryProto) -> Tuple[errors.Status, Optional[file_system.RandomAccessFile]]:
    # Open the data file if it has not been opened.
    file = self._data[entry.shard_id]
    if file is None:
      s, file = self._env.new_random_access_file(naming.data_filename(self._prefix, entry.shard_id, self._num_shards))
      if not s.ok():
        return s, None
      self._data[entry.shard_id] = file
      fileno = getattr(file, '_fd', None)
      if fileno is not None:
        # bytes = entry.offset + entry.size
        # offset = entry.offset
        # start = offset - offset % mmap.ALLOCATIONGRANULARITY
        # bytes -= start
        # array_offset = offset - start
        bytes = 0
        start = 0
        mm = mmap.mmap(fileno, bytes, access=mmap.ACCESS_READ, offset=start)
        self._mmap[entry.shard_id] = mm
    assert file is not None
    return errors.Status.OK(), file

  def get_mmap(self, entry: tensor_bundle_pb2.BundleEntryProto) -> Tuple[errors.Status, Optional[mmap.mmap]]:
    mm = self._mmap[entry.shard_id]
    if mm is None:
      s, file = self.get_file(entry)
      if not s.ok():
        return s, None
      fileno = getattr(file, '_fd', None)
      if fileno is not None:
        bytes = 0
        start = 0
        mm = mmap.mmap(fileno, bytes, access=mmap.ACCESS_READ, offset=start)
        self._mmap[entry.shard_id] = mm
    if mm is None:
      return errors.Unavailable("Can't mmap file"), None
    else:
      return errors.Status.OK(), mm

  def get_value(self, entry: tensor_bundle_pb2.BundleEntryProto) -> Tuple[errors.Status, Optional[tensor.Tensor]]:
    stored_shape = tensor_shape.TensorShape.from_proto(entry.shape)
    ret = tensor.Tensor(entry.dtype, stored_shape)
    s, file = self.get_file(entry)
    if not s.ok():
      return s, None
    s, mm = self.get_mmap(entry)
    if not s.ok():
      s, sp = file.read(entry.offset, entry.size)
      if not s.ok():
        return s, None
      buf = tensor.TensorBuffer(sp.bytes())
    else:
      array_offset = entry.offset
      buf = tensor.TensorBuffer(mm, array_offset, order="C")
    ret.set_data(buf)
    return errors.Status.OK(), ret

  def get_numpy(self, entry: tensor_bundle_pb2.BundleEntryProto) -> Tuple[errors.Status, Optional[np.ndarray]]:
    s, tensor_value = self.get_value(entry)
    if not s.ok():
      return s, None
    return tensor_value.to_py()

