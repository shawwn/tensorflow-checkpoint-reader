from .pb.tensorflow.core.framework import tensor_shape_pb2
from .pb.tensorflow.core.framework import types_pb2
from typing import Sequence, Optional

from . import errors
from . import numpy_util

import numpy as np

class TensorShape:
  def __init__(self, data_type: types_pb2.DataType = types_pb2.DT_INVALID):
    self._dims = []
    self._num_elements = 1
    self._data_type = data_type

  @classmethod
  def from_dims(cls, dims: Sequence[int]):
    self = cls()
    errors.raise_if_error(self.init_dims(dims))
    return self

  @classmethod
  def from_proto(cls, proto: tensor_shape_pb2.TensorShapeProto):
    self = cls()
    dims = [dim.size for dim in proto.dim]
    errors.raise_if_error(self.init_dims(dims))
    return self

  def to_list(self):
    return tuple(self._dims)

  def __repr__(self):
    return f"TensorShape(data_type={self.data_type()}, dtype={self.dtype()}, num_elements={self.num_elements()}, dims={self.to_list()})"

  def __iter__(self):
    return iter(self.to_list())

  def __len__(self):
    return len(self.to_list())

  def __getitem__(self, d):
    return self.to_list()[d]

  def max_dimensions(self):
    """Maximum number of dimensions in a tensor.
    It's 254 because 255 = kUnknownRank is used to represent unknown rank."""
    return 254

  def data_type(self) -> types_pb2.DataType:
    return self._data_type

  def dtype(self) -> Optional[np.dtype]:
    s, dtype = numpy_util.data_type_to_numpy_dtype(self.data_type())
    if s.ok():
      return dtype
    else:
      return None

  def set_data_type(self, data_type: types_pb2.DataType):
    self._data_type = data_type

  def ndims_byte(self) -> int:
    return len(self._dims)
  
  def dims(self) -> int:
    return len(self._dims)
  
  def num_elements(self) -> int:
    return self._num_elements
  
  def set_num_elements(self, n):
    self._num_elements = n
  
  def dim_size(self, d: int) -> int:
    return self._dims[d]

  def set_dim(self, d: int, size: int):
    assert d >= 0
    assert d < self.dims()
    self._dims[d] = size
  
  def init_dims(self, dim_sizes: Sequence[int]) -> errors.Status:
    self._dims.clear()
    self.set_num_elements(1)
    status = errors.Status.OK()
    for s in dim_sizes:
      status.update(self.add_dim_with_status(s))
      if not status.ok():
        return status
    return status

  def add_dim_with_status(self, size: int) -> errors.Status:
    if self.ndims_byte() >= self.max_dimensions():
      return errors.Internal("Too many dimensions in tensor")
    
    assert size >= 0
    new_num_elements = self.num_elements() * size
    if new_num_elements < 0:
      return errors.Internal("Encountered overflow when multiplying ",
                             self.num_elements(), " with ", size,
                             ", result: ", new_num_elements)

    self.unsafe_add_dim(size, new_num_elements)
    return errors.Status.OK()

  def unsafe_add_dim(self, size: int, new_num_elements: int):
    self._dims.append(size)
    self.set_num_elements(new_num_elements)


    
    