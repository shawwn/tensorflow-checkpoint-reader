
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/protobuf/named_tensor.proto', package='tensorflow', syntax='proto3', serialized_options=b'\n\x18org.tensorflow.frameworkB\x11NamedTensorProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n+tensorflow/core/protobuf/named_tensor.proto\x12\ntensorflow\x1a&tensorflow/core/framework/tensor.proto"I\n\x10NamedTensorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x06tensor\x18\x02 \x01(\x0b2\x17.tensorflow.TensorProtoB\x89\x01\n\x18org.tensorflow.frameworkB\x11NamedTensorProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01b\x06proto3', dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR])
_NAMEDTENSORPROTO = _descriptor.Descriptor(name='NamedTensorProto', full_name='tensorflow.NamedTensorProto', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='tensorflow.NamedTensorProto.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='tensor', full_name='tensorflow.NamedTensorProto.tensor', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=99, serialized_end=172)
_NAMEDTENSORPROTO.fields_by_name['tensor'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
DESCRIPTOR.message_types_by_name['NamedTensorProto'] = _NAMEDTENSORPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
NamedTensorProto = _reflection.GeneratedProtocolMessageType('NamedTensorProto', (_message.Message,), {'DESCRIPTOR': _NAMEDTENSORPROTO, '__module__': 'tensorflow.core.protobuf.named_tensor_pb2'})
_sym_db.RegisterMessage(NamedTensorProto)
DESCRIPTOR._options = None
