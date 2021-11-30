from .pb.tensorflow.core.framework import types_pb2
from . import errors

from typing import Tuple, Optional
import builtins

import numpy as np
try:
  from jaxlib import xla_client as _xc
  _np_bfloat16 = _xc.bfloat16
except ImportError:
  _np_bfloat16 = None

# Standard mappings between types_pb2.DataType values and string names.
_TYPE_TO_STRING = {
  types_pb2.DT_HALF: "float16",
  types_pb2.DT_FLOAT: "float32",
  types_pb2.DT_DOUBLE: "float64",
  types_pb2.DT_INT32: "int32",
  types_pb2.DT_UINT8: "uint8",
  types_pb2.DT_UINT16: "uint16",
  types_pb2.DT_UINT32: "uint32",
  types_pb2.DT_UINT64: "uint64",
  types_pb2.DT_INT16: "int16",
  types_pb2.DT_INT8: "int8",
  types_pb2.DT_STRING: "string",
  types_pb2.DT_COMPLEX64: "complex64",
  types_pb2.DT_COMPLEX128: "complex128",
  types_pb2.DT_INT64: "int64",
  types_pb2.DT_BOOL: "bool",
  types_pb2.DT_QINT8: "qint8",
  types_pb2.DT_QUINT8: "quint8",
  types_pb2.DT_QINT16: "qint16",
  types_pb2.DT_QUINT16: "quint16",
  types_pb2.DT_QINT32: "qint32",
  types_pb2.DT_BFLOAT16: "bfloat16",
  types_pb2.DT_RESOURCE: "resource",
  types_pb2.DT_VARIANT: "variant",
  types_pb2.DT_HALF_REF: "float16_ref",
  types_pb2.DT_FLOAT_REF: "float32_ref",
  types_pb2.DT_DOUBLE_REF: "float64_ref",
  types_pb2.DT_INT32_REF: "int32_ref",
  types_pb2.DT_UINT32_REF: "uint32_ref",
  types_pb2.DT_UINT8_REF: "uint8_ref",
  types_pb2.DT_UINT16_REF: "uint16_ref",
  types_pb2.DT_INT16_REF: "int16_ref",
  types_pb2.DT_INT8_REF: "int8_ref",
  types_pb2.DT_STRING_REF: "string_ref",
  types_pb2.DT_COMPLEX64_REF: "complex64_ref",
  types_pb2.DT_COMPLEX128_REF: "complex128_ref",
  types_pb2.DT_INT64_REF: "int64_ref",
  types_pb2.DT_UINT64_REF: "uint64_ref",
  types_pb2.DT_BOOL_REF: "bool_ref",
  types_pb2.DT_QINT8_REF: "qint8_ref",
  types_pb2.DT_QUINT8_REF: "quint8_ref",
  types_pb2.DT_QINT16_REF: "qint16_ref",
  types_pb2.DT_QUINT16_REF: "quint16_ref",
  types_pb2.DT_QINT32_REF: "qint32_ref",
  types_pb2.DT_BFLOAT16_REF: "bfloat16_ref",
  types_pb2.DT_RESOURCE_REF: "resource_ref",
  types_pb2.DT_VARIANT_REF: "variant_ref",
}
_STRING_TO_TYPE = {
  value: key for key, value in _TYPE_TO_STRING.items()
}
# Add non-canonical aliases.
_STRING_TO_TYPE["half"] = types_pb2.DT_HALF
_STRING_TO_TYPE["half_ref"] = types_pb2.DT_HALF_REF
_STRING_TO_TYPE["float"] = types_pb2.DT_FLOAT
_STRING_TO_TYPE["float_ref"] = types_pb2.DT_FLOAT_REF
_STRING_TO_TYPE["double"] = types_pb2.DT_DOUBLE
_STRING_TO_TYPE["double_ref"] = types_pb2.DT_DOUBLE_REF




# Numpy representation for quantized dtypes.
#
# These are magic strings that are used in the swig wrapper to identify
# quantized types.
# TODO(mrry,keveman): Investigate Numpy type registration to replace this
# hard-coding of names.
_np_qint8 = np.dtype([("qint8", np.int8)])
_np_quint8 = np.dtype([("quint8", np.uint8)])
_np_qint16 = np.dtype([("qint16", np.int16)])
_np_quint16 = np.dtype([("quint16", np.uint16)])
_np_qint32 = np.dtype([("qint32", np.int32)])

# _np_bfloat16 is defined by a module import.

# Custom struct dtype for directly-fed ResourceHandles of supported type(s).
_np_resource = np.dtype([("resource", np.ubyte)])

# Standard mappings between types_pb2.DataType values and numpy.dtypes.
_NP_TO_TYPE = {
  np.float16: types_pb2.DT_HALF,
  np.float32: types_pb2.DT_FLOAT,
  np.float64: types_pb2.DT_DOUBLE,
  np.int32: types_pb2.DT_INT32,
  np.int64: types_pb2.DT_INT64,
  np.uint8: types_pb2.DT_UINT8,
  np.uint16: types_pb2.DT_UINT16,
  np.uint32: types_pb2.DT_UINT32,
  np.uint64: types_pb2.DT_UINT64,
  np.int16: types_pb2.DT_INT16,
  np.int8: types_pb2.DT_INT8,
  np.complex64: types_pb2.DT_COMPLEX64,
  np.complex128: types_pb2.DT_COMPLEX128,
  np.object_: types_pb2.DT_STRING,
  np.string_: types_pb2.DT_STRING,
  np.unicode_: types_pb2.DT_STRING,
  np.bool_: types_pb2.DT_BOOL,
  _np_qint8: types_pb2.DT_QINT8,
  _np_quint8: types_pb2.DT_QUINT8,
  _np_qint16: types_pb2.DT_QINT16,
  _np_quint16: types_pb2.DT_QUINT16,
  _np_qint32: types_pb2.DT_QINT32,
}
if _np_bfloat16 is not None:
  _NP_TO_TYPE[_np_bfloat16] = types_pb2.DT_BFLOAT16


# Map (some) NumPy platform dtypes to TF ones using their fixed-width
# synonyms. Note that platform dtypes are not always simples aliases,
# i.e. reference equality is not guaranteed. See e.g. numpy/numpy#9799.
for pdt in [
  np.intc,
  np.uintc,
  np.int_,
  np.uint,
  np.longlong,
  np.ulonglong,
]:
  if pdt not in _NP_TO_TYPE:
    _NP_TO_TYPE[pdt] = next(
      _NP_TO_TYPE[dt] for dt in _NP_TO_TYPE if dt == pdt().dtype)  # pylint: disable=no-value-for-parameter


TYPE_VALUE_DTYPES = set(_NP_TO_TYPE.values())

_TYPE_TO_NP = {
  types_pb2.DT_HALF:
    np.float16,
  types_pb2.DT_FLOAT:
    np.float32,
  types_pb2.DT_DOUBLE:
    np.float64,
  types_pb2.DT_INT32:
    np.int32,
  types_pb2.DT_UINT8:
    np.uint8,
  types_pb2.DT_UINT16:
    np.uint16,
  types_pb2.DT_UINT32:
    np.uint32,
  types_pb2.DT_UINT64:
    np.uint64,
  types_pb2.DT_INT16:
    np.int16,
  types_pb2.DT_INT8:
    np.int8,
  # NOTE(touts): For strings we use np.object as it supports variable length
  # strings.
  types_pb2.DT_STRING:
    np.object,
  types_pb2.DT_COMPLEX64:
    np.complex64,
  types_pb2.DT_COMPLEX128:
    np.complex128,
  types_pb2.DT_INT64:
    np.int64,
  types_pb2.DT_BOOL:
    np.bool_,
  types_pb2.DT_QINT8:
    _np_qint8,
  types_pb2.DT_QUINT8:
    _np_quint8,
  types_pb2.DT_QINT16:
    _np_qint16,
  types_pb2.DT_QUINT16:
    _np_quint16,
  types_pb2.DT_QINT32:
    _np_qint32,
  types_pb2.DT_BFLOAT16:
    _np_bfloat16,

  # Ref types
  types_pb2.DT_HALF_REF:
    np.float16,
  types_pb2.DT_FLOAT_REF:
    np.float32,
  types_pb2.DT_DOUBLE_REF:
    np.float64,
  types_pb2.DT_INT32_REF:
    np.int32,
  types_pb2.DT_UINT32_REF:
    np.uint32,
  types_pb2.DT_UINT8_REF:
    np.uint8,
  types_pb2.DT_UINT16_REF:
    np.uint16,
  types_pb2.DT_INT16_REF:
    np.int16,
  types_pb2.DT_INT8_REF:
    np.int8,
  types_pb2.DT_STRING_REF:
    np.object,
  types_pb2.DT_COMPLEX64_REF:
    np.complex64,
  types_pb2.DT_COMPLEX128_REF:
    np.complex128,
  types_pb2.DT_INT64_REF:
    np.int64,
  types_pb2.DT_UINT64_REF:
    np.uint64,
  types_pb2.DT_BOOL_REF:
    np.bool,
  types_pb2.DT_QINT8_REF:
    _np_qint8,
  types_pb2.DT_QUINT8_REF:
    _np_quint8,
  types_pb2.DT_QINT16_REF:
    _np_qint16,
  types_pb2.DT_QUINT16_REF:
    _np_quint16,
  types_pb2.DT_QINT32_REF:
    _np_qint32,
  types_pb2.DT_BFLOAT16_REF:
    _np_bfloat16,
}

_PYTHON_TO_TYPE = {
  builtins.float: types_pb2.DT_FLOAT,
  builtins.int: types_pb2.DT_INT32,
  builtins.bool: types_pb2.DT_BOOL,
  builtins.object: types_pb2.DT_STRING,
  builtins.str: types_pb2.DT_STRING,
  builtins.bytes: types_pb2.DT_STRING,
}

def data_type_to_numpy_dtype(type: types_pb2.DataType) -> Tuple[errors.Status, Optional[np.dtype]]:
  if type in _TYPE_TO_NP:
    return errors.Status.OK(), _TYPE_TO_NP[type]
  else:
    return errors.Unimplemented("Can't convert data type ", _TYPE_TO_STRING.get(type, type), " to numpy dtype"), None
#
# def data_type_to_numpy_dtype_old(type: types_pb2.DataType) -> Tuple[errors.Status, Optional[np.dtype]]:
#   # DT_INVALID = 0
#   # DT_FLOAT = 1
#   # DT_DOUBLE = 2
#   # DT_INT32 = 3
#   # DT_UINT8 = 4
#   # DT_INT16 = 5
#   # DT_INT8 = 6
#   # DT_STRING = 7
#   # DT_COMPLEX64 = 8
#   # DT_INT64 = 9
#   # DT_BOOL = 10
#   # DT_QINT8 = 11
#   # DT_QUINT8 = 12
#   # DT_QINT32 = 13
#   # DT_BFLOAT16 = 14
#   # DT_QINT16 = 15
#   # DT_QUINT16 = 16
#   # DT_UINT16 = 17
#   # DT_COMPLEX128 = 18
#   # DT_HALF = 19
#   # DT_RESOURCE = 20
#   # DT_VARIANT = 21
#   # DT_UINT32 = 22
#   # DT_UINT64 = 23
#   dtype = None
#   if type == types_pb2.DT_FLOAT:
#     dtype = np.float32
#   elif type == types_pb2.DT_DOUBLE:
#     dtype = np.float64
#   elif type == types_pb2.DT_INT32:
#     dtype = np.int32
#   elif type == types_pb2.DT_UINT8:
#     dtype = np.uint8
#   elif type == types_pb2.DT_INT16:
#     dtype = np.int16
#   elif type == types_pb2.DT_INT8:
#     dtype = np.int8
#   elif type == types_pb2.DT_STRING:
#     dtype = np.dtype(bytes)
#   elif type == types_pb2.DT_COMPLEX64:
#     dtype = np.complex64
#   elif type == types_pb2.DT_INT64:
#     dtype = np.int64
#   elif type == types_pb2.DT_BOOL:
#     dtype = np.bool
#   # elif type == types_pb2.DT_QINT8:
#   #   dtype = np.qint8
#   # elif type == types_pb2.DT_QUINT8:
#   #   dtype = np.quint8
#   # elif type == types_pb2.DT_QINT32:
#   #   dtype = np.qint32
#   elif type == types_pb2.DT_BFLOAT16:
#     if _np_bfloat16 is not None:
#       dtype = _np_bfloat16
#   # elif type == types_pb2.DT_QINT16:
#   #   dtype = np.qint16
#   # elif type == types_pb2.DT_QUINT16:
#   #   dtype = np.quint16
#   elif type == types_pb2.DT_UINT16:
#     dtype = np.uint16
#   elif type == types_pb2.DT_COMPLEX128:
#     dtype = np.complex128
#   elif type == types_pb2.DT_HALF:
#     dtype = np.half
#   # elif type == types_pb2.DT_RESOURCE:
#   #   return errors.Unimplemented("DT_RESOURCE can't be converted to a numpy dtype"), None
#   # elif type == types_pb2.DT_VARIANT:
#   #   return errors.Unimplemented("DT_VARAINT can't be converted to a numpy dtype"), None
#   elif type == types_pb2.DT_UINT32:
#     dtype = np.uint32
#   elif type == types_pb2.DT_UINT64:
#     dtype = np.uint64
#   if dtype is None:
#     return errors.Unimplemented("Can't convert data type ", type, " to numpy dtype"), None
#   return errors.Status.OK(), dtype
