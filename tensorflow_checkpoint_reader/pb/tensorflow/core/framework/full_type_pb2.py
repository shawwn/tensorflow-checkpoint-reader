
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/framework/full_type.proto', package='tensorflow', syntax='proto3', serialized_options=b'\n\x18org.tensorflow.frameworkB\x0eFullTypeProtosP\x01ZPgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/full_type_go_proto\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n)tensorflow/core/framework/full_type.proto\x12\ntensorflow"r\n\x0bFullTypeDef\x12\'\n\x07type_id\x18\x01 \x01(\x0e2\x16.tensorflow.FullTypeId\x12%\n\x04args\x18\x02 \x03(\x0b2\x17.tensorflow.FullTypeDef\x12\x0b\n\x01s\x18\x03 \x01(\tH\x00B\x06\n\x04attr*\xac\x03\n\nFullTypeId\x12\r\n\tTFT_UNSET\x10\x00\x12\x0b\n\x07TFT_VAR\x10\x01\x12\x0b\n\x07TFT_ANY\x10\x02\x12\x0f\n\x0bTFT_PRODUCT\x10\x03\x12\x10\n\x0cTFT_CALLABLE\x10d\x12\x0f\n\nTFT_TENSOR\x10\xe8\x07\x12\x0e\n\tTFT_ARRAY\x10\xe9\x07\x12\x11\n\x0cTFT_OPTIONAL\x10\xea\x07\x12\x10\n\x0bTFT_DATASET\x10\xf6N\x12\r\n\x08TFT_BOOL\x10\xc8\x01\x12\x0e\n\tTFT_UINT8\x10\xc9\x01\x12\x0f\n\nTFT_UINT16\x10\xca\x01\x12\x0f\n\nTFT_UINT32\x10\xcb\x01\x12\x0f\n\nTFT_UINT64\x10\xcc\x01\x12\r\n\x08TFT_INT8\x10\xcd\x01\x12\x0e\n\tTFT_INT16\x10\xce\x01\x12\x0e\n\tTFT_INT32\x10\xcf\x01\x12\x0e\n\tTFT_INT64\x10\xd0\x01\x12\r\n\x08TFT_HALF\x10\xd1\x01\x12\x0e\n\tTFT_FLOAT\x10\xd2\x01\x12\x0f\n\nTFT_DOUBLE\x10\xd3\x01\x12\x11\n\x0cTFT_BFLOAT16\x10\xd7\x01\x12\x12\n\rTFT_COMPLEX64\x10\xd4\x01\x12\x13\n\x0eTFT_COMPLEX128\x10\xd5\x01\x12\x0f\n\nTFT_STRING\x10\xd6\x01B\x81\x01\n\x18org.tensorflow.frameworkB\x0eFullTypeProtosP\x01ZPgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/full_type_go_proto\xf8\x01\x01b\x06proto3')
_FULLTYPEID = _descriptor.EnumDescriptor(name='FullTypeId', full_name='tensorflow.FullTypeId', filename=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key, values=[_descriptor.EnumValueDescriptor(name='TFT_UNSET', index=0, number=0, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_VAR', index=1, number=1, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_ANY', index=2, number=2, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_PRODUCT', index=3, number=3, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_CALLABLE', index=4, number=100, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_TENSOR', index=5, number=1000, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_ARRAY', index=6, number=1001, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_OPTIONAL', index=7, number=1002, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_DATASET', index=8, number=10102, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_BOOL', index=9, number=200, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_UINT8', index=10, number=201, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_UINT16', index=11, number=202, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_UINT32', index=12, number=203, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_UINT64', index=13, number=204, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_INT8', index=14, number=205, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_INT16', index=15, number=206, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_INT32', index=16, number=207, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_INT64', index=17, number=208, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_HALF', index=18, number=209, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_FLOAT', index=19, number=210, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_DOUBLE', index=20, number=211, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_BFLOAT16', index=21, number=215, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_COMPLEX64', index=22, number=212, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_COMPLEX128', index=23, number=213, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TFT_STRING', index=24, number=214, serialized_options=None, type=None, create_key=_descriptor._internal_create_key)], containing_type=None, serialized_options=None, serialized_start=174, serialized_end=602)
_sym_db.RegisterEnumDescriptor(_FULLTYPEID)
FullTypeId = enum_type_wrapper.EnumTypeWrapper(_FULLTYPEID)
TFT_UNSET = 0
TFT_VAR = 1
TFT_ANY = 2
TFT_PRODUCT = 3
TFT_CALLABLE = 100
TFT_TENSOR = 1000
TFT_ARRAY = 1001
TFT_OPTIONAL = 1002
TFT_DATASET = 10102
TFT_BOOL = 200
TFT_UINT8 = 201
TFT_UINT16 = 202
TFT_UINT32 = 203
TFT_UINT64 = 204
TFT_INT8 = 205
TFT_INT16 = 206
TFT_INT32 = 207
TFT_INT64 = 208
TFT_HALF = 209
TFT_FLOAT = 210
TFT_DOUBLE = 211
TFT_BFLOAT16 = 215
TFT_COMPLEX64 = 212
TFT_COMPLEX128 = 213
TFT_STRING = 214
_FULLTYPEDEF = _descriptor.Descriptor(name='FullTypeDef', full_name='tensorflow.FullTypeDef', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='type_id', full_name='tensorflow.FullTypeDef.type_id', index=0, number=1, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='args', full_name='tensorflow.FullTypeDef.args', index=1, number=2, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='s', full_name='tensorflow.FullTypeDef.s', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='attr', full_name='tensorflow.FullTypeDef.attr', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=57, serialized_end=171)
_FULLTYPEDEF.fields_by_name['type_id'].enum_type = _FULLTYPEID
_FULLTYPEDEF.fields_by_name['args'].message_type = _FULLTYPEDEF
_FULLTYPEDEF.oneofs_by_name['attr'].fields.append(_FULLTYPEDEF.fields_by_name['s'])
_FULLTYPEDEF.fields_by_name['s'].containing_oneof = _FULLTYPEDEF.oneofs_by_name['attr']
DESCRIPTOR.message_types_by_name['FullTypeDef'] = _FULLTYPEDEF
DESCRIPTOR.enum_types_by_name['FullTypeId'] = _FULLTYPEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
FullTypeDef = _reflection.GeneratedProtocolMessageType('FullTypeDef', (_message.Message,), {'DESCRIPTOR': _FULLTYPEDEF, '__module__': 'tensorflow.core.framework.full_type_pb2'})
_sym_db.RegisterMessage(FullTypeDef)
DESCRIPTOR._options = None
