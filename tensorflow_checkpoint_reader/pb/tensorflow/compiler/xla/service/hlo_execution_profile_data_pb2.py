
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....tensorflow.compiler.xla.service import hlo_profile_printer_data_pb2 as tensorflow_dot_compiler_dot_xla_dot_service_dot_hlo__profile__printer__data__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/compiler/xla/service/hlo_execution_profile_data.proto', package='xla', syntax='proto3', serialized_options=b'\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n@tensorflow/compiler/xla/service/hlo_execution_profile_data.proto\x12\x03xla\x1a>tensorflow/compiler/xla/service/hlo_profile_printer_data.proto"e\n\x17HloExecutionProfileData\x120\n\x0cprinter_data\x18\x01 \x01(\x0b2\x1a.xla.HloProfilePrinterData\x12\x18\n\x10profile_counters\x18\x02 \x03(\x03B\x03\xf8\x01\x01b\x06proto3', dependencies=[tensorflow_dot_compiler_dot_xla_dot_service_dot_hlo__profile__printer__data__pb2.DESCRIPTOR])
_HLOEXECUTIONPROFILEDATA = _descriptor.Descriptor(name='HloExecutionProfileData', full_name='xla.HloExecutionProfileData', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='printer_data', full_name='xla.HloExecutionProfileData.printer_data', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='profile_counters', full_name='xla.HloExecutionProfileData.profile_counters', index=1, number=2, type=3, cpp_type=2, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=137, serialized_end=238)
_HLOEXECUTIONPROFILEDATA.fields_by_name['printer_data'].message_type = tensorflow_dot_compiler_dot_xla_dot_service_dot_hlo__profile__printer__data__pb2._HLOPROFILEPRINTERDATA
DESCRIPTOR.message_types_by_name['HloExecutionProfileData'] = _HLOEXECUTIONPROFILEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
HloExecutionProfileData = _reflection.GeneratedProtocolMessageType('HloExecutionProfileData', (_message.Message,), {'DESCRIPTOR': _HLOEXECUTIONPROFILEDATA, '__module__': 'tensorflow.compiler.xla.service.hlo_execution_profile_data_pb2'})
_sym_db.RegisterMessage(HloExecutionProfileData)
DESCRIPTOR._options = None
