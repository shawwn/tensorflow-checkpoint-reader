
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/lite/toco/types.proto', package='toco', syntax='proto2', serialized_options=None, create_key=_descriptor._internal_create_key, serialized_pb=b'\n tensorflow/lite/toco/types.proto\x12\x04toco*\xa7\x02\n\nIODataType\x12\x18\n\x14IO_DATA_TYPE_UNKNOWN\x10\x00\x12\t\n\x05FLOAT\x10\x01\x12\x13\n\x0fQUANTIZED_UINT8\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\n\n\x06STRING\x10\x05\x12\x13\n\x0fQUANTIZED_INT16\x10\x06\x12\x08\n\x04BOOL\x10\x07\x12\r\n\tCOMPLEX64\x10\x08\x12\x12\n\x0eQUANTIZED_INT8\x10\t\x12\x0b\n\x07FLOAT16\x10\n\x12\x0b\n\x07FLOAT64\x10\x0b\x12\x0e\n\nCOMPLEX128\x10\x0c\x12\n\n\x06UINT64\x10\r\x12\x0c\n\x08RESOURCE\x10\x0e\x12\x0b\n\x07VARIANT\x10\x0f\x12\n\n\x06UINT32\x10\x10\x12\t\n\x05UINT8\x10\x11\x12\x08\n\x04INT8\x10\x12\x12\t\n\x05INT16\x10\x13')
_IODATATYPE = _descriptor.EnumDescriptor(name='IODataType', full_name='toco.IODataType', filename=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key, values=[_descriptor.EnumValueDescriptor(name='IO_DATA_TYPE_UNKNOWN', index=0, number=0, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='FLOAT', index=1, number=1, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='QUANTIZED_UINT8', index=2, number=2, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='INT32', index=3, number=3, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='INT64', index=4, number=4, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='STRING', index=5, number=5, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='QUANTIZED_INT16', index=6, number=6, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='BOOL', index=7, number=7, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='COMPLEX64', index=8, number=8, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='QUANTIZED_INT8', index=9, number=9, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='FLOAT16', index=10, number=10, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='FLOAT64', index=11, number=11, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='COMPLEX128', index=12, number=12, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='UINT64', index=13, number=13, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='RESOURCE', index=14, number=14, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='VARIANT', index=15, number=15, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='UINT32', index=16, number=16, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='UINT8', index=17, number=17, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='INT8', index=18, number=18, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='INT16', index=19, number=19, serialized_options=None, type=None, create_key=_descriptor._internal_create_key)], containing_type=None, serialized_options=None, serialized_start=43, serialized_end=338)
_sym_db.RegisterEnumDescriptor(_IODATATYPE)
IODataType = enum_type_wrapper.EnumTypeWrapper(_IODATATYPE)
IO_DATA_TYPE_UNKNOWN = 0
FLOAT = 1
QUANTIZED_UINT8 = 2
INT32 = 3
INT64 = 4
STRING = 5
QUANTIZED_INT16 = 6
BOOL = 7
COMPLEX64 = 8
QUANTIZED_INT8 = 9
FLOAT16 = 10
FLOAT64 = 11
COMPLEX128 = 12
UINT64 = 13
RESOURCE = 14
VARIANT = 15
UINT32 = 16
UINT8 = 17
INT8 = 18
INT16 = 19
DESCRIPTOR.enum_types_by_name['IODataType'] = _IODATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
