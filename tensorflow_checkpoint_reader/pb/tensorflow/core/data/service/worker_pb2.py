
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....tensorflow.core.data import dataset_pb2 as tensorflow_dot_core_dot_data_dot_dataset__pb2
from .....tensorflow.core.data.service import common_pb2 as tensorflow_dot_core_dot_data_dot_service_dot_common__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/data/service/worker.proto', package='tensorflow.data', syntax='proto3', serialized_options=None, create_key=_descriptor._internal_create_key, serialized_pb=b'\n)tensorflow/core/data/service/worker.proto\x12\x0ftensorflow.data\x1a"tensorflow/core/data/dataset.proto\x1a)tensorflow/core/data/service/common.proto"<\n\x12ProcessTaskRequest\x12&\n\x04task\x18\x01 \x01(\x0b2\x18.tensorflow.data.TaskDef"\x15\n\x13ProcessTaskResponse"\xbc\x01\n\x11GetElementRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x18\n\x0econsumer_index\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bround_index\x18\x03 \x01(\x03H\x01\x12\x1e\n\x16skipped_previous_round\x18\x04 \x01(\x08\x12\x12\n\nallow_skip\x18\x05 \x01(\x08B\x19\n\x17optional_consumer_indexB\x16\n\x14optional_round_index"\xda\x01\n\x12GetElementResponse\x128\n\ncompressed\x18\x03 \x01(\x0b2".tensorflow.data.CompressedElementH\x00\x12<\n\x0cuncompressed\x18\x05 \x01(\x0b2$.tensorflow.data.UncompressedElementH\x00\x12\x15\n\relement_index\x18\x06 \x01(\x03\x12\x17\n\x0fend_of_sequence\x18\x02 \x01(\x08\x12\x11\n\tskip_task\x18\x04 \x01(\x08B\t\n\x07element"\x17\n\x15GetWorkerTasksRequest"B\n\x16GetWorkerTasksResponse\x12(\n\x05tasks\x18\x01 \x03(\x0b2\x19.tensorflow.data.TaskInfo2\xa3\x02\n\rWorkerService\x12X\n\x0bProcessTask\x12#.tensorflow.data.ProcessTaskRequest\x1a$.tensorflow.data.ProcessTaskResponse\x12U\n\nGetElement\x12".tensorflow.data.GetElementRequest\x1a#.tensorflow.data.GetElementResponse\x12a\n\x0eGetWorkerTasks\x12&.tensorflow.data.GetWorkerTasksRequest\x1a\'.tensorflow.data.GetWorkerTasksResponseb\x06proto3', dependencies=[tensorflow_dot_core_dot_data_dot_dataset__pb2.DESCRIPTOR, tensorflow_dot_core_dot_data_dot_service_dot_common__pb2.DESCRIPTOR])
_PROCESSTASKREQUEST = _descriptor.Descriptor(name='ProcessTaskRequest', full_name='tensorflow.data.ProcessTaskRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='task', full_name='tensorflow.data.ProcessTaskRequest.task', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=141, serialized_end=201)
_PROCESSTASKRESPONSE = _descriptor.Descriptor(name='ProcessTaskResponse', full_name='tensorflow.data.ProcessTaskResponse', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=203, serialized_end=224)
_GETELEMENTREQUEST = _descriptor.Descriptor(name='GetElementRequest', full_name='tensorflow.data.GetElementRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='task_id', full_name='tensorflow.data.GetElementRequest.task_id', index=0, number=1, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='consumer_index', full_name='tensorflow.data.GetElementRequest.consumer_index', index=1, number=2, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='round_index', full_name='tensorflow.data.GetElementRequest.round_index', index=2, number=3, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='skipped_previous_round', full_name='tensorflow.data.GetElementRequest.skipped_previous_round', index=3, number=4, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='allow_skip', full_name='tensorflow.data.GetElementRequest.allow_skip', index=4, number=5, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='optional_consumer_index', full_name='tensorflow.data.GetElementRequest.optional_consumer_index', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[]), _descriptor.OneofDescriptor(name='optional_round_index', full_name='tensorflow.data.GetElementRequest.optional_round_index', index=1, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=227, serialized_end=415)
_GETELEMENTRESPONSE = _descriptor.Descriptor(name='GetElementResponse', full_name='tensorflow.data.GetElementResponse', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='compressed', full_name='tensorflow.data.GetElementResponse.compressed', index=0, number=3, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='uncompressed', full_name='tensorflow.data.GetElementResponse.uncompressed', index=1, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='element_index', full_name='tensorflow.data.GetElementResponse.element_index', index=2, number=6, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='end_of_sequence', full_name='tensorflow.data.GetElementResponse.end_of_sequence', index=3, number=2, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='skip_task', full_name='tensorflow.data.GetElementResponse.skip_task', index=4, number=4, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='element', full_name='tensorflow.data.GetElementResponse.element', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=418, serialized_end=636)
_GETWORKERTASKSREQUEST = _descriptor.Descriptor(name='GetWorkerTasksRequest', full_name='tensorflow.data.GetWorkerTasksRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=638, serialized_end=661)
_GETWORKERTASKSRESPONSE = _descriptor.Descriptor(name='GetWorkerTasksResponse', full_name='tensorflow.data.GetWorkerTasksResponse', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='tasks', full_name='tensorflow.data.GetWorkerTasksResponse.tasks', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=663, serialized_end=729)
_PROCESSTASKREQUEST.fields_by_name['task'].message_type = tensorflow_dot_core_dot_data_dot_service_dot_common__pb2._TASKDEF
_GETELEMENTREQUEST.oneofs_by_name['optional_consumer_index'].fields.append(_GETELEMENTREQUEST.fields_by_name['consumer_index'])
_GETELEMENTREQUEST.fields_by_name['consumer_index'].containing_oneof = _GETELEMENTREQUEST.oneofs_by_name['optional_consumer_index']
_GETELEMENTREQUEST.oneofs_by_name['optional_round_index'].fields.append(_GETELEMENTREQUEST.fields_by_name['round_index'])
_GETELEMENTREQUEST.fields_by_name['round_index'].containing_oneof = _GETELEMENTREQUEST.oneofs_by_name['optional_round_index']
_GETELEMENTRESPONSE.fields_by_name['compressed'].message_type = tensorflow_dot_core_dot_data_dot_dataset__pb2._COMPRESSEDELEMENT
_GETELEMENTRESPONSE.fields_by_name['uncompressed'].message_type = tensorflow_dot_core_dot_data_dot_dataset__pb2._UNCOMPRESSEDELEMENT
_GETELEMENTRESPONSE.oneofs_by_name['element'].fields.append(_GETELEMENTRESPONSE.fields_by_name['compressed'])
_GETELEMENTRESPONSE.fields_by_name['compressed'].containing_oneof = _GETELEMENTRESPONSE.oneofs_by_name['element']
_GETELEMENTRESPONSE.oneofs_by_name['element'].fields.append(_GETELEMENTRESPONSE.fields_by_name['uncompressed'])
_GETELEMENTRESPONSE.fields_by_name['uncompressed'].containing_oneof = _GETELEMENTRESPONSE.oneofs_by_name['element']
_GETWORKERTASKSRESPONSE.fields_by_name['tasks'].message_type = tensorflow_dot_core_dot_data_dot_service_dot_common__pb2._TASKINFO
DESCRIPTOR.message_types_by_name['ProcessTaskRequest'] = _PROCESSTASKREQUEST
DESCRIPTOR.message_types_by_name['ProcessTaskResponse'] = _PROCESSTASKRESPONSE
DESCRIPTOR.message_types_by_name['GetElementRequest'] = _GETELEMENTREQUEST
DESCRIPTOR.message_types_by_name['GetElementResponse'] = _GETELEMENTRESPONSE
DESCRIPTOR.message_types_by_name['GetWorkerTasksRequest'] = _GETWORKERTASKSREQUEST
DESCRIPTOR.message_types_by_name['GetWorkerTasksResponse'] = _GETWORKERTASKSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ProcessTaskRequest = _reflection.GeneratedProtocolMessageType('ProcessTaskRequest', (_message.Message,), {'DESCRIPTOR': _PROCESSTASKREQUEST, '__module__': 'tensorflow.core.data.service.worker_pb2'})
_sym_db.RegisterMessage(ProcessTaskRequest)
ProcessTaskResponse = _reflection.GeneratedProtocolMessageType('ProcessTaskResponse', (_message.Message,), {'DESCRIPTOR': _PROCESSTASKRESPONSE, '__module__': 'tensorflow.core.data.service.worker_pb2'})
_sym_db.RegisterMessage(ProcessTaskResponse)
GetElementRequest = _reflection.GeneratedProtocolMessageType('GetElementRequest', (_message.Message,), {'DESCRIPTOR': _GETELEMENTREQUEST, '__module__': 'tensorflow.core.data.service.worker_pb2'})
_sym_db.RegisterMessage(GetElementRequest)
GetElementResponse = _reflection.GeneratedProtocolMessageType('GetElementResponse', (_message.Message,), {'DESCRIPTOR': _GETELEMENTRESPONSE, '__module__': 'tensorflow.core.data.service.worker_pb2'})
_sym_db.RegisterMessage(GetElementResponse)
GetWorkerTasksRequest = _reflection.GeneratedProtocolMessageType('GetWorkerTasksRequest', (_message.Message,), {'DESCRIPTOR': _GETWORKERTASKSREQUEST, '__module__': 'tensorflow.core.data.service.worker_pb2'})
_sym_db.RegisterMessage(GetWorkerTasksRequest)
GetWorkerTasksResponse = _reflection.GeneratedProtocolMessageType('GetWorkerTasksResponse', (_message.Message,), {'DESCRIPTOR': _GETWORKERTASKSRESPONSE, '__module__': 'tensorflow.core.data.service.worker_pb2'})
_sym_db.RegisterMessage(GetWorkerTasksResponse)
_WORKERSERVICE = _descriptor.ServiceDescriptor(name='WorkerService', full_name='tensorflow.data.WorkerService', file=DESCRIPTOR, index=0, serialized_options=None, create_key=_descriptor._internal_create_key, serialized_start=732, serialized_end=1023, methods=[_descriptor.MethodDescriptor(name='ProcessTask', full_name='tensorflow.data.WorkerService.ProcessTask', index=0, containing_service=None, input_type=_PROCESSTASKREQUEST, output_type=_PROCESSTASKRESPONSE, serialized_options=None, create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='GetElement', full_name='tensorflow.data.WorkerService.GetElement', index=1, containing_service=None, input_type=_GETELEMENTREQUEST, output_type=_GETELEMENTRESPONSE, serialized_options=None, create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='GetWorkerTasks', full_name='tensorflow.data.WorkerService.GetWorkerTasks', index=2, containing_service=None, input_type=_GETWORKERTASKSREQUEST, output_type=_GETWORKERTASKSRESPONSE, serialized_options=None, create_key=_descriptor._internal_create_key)])
_sym_db.RegisterServiceDescriptor(_WORKERSERVICE)
DESCRIPTOR.services_by_name['WorkerService'] = _WORKERSERVICE