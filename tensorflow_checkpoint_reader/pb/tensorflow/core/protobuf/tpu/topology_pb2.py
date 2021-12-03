
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/protobuf/tpu/topology.proto', package='tensorflow.tpu', syntax='proto3', serialized_options=b'\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n+tensorflow/core/protobuf/tpu/topology.proto\x12\x0etensorflow.tpu"t\n\rTopologyProto\x12\x12\n\nmesh_shape\x18\x01 \x03(\x05\x12\x11\n\tnum_tasks\x18\x02 \x01(\x05\x12 \n\x18num_tpu_devices_per_task\x18\x03 \x01(\x05\x12\x1a\n\x12device_coordinates\x18\x04 \x03(\x05B\x03\xf8\x01\x01b\x06proto3')
_TOPOLOGYPROTO = _descriptor.Descriptor(name='TopologyProto', full_name='tensorflow.tpu.TopologyProto', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='mesh_shape', full_name='tensorflow.tpu.TopologyProto.mesh_shape', index=0, number=1, type=5, cpp_type=1, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='num_tasks', full_name='tensorflow.tpu.TopologyProto.num_tasks', index=1, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='num_tpu_devices_per_task', full_name='tensorflow.tpu.TopologyProto.num_tpu_devices_per_task', index=2, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='device_coordinates', full_name='tensorflow.tpu.TopologyProto.device_coordinates', index=3, number=4, type=5, cpp_type=1, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=63, serialized_end=179)
DESCRIPTOR.message_types_by_name['TopologyProto'] = _TOPOLOGYPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
TopologyProto = _reflection.GeneratedProtocolMessageType('TopologyProto', (_message.Message,), {'DESCRIPTOR': _TOPOLOGYPROTO, '__module__': 'tensorflow.core.protobuf.tpu.topology_pb2'})
_sym_db.RegisterMessage(TopologyProto)
DESCRIPTOR._options = None
