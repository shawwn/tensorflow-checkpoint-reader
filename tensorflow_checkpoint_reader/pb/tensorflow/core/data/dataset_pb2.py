
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from ....tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from ....tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/data/dataset.proto', package='tensorflow.data', syntax='proto3', serialized_options=None, create_key=_descriptor._internal_create_key, serialized_pb=b'\n"tensorflow/core/data/dataset.proto\x12\x0ftensorflow.data\x1a&tensorflow/core/framework/tensor.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto"\x91\x01\n\x1bCompressedComponentMetadata\x12#\n\x05dtype\x18\x01 \x01(\x0e2\x14.tensorflow.DataType\x122\n\x0ctensor_shape\x18\x02 \x01(\x0b2\x1c.tensorflow.TensorShapeProto\x12\x19\n\x11tensor_size_bytes\x18\x03 \x01(\x03"k\n\x11CompressedElement\x12\x0c\n\x04data\x18\x01 \x01(\x0c\x12H\n\x12component_metadata\x18\x02 \x03(\x0b2,.tensorflow.data.CompressedComponentMetadata"B\n\x13UncompressedElement\x12+\n\ncomponents\x18\x01 \x03(\x0b2\x17.tensorflow.TensorProtob\x06proto3', dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR, tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR, tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR])
_COMPRESSEDCOMPONENTMETADATA = _descriptor.Descriptor(name='CompressedComponentMetadata', full_name='tensorflow.data.CompressedComponentMetadata', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='dtype', full_name='tensorflow.data.CompressedComponentMetadata.dtype', index=0, number=1, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='tensor_shape', full_name='tensorflow.data.CompressedComponentMetadata.tensor_shape', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='tensor_size_bytes', full_name='tensorflow.data.CompressedComponentMetadata.tensor_size_bytes', index=2, number=3, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=181, serialized_end=326)
_COMPRESSEDELEMENT = _descriptor.Descriptor(name='CompressedElement', full_name='tensorflow.data.CompressedElement', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='data', full_name='tensorflow.data.CompressedElement.data', index=0, number=1, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b'', message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='component_metadata', full_name='tensorflow.data.CompressedElement.component_metadata', index=1, number=2, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=328, serialized_end=435)
_UNCOMPRESSEDELEMENT = _descriptor.Descriptor(name='UncompressedElement', full_name='tensorflow.data.UncompressedElement', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='components', full_name='tensorflow.data.UncompressedElement.components', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=437, serialized_end=503)
_COMPRESSEDCOMPONENTMETADATA.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_COMPRESSEDCOMPONENTMETADATA.fields_by_name['tensor_shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_COMPRESSEDELEMENT.fields_by_name['component_metadata'].message_type = _COMPRESSEDCOMPONENTMETADATA
_UNCOMPRESSEDELEMENT.fields_by_name['components'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
DESCRIPTOR.message_types_by_name['CompressedComponentMetadata'] = _COMPRESSEDCOMPONENTMETADATA
DESCRIPTOR.message_types_by_name['CompressedElement'] = _COMPRESSEDELEMENT
DESCRIPTOR.message_types_by_name['UncompressedElement'] = _UNCOMPRESSEDELEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CompressedComponentMetadata = _reflection.GeneratedProtocolMessageType('CompressedComponentMetadata', (_message.Message,), {'DESCRIPTOR': _COMPRESSEDCOMPONENTMETADATA, '__module__': 'tensorflow.core.data.dataset_pb2'})
_sym_db.RegisterMessage(CompressedComponentMetadata)
CompressedElement = _reflection.GeneratedProtocolMessageType('CompressedElement', (_message.Message,), {'DESCRIPTOR': _COMPRESSEDELEMENT, '__module__': 'tensorflow.core.data.dataset_pb2'})
_sym_db.RegisterMessage(CompressedElement)
UncompressedElement = _reflection.GeneratedProtocolMessageType('UncompressedElement', (_message.Message,), {'DESCRIPTOR': _UNCOMPRESSEDELEMENT, '__module__': 'tensorflow.core.data.dataset_pb2'})
_sym_db.RegisterMessage(UncompressedElement)