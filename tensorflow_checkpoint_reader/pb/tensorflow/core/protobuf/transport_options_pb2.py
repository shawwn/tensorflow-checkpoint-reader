
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/protobuf/transport_options.proto', package='tensorflow', syntax='proto3', serialized_options=b'ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto', create_key=_descriptor._internal_create_key, serialized_pb=b'\n0tensorflow/core/protobuf/transport_options.proto\x12\ntensorflow"*\n\x10RecvBufRespExtra\x12\x16\n\x0etensor_content\x18\x01 \x03(\x0cBWZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_protob\x06proto3')
_RECVBUFRESPEXTRA = _descriptor.Descriptor(name='RecvBufRespExtra', full_name='tensorflow.RecvBufRespExtra', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='tensor_content', full_name='tensorflow.RecvBufRespExtra.tensor_content', index=0, number=1, type=12, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=64, serialized_end=106)
DESCRIPTOR.message_types_by_name['RecvBufRespExtra'] = _RECVBUFRESPEXTRA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
RecvBufRespExtra = _reflection.GeneratedProtocolMessageType('RecvBufRespExtra', (_message.Message,), {'DESCRIPTOR': _RECVBUFRESPEXTRA, '__module__': 'tensorflow.core.protobuf.transport_options_pb2'})
_sym_db.RegisterMessage(RecvBufRespExtra)
DESCRIPTOR._options = None
