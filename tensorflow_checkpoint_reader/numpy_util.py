from .pb.tensorflow.core.framework import types_pb2
from . import errors

from typing import Tuple, Optional

import numpy as np
try:
  from jaxlib import xla_client as xc
except ImportError:
  xc = None

def data_type_to_numpy_dtype(type: types_pb2.DataType) -> Tuple[errors.Status, Optional[np.dtype]]:
  # DT_INVALID = 0
  # DT_FLOAT = 1
  # DT_DOUBLE = 2
  # DT_INT32 = 3
  # DT_UINT8 = 4
  # DT_INT16 = 5
  # DT_INT8 = 6
  # DT_STRING = 7
  # DT_COMPLEX64 = 8
  # DT_INT64 = 9
  # DT_BOOL = 10
  # DT_QINT8 = 11
  # DT_QUINT8 = 12
  # DT_QINT32 = 13
  # DT_BFLOAT16 = 14
  # DT_QINT16 = 15
  # DT_QUINT16 = 16
  # DT_UINT16 = 17
  # DT_COMPLEX128 = 18
  # DT_HALF = 19
  # DT_RESOURCE = 20
  # DT_VARIANT = 21
  # DT_UINT32 = 22
  # DT_UINT64 = 23
  dtype = None
  if type == types_pb2.DT_FLOAT:
    dtype = np.float32
  elif type == types_pb2.DT_DOUBLE:
    dtype = np.float64
  elif type == types_pb2.DT_INT32:
    dtype = np.int32
  elif type == types_pb2.DT_UINT8:
    dtype = np.uint8
  elif type == types_pb2.DT_INT16:
    dtype = np.int16
  elif type == types_pb2.DT_INT8:
    dtype = np.int8
  elif type == types_pb2.DT_STRING:
    dtype = np.dtype(bytes)
  elif type == types_pb2.DT_COMPLEX64:
    dtype = np.complex64
  elif type == types_pb2.DT_INT64:
    dtype = np.int64
  elif type == types_pb2.DT_BOOL:
    dtype = np.bool
  # elif type == types_pb2.DT_QINT8:
  #   dtype = np.qint8
  # elif type == types_pb2.DT_QUINT8:
  #   dtype = np.quint8
  # elif type == types_pb2.DT_QINT32:
  #   dtype = np.qint32
  elif type == types_pb2.DT_BFLOAT16:
    if xc is not None:
      dtype = xc.bfloat16
  # elif type == types_pb2.DT_QINT16:
  #   dtype = np.qint16
  # elif type == types_pb2.DT_QUINT16:
  #   dtype = np.quint16
  elif type == types_pb2.DT_UINT16:
    dtype = np.uint16
  elif type == types_pb2.DT_COMPLEX128:
    dtype = np.complex128
  elif type == types_pb2.DT_HALF:
    dtype = np.half
  # elif type == types_pb2.DT_RESOURCE:
  #   return errors.Unimplemented("DT_RESOURCE can't be converted to a numpy dtype"), None
  # elif type == types_pb2.DT_VARIANT:
  #   return errors.Unimplemented("DT_VARAINT can't be converted to a numpy dtype"), None
  elif type == types_pb2.DT_UINT32:
    dtype = np.uint32
  elif type == types_pb2.DT_UINT64:
    dtype = np.uint64
  if dtype is None:
    return errors.Unimplemented("Can't convert data type ", type, " to numpy dtype"), None
  return errors.Status.OK(), dtype
