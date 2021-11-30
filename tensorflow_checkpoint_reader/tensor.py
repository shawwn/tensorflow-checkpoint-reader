from .pb.tensorflow.core.framework import types_pb2
from . import tensor_shape
from . import errors

from typing import Tuple, Optional

import numpy as np


class TensorBuffer:
  def __init__(self, data=None, array_offset=0, order="C"):
    self._data = data
    self._array_offset = array_offset
    self._order = order

  def data(self):
    return self._data

  def array_offset(self):
    return self._array_offset

  def order(self):
    return self._order


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

  def __repr__(self):
    return f"Tensor(is_initialized={self.is_initialized()}, shape={self.shape()!r})"

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

  def to_py(self) -> Tuple[errors.Status, Optional[np.ndarray]]:
    if not self.is_initialized():
      return errors.FailedPrecondition("Not initialized"), None
    shape = self.shape()
    dtype = shape.dtype()
    if dtype is None:
      return errors.Unimplemented("Data type ", shape.data_type(), " not supported"), None
    if self.num_elements() != 0:
      arr = np.ndarray.__new__(np.ndarray,
                               shape=shape.to_list(),
                               dtype=dtype,
                               buffer=self._buf.data(),
                               offset=self._buf.array_offset(),
                               order=self._buf.order())
      # a = np.frombuffer(self._buf.data(), dtype, shape.num_elements())
      # a = a.reshape(shape.to_list())
    else:
      arr = np.zeros(shape.to_list(), dtype)
    return errors.Status.OK(), arr
