
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/profiler/protobuf/diagnostics.proto', package='tensorflow.profiler', syntax='proto3', serialized_options=None, create_key=_descriptor._internal_create_key, serialized_pb=b'\n3tensorflow/core/profiler/protobuf/diagnostics.proto\x12\x13tensorflow.profiler"=\n\x0bDiagnostics\x12\x0c\n\x04info\x18\x01 \x03(\t\x12\x10\n\x08warnings\x18\x02 \x03(\t\x12\x0e\n\x06errors\x18\x03 \x03(\tb\x06proto3')
_DIAGNOSTICS = _descriptor.Descriptor(name='Diagnostics', full_name='tensorflow.profiler.Diagnostics', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='info', full_name='tensorflow.profiler.Diagnostics.info', index=0, number=1, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='warnings', full_name='tensorflow.profiler.Diagnostics.warnings', index=1, number=2, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='errors', full_name='tensorflow.profiler.Diagnostics.errors', index=2, number=3, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=76, serialized_end=137)
DESCRIPTOR.message_types_by_name['Diagnostics'] = _DIAGNOSTICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Diagnostics = _reflection.GeneratedProtocolMessageType('Diagnostics', (_message.Message,), {'DESCRIPTOR': _DIAGNOSTICS, '__module__': 'tensorflow.core.profiler.protobuf.diagnostics_pb2'})
_sym_db.RegisterMessage(Diagnostics)
