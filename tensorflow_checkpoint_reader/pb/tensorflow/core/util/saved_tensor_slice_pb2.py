
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from ....tensorflow.core.framework import tensor_slice_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__slice__pb2
from ....tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from ....tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2
from ....tensorflow.core.framework import versions_pb2 as tensorflow_dot_core_dot_framework_dot_versions__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/util/saved_tensor_slice.proto', package='tensorflow', syntax='proto3', serialized_options=b'\n\x13org.tensorflow.utilB\x16SavedTensorSliceProtosP\x01\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n-tensorflow/core/util/saved_tensor_slice.proto\x12\ntensorflow\x1a,tensorflow/core/framework/tensor_shape.proto\x1a,tensorflow/core/framework/tensor_slice.proto\x1a&tensorflow/core/framework/tensor.proto\x1a%tensorflow/core/framework/types.proto\x1a(tensorflow/core/framework/versions.proto"\x9c\x01\n\x0eSavedSliceMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x05shape\x18\x02 \x01(\x0b2\x1c.tensorflow.TensorShapeProto\x12"\n\x04type\x18\x03 \x01(\x0e2\x14.tensorflow.DataType\x12+\n\x05slice\x18\x04 \x03(\x0b2\x1c.tensorflow.TensorSliceProto"l\n\x14SavedTensorSliceMeta\x12*\n\x06tensor\x18\x01 \x03(\x0b2\x1a.tensorflow.SavedSliceMeta\x12(\n\x08versions\x18\x02 \x01(\x0b2\x16.tensorflow.VersionDef"n\n\nSavedSlice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x05slice\x18\x02 \x01(\x0b2\x1c.tensorflow.TensorSliceProto\x12%\n\x04data\x18\x03 \x01(\x0b2\x17.tensorflow.TensorProto"i\n\x11SavedTensorSlices\x12.\n\x04meta\x18\x01 \x01(\x0b2 .tensorflow.SavedTensorSliceMeta\x12$\n\x04data\x18\x02 \x01(\x0b2\x16.tensorflow.SavedSliceB2\n\x13org.tensorflow.utilB\x16SavedTensorSliceProtosP\x01\xf8\x01\x01b\x06proto3', dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR, tensorflow_dot_core_dot_framework_dot_tensor__slice__pb2.DESCRIPTOR, tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR, tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR, tensorflow_dot_core_dot_framework_dot_versions__pb2.DESCRIPTOR])
_SAVEDSLICEMETA = _descriptor.Descriptor(name='SavedSliceMeta', full_name='tensorflow.SavedSliceMeta', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='tensorflow.SavedSliceMeta.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='shape', full_name='tensorflow.SavedSliceMeta.shape', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='type', full_name='tensorflow.SavedSliceMeta.type', index=2, number=3, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='slice', full_name='tensorflow.SavedSliceMeta.slice', index=3, number=4, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=275, serialized_end=431)
_SAVEDTENSORSLICEMETA = _descriptor.Descriptor(name='SavedTensorSliceMeta', full_name='tensorflow.SavedTensorSliceMeta', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='tensor', full_name='tensorflow.SavedTensorSliceMeta.tensor', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='versions', full_name='tensorflow.SavedTensorSliceMeta.versions', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=433, serialized_end=541)
_SAVEDSLICE = _descriptor.Descriptor(name='SavedSlice', full_name='tensorflow.SavedSlice', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='tensorflow.SavedSlice.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='slice', full_name='tensorflow.SavedSlice.slice', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='data', full_name='tensorflow.SavedSlice.data', index=2, number=3, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=543, serialized_end=653)
_SAVEDTENSORSLICES = _descriptor.Descriptor(name='SavedTensorSlices', full_name='tensorflow.SavedTensorSlices', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='meta', full_name='tensorflow.SavedTensorSlices.meta', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='data', full_name='tensorflow.SavedTensorSlices.data', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=655, serialized_end=760)
_SAVEDSLICEMETA.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_SAVEDSLICEMETA.fields_by_name['type'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_SAVEDSLICEMETA.fields_by_name['slice'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__slice__pb2._TENSORSLICEPROTO
_SAVEDTENSORSLICEMETA.fields_by_name['tensor'].message_type = _SAVEDSLICEMETA
_SAVEDTENSORSLICEMETA.fields_by_name['versions'].message_type = tensorflow_dot_core_dot_framework_dot_versions__pb2._VERSIONDEF
_SAVEDSLICE.fields_by_name['slice'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__slice__pb2._TENSORSLICEPROTO
_SAVEDSLICE.fields_by_name['data'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_SAVEDTENSORSLICES.fields_by_name['meta'].message_type = _SAVEDTENSORSLICEMETA
_SAVEDTENSORSLICES.fields_by_name['data'].message_type = _SAVEDSLICE
DESCRIPTOR.message_types_by_name['SavedSliceMeta'] = _SAVEDSLICEMETA
DESCRIPTOR.message_types_by_name['SavedTensorSliceMeta'] = _SAVEDTENSORSLICEMETA
DESCRIPTOR.message_types_by_name['SavedSlice'] = _SAVEDSLICE
DESCRIPTOR.message_types_by_name['SavedTensorSlices'] = _SAVEDTENSORSLICES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SavedSliceMeta = _reflection.GeneratedProtocolMessageType('SavedSliceMeta', (_message.Message,), {'DESCRIPTOR': _SAVEDSLICEMETA, '__module__': 'tensorflow.core.util.saved_tensor_slice_pb2'})
_sym_db.RegisterMessage(SavedSliceMeta)
SavedTensorSliceMeta = _reflection.GeneratedProtocolMessageType('SavedTensorSliceMeta', (_message.Message,), {'DESCRIPTOR': _SAVEDTENSORSLICEMETA, '__module__': 'tensorflow.core.util.saved_tensor_slice_pb2'})
_sym_db.RegisterMessage(SavedTensorSliceMeta)
SavedSlice = _reflection.GeneratedProtocolMessageType('SavedSlice', (_message.Message,), {'DESCRIPTOR': _SAVEDSLICE, '__module__': 'tensorflow.core.util.saved_tensor_slice_pb2'})
_sym_db.RegisterMessage(SavedSlice)
SavedTensorSlices = _reflection.GeneratedProtocolMessageType('SavedTensorSlices', (_message.Message,), {'DESCRIPTOR': _SAVEDTENSORSLICES, '__module__': 'tensorflow.core.util.saved_tensor_slice_pb2'})
_sym_db.RegisterMessage(SavedTensorSlices)
DESCRIPTOR._options = None
