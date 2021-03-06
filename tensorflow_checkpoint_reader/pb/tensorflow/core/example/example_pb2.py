
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....tensorflow.core.example import feature_pb2 as tensorflow_dot_core_dot_example_dot_feature__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/example/example.proto', package='tensorflow', syntax='proto3', serialized_options=b'\n\x16org.tensorflow.exampleB\rExampleProtosP\x01ZSgithub.com/tensorflow/tensorflow/tensorflow/go/core/example/example_protos_go_proto\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n%tensorflow/core/example/example.proto\x12\ntensorflow\x1a%tensorflow/core/example/feature.proto"1\n\x07Example\x12&\n\x08features\x18\x01 \x01(\x0b2\x14.tensorflow.Features"i\n\x0fSequenceExample\x12%\n\x07context\x18\x01 \x01(\x0b2\x14.tensorflow.Features\x12/\n\rfeature_lists\x18\x02 \x01(\x0b2\x18.tensorflow.FeatureListsB\x81\x01\n\x16org.tensorflow.exampleB\rExampleProtosP\x01ZSgithub.com/tensorflow/tensorflow/tensorflow/go/core/example/example_protos_go_proto\xf8\x01\x01b\x06proto3', dependencies=[tensorflow_dot_core_dot_example_dot_feature__pb2.DESCRIPTOR])
_EXAMPLE = _descriptor.Descriptor(name='Example', full_name='tensorflow.Example', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='features', full_name='tensorflow.Example.features', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=92, serialized_end=141)
_SEQUENCEEXAMPLE = _descriptor.Descriptor(name='SequenceExample', full_name='tensorflow.SequenceExample', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='context', full_name='tensorflow.SequenceExample.context', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='feature_lists', full_name='tensorflow.SequenceExample.feature_lists', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=143, serialized_end=248)
_EXAMPLE.fields_by_name['features'].message_type = tensorflow_dot_core_dot_example_dot_feature__pb2._FEATURES
_SEQUENCEEXAMPLE.fields_by_name['context'].message_type = tensorflow_dot_core_dot_example_dot_feature__pb2._FEATURES
_SEQUENCEEXAMPLE.fields_by_name['feature_lists'].message_type = tensorflow_dot_core_dot_example_dot_feature__pb2._FEATURELISTS
DESCRIPTOR.message_types_by_name['Example'] = _EXAMPLE
DESCRIPTOR.message_types_by_name['SequenceExample'] = _SEQUENCEEXAMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Example = _reflection.GeneratedProtocolMessageType('Example', (_message.Message,), {'DESCRIPTOR': _EXAMPLE, '__module__': 'tensorflow.core.example.example_pb2'})
_sym_db.RegisterMessage(Example)
SequenceExample = _reflection.GeneratedProtocolMessageType('SequenceExample', (_message.Message,), {'DESCRIPTOR': _SEQUENCEEXAMPLE, '__module__': 'tensorflow.core.example.example_pb2'})
_sym_db.RegisterMessage(SequenceExample)
DESCRIPTOR._options = None
