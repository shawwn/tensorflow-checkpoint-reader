
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....tensorflow.core.protobuf import meta_graph_pb2 as tensorflow_dot_core_dot_protobuf_dot_meta__graph__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/protobuf/saved_model.proto', package='tensorflow', syntax='proto3', serialized_options=b'\n\x18org.tensorflow.frameworkB\x10SavedModelProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n*tensorflow/core/protobuf/saved_model.proto\x12\ntensorflow\x1a)tensorflow/core/protobuf/meta_graph.proto"_\n\nSavedModel\x12"\n\x1asaved_model_schema_version\x18\x01 \x01(\x03\x12-\n\x0bmeta_graphs\x18\x02 \x03(\x0b2\x18.tensorflow.MetaGraphDefB\x88\x01\n\x18org.tensorflow.frameworkB\x10SavedModelProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01b\x06proto3', dependencies=[tensorflow_dot_core_dot_protobuf_dot_meta__graph__pb2.DESCRIPTOR])
_SAVEDMODEL = _descriptor.Descriptor(name='SavedModel', full_name='tensorflow.SavedModel', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='saved_model_schema_version', full_name='tensorflow.SavedModel.saved_model_schema_version', index=0, number=1, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='meta_graphs', full_name='tensorflow.SavedModel.meta_graphs', index=1, number=2, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=101, serialized_end=196)
_SAVEDMODEL.fields_by_name['meta_graphs'].message_type = tensorflow_dot_core_dot_protobuf_dot_meta__graph__pb2._METAGRAPHDEF
DESCRIPTOR.message_types_by_name['SavedModel'] = _SAVEDMODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SavedModel = _reflection.GeneratedProtocolMessageType('SavedModel', (_message.Message,), {'DESCRIPTOR': _SAVEDMODEL, '__module__': 'tensorflow.core.protobuf.saved_model_pb2'})
_sym_db.RegisterMessage(SavedModel)
DESCRIPTOR._options = None
