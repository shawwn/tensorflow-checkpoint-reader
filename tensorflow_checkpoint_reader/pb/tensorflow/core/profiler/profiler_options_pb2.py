
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/profiler/profiler_options.proto', package='tensorflow', syntax='proto3', serialized_options=None, create_key=_descriptor._internal_create_key, serialized_pb=b'\n/tensorflow/core/profiler/profiler_options.proto\x12\ntensorflow"\xed\x02\n\x0eProfileOptions\x12\x0f\n\x07version\x18\x05 \x01(\r\x12:\n\x0bdevice_type\x18\x06 \x01(\x0e2%.tensorflow.ProfileOptions.DeviceType\x12\x1b\n\x13include_dataset_ops\x18\x01 \x01(\x08\x12\x19\n\x11host_tracer_level\x18\x02 \x01(\r\x12\x1b\n\x13device_tracer_level\x18\x03 \x01(\r\x12\x1b\n\x13python_tracer_level\x18\x04 \x01(\r\x12\x18\n\x10enable_hlo_proto\x18\x07 \x01(\x08\x12\x1a\n\x12start_timestamp_ns\x18\x08 \x01(\x04\x12\x13\n\x0bduration_ms\x18\t \x01(\x04\x12\x17\n\x0frepository_path\x18\n \x01(\t"8\n\nDeviceType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x07\n\x03CPU\x10\x01\x12\x07\n\x03GPU\x10\x02\x12\x07\n\x03TPU\x10\x03"\xd0\x01\n#RemoteProfilerSessionManagerOptions\x124\n\x10profiler_options\x18\x01 \x01(\x0b2\x1a.tensorflow.ProfileOptions\x12\x19\n\x11service_addresses\x18\x02 \x03(\t\x12%\n\x1dsession_creation_timestamp_ns\x18\x03 \x01(\x04\x12\x1f\n\x17max_session_duration_ms\x18\x04 \x01(\x04\x12\x10\n\x08delay_ms\x18\x05 \x01(\x04b\x06proto3')
_PROFILEOPTIONS_DEVICETYPE = _descriptor.EnumDescriptor(name='DeviceType', full_name='tensorflow.ProfileOptions.DeviceType', filename=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key, values=[_descriptor.EnumValueDescriptor(name='UNSPECIFIED', index=0, number=0, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='CPU', index=1, number=1, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='GPU', index=2, number=2, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='TPU', index=3, number=3, serialized_options=None, type=None, create_key=_descriptor._internal_create_key)], containing_type=None, serialized_options=None, serialized_start=373, serialized_end=429)
_sym_db.RegisterEnumDescriptor(_PROFILEOPTIONS_DEVICETYPE)
_PROFILEOPTIONS = _descriptor.Descriptor(name='ProfileOptions', full_name='tensorflow.ProfileOptions', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='version', full_name='tensorflow.ProfileOptions.version', index=0, number=5, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='device_type', full_name='tensorflow.ProfileOptions.device_type', index=1, number=6, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='include_dataset_ops', full_name='tensorflow.ProfileOptions.include_dataset_ops', index=2, number=1, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='host_tracer_level', full_name='tensorflow.ProfileOptions.host_tracer_level', index=3, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='device_tracer_level', full_name='tensorflow.ProfileOptions.device_tracer_level', index=4, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='python_tracer_level', full_name='tensorflow.ProfileOptions.python_tracer_level', index=5, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='enable_hlo_proto', full_name='tensorflow.ProfileOptions.enable_hlo_proto', index=6, number=7, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='start_timestamp_ns', full_name='tensorflow.ProfileOptions.start_timestamp_ns', index=7, number=8, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='duration_ms', full_name='tensorflow.ProfileOptions.duration_ms', index=8, number=9, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='repository_path', full_name='tensorflow.ProfileOptions.repository_path', index=9, number=10, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[_PROFILEOPTIONS_DEVICETYPE], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=64, serialized_end=429)
_REMOTEPROFILERSESSIONMANAGEROPTIONS = _descriptor.Descriptor(name='RemoteProfilerSessionManagerOptions', full_name='tensorflow.RemoteProfilerSessionManagerOptions', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='profiler_options', full_name='tensorflow.RemoteProfilerSessionManagerOptions.profiler_options', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='service_addresses', full_name='tensorflow.RemoteProfilerSessionManagerOptions.service_addresses', index=1, number=2, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='session_creation_timestamp_ns', full_name='tensorflow.RemoteProfilerSessionManagerOptions.session_creation_timestamp_ns', index=2, number=3, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='max_session_duration_ms', full_name='tensorflow.RemoteProfilerSessionManagerOptions.max_session_duration_ms', index=3, number=4, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='delay_ms', full_name='tensorflow.RemoteProfilerSessionManagerOptions.delay_ms', index=4, number=5, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=432, serialized_end=640)
_PROFILEOPTIONS.fields_by_name['device_type'].enum_type = _PROFILEOPTIONS_DEVICETYPE
_PROFILEOPTIONS_DEVICETYPE.containing_type = _PROFILEOPTIONS
_REMOTEPROFILERSESSIONMANAGEROPTIONS.fields_by_name['profiler_options'].message_type = _PROFILEOPTIONS
DESCRIPTOR.message_types_by_name['ProfileOptions'] = _PROFILEOPTIONS
DESCRIPTOR.message_types_by_name['RemoteProfilerSessionManagerOptions'] = _REMOTEPROFILERSESSIONMANAGEROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ProfileOptions = _reflection.GeneratedProtocolMessageType('ProfileOptions', (_message.Message,), {'DESCRIPTOR': _PROFILEOPTIONS, '__module__': 'tensorflow.core.profiler.profiler_options_pb2'})
_sym_db.RegisterMessage(ProfileOptions)
RemoteProfilerSessionManagerOptions = _reflection.GeneratedProtocolMessageType('RemoteProfilerSessionManagerOptions', (_message.Message,), {'DESCRIPTOR': _REMOTEPROFILERSESSIONMANAGEROPTIONS, '__module__': 'tensorflow.core.profiler.profiler_options_pb2'})
_sym_db.RegisterMessage(RemoteProfilerSessionManagerOptions)
