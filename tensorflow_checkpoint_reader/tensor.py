from .pb.tensorflow.core.framework import types_pb2
from . import tensor_shape

import numpy as np

class TensorBuffer:
  def __init__(self, data = None):
    self._data = data

  def data(self):
    return self._data

class Tensor:
  def __init__(self,
               type: types_pb2.DataType = types_pb2.DT_FLOAT,
               shape: tensor_shape.TensorShape = None,
               buf: TensorBuffer = None):
    if shape is None:
      shape = tensor_shape.TensorShape()
    shape.set_data_type(type)
    self._shape = shape
    self._buf = buf

  def shape(self) -> tensor_shape.TensorShape:
    return self._shape

  def dtype(self) -> types_pb2.DataType:
    return self._shape.data_type()
  
  def dims(self) -> int:
    return self.shape().dims()

  def dim_size(self, d: int) -> int:
    return self.shape().dim_size(d)

  def num_elements(self) -> int:
    return self.shape().num_elements()

  def is_initialized(self) -> bool:
    """If necessary, has this Tensor been initialized?

    Zero-element Tensors are always considered initialized, even if they
    have never been assigned to and do not have any memory allocated."""
    return (self._buf is not None and self._buf.data() is not None) or self.num_elements() == 0

  def set_data(self, buf: TensorBuffer):
    self._buf = buf

  def to_py(self) -> np.ndarray:
    assert self.is_initialized()
    data_type = self.dtype()
    assert data_type is types_pb2.DT_FLOAT
    dtype = np.float32
    shape = self.shape().to_list()
    if self.num_elements() != 0:
      a = np.frombuffer(self._buf.data(), dtype, self.shape().num_elements())
      return a.reshape(shape)
    else:
      return np.zeros(shape, dtype)
