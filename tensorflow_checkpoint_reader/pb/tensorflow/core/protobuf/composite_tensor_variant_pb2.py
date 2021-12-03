
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....tensorflow.core.protobuf import struct_pb2 as tensorflow_dot_core_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/protobuf/composite_tensor_variant.proto', package='tensorflow', syntax='proto3', serialized_options=b'ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto', create_key=_descriptor._internal_create_key, serialized_pb=b'\n7tensorflow/core/protobuf/composite_tensor_variant.proto\x12\ntensorflow\x1a%tensorflow/core/protobuf/struct.proto"T\n\x1eCompositeTensorVariantMetadata\x122\n\x0ftype_spec_proto\x18\x01 \x01(\x0b2\x19.tensorflow.TypeSpecProtoBWZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_protob\x06proto3', dependencies=[tensorflow_dot_core_dot_protobuf_dot_struct__pb2.DESCRIPTOR])
_COMPOSITETENSORVARIANTMETADATA = _descriptor.Descriptor(name='CompositeTensorVariantMetadata', full_name='tensorflow.CompositeTensorVariantMetadata', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='type_spec_proto', full_name='tensorflow.CompositeTensorVariantMetadata.type_spec_proto', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=110, serialized_end=194)
_COMPOSITETENSORVARIANTMETADATA.fields_by_name['type_spec_proto'].message_type = tensorflow_dot_core_dot_protobuf_dot_struct__pb2._TYPESPECPROTO
DESCRIPTOR.message_types_by_name['CompositeTensorVariantMetadata'] = _COMPOSITETENSORVARIANTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CompositeTensorVariantMetadata = _reflection.GeneratedProtocolMessageType('CompositeTensorVariantMetadata', (_message.Message,), {'DESCRIPTOR': _COMPOSITETENSORVARIANTMETADATA, '__module__': 'tensorflow.core.protobuf.composite_tensor_variant_pb2'})
_sym_db.RegisterMessage(CompositeTensorVariantMetadata)
DESCRIPTOR._options = None
