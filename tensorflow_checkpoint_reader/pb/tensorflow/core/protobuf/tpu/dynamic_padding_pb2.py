
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/protobuf/tpu/dynamic_padding.proto', package='tensorflow.tpu', syntax='proto3', serialized_options=b'\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n2tensorflow/core/protobuf/tpu/dynamic_padding.proto\x12\x0etensorflow.tpu"O\n\nPaddingMap\x12\x11\n\targ_index\x18\x01 \x01(\x05\x12\x13\n\x0bshape_index\x18\x02 \x01(\x05\x12\x19\n\x11padding_arg_index\x18\x03 \x01(\x05B\x03\xf8\x01\x01b\x06proto3')
_PADDINGMAP = _descriptor.Descriptor(name='PaddingMap', full_name='tensorflow.tpu.PaddingMap', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='arg_index', full_name='tensorflow.tpu.PaddingMap.arg_index', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='shape_index', full_name='tensorflow.tpu.PaddingMap.shape_index', index=1, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='padding_arg_index', full_name='tensorflow.tpu.PaddingMap.padding_arg_index', index=2, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=70, serialized_end=149)
DESCRIPTOR.message_types_by_name['PaddingMap'] = _PADDINGMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PaddingMap = _reflection.GeneratedProtocolMessageType('PaddingMap', (_message.Message,), {'DESCRIPTOR': _PADDINGMAP, '__module__': 'tensorflow.core.protobuf.tpu.dynamic_padding_pb2'})
_sym_db.RegisterMessage(PaddingMap)
DESCRIPTOR._options = None
