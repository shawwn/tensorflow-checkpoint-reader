
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/profiler/protobuf/op_profile.proto', package='tensorflow.profiler.op_profile', syntax='proto3', serialized_options=None, create_key=_descriptor._internal_create_key, serialized_pb=b'\n2tensorflow/core/profiler/protobuf/op_profile.proto\x12\x1etensorflow.profiler.op_profile"\xd1\x02\n\x07Profile\x129\n\x0bby_category\x18\x01 \x01(\x0b2$.tensorflow.profiler.op_profile.Node\x128\n\nby_program\x18\x04 \x01(\x0b2$.tensorflow.profiler.op_profile.Node\x12\x13\n\x0bdevice_type\x18\x05 \x01(\t\x12F\n\x18by_category_exclude_idle\x18\x06 \x01(\x0b2$.tensorflow.profiler.op_profile.Node\x12E\n\x17by_program_exclude_idle\x18\x07 \x01(\x0b2$.tensorflow.profiler.op_profile.NodeJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04R\x14by_program_structureR\x0bper_program"\xb4\x05\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x128\n\x07metrics\x18\x02 \x01(\x0b2\'.tensorflow.profiler.op_profile.Metrics\x126\n\x08children\x18\x03 \x03(\x0b2$.tensorflow.profiler.op_profile.Node\x12L\n\x08category\x18\x04 \x01(\x0b28.tensorflow.profiler.op_profile.Node.InstructionCategoryH\x00\x12B\n\x03xla\x18\x05 \x01(\x0b23.tensorflow.profiler.op_profile.Node.XLAInstructionH\x00\x12\x14\n\x0cnum_children\x18\x06 \x01(\x05\x1a\x15\n\x13InstructionCategory\x1a\xe0\x02\n\x0eXLAInstruction\x12\n\n\x02op\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\x12\n\nprovenance\x18\x03 \x01(\t\x12\x10\n\x08category\x18\x04 \x01(\t\x12R\n\x06layout\x18\x05 \x01(\x0b2B.tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis\x1a\xb3\x01\n\x0eLayoutAnalysis\x12`\n\ndimensions\x18\x01 \x03(\x0b2L.tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension\x1a?\n\tDimension\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x11\n\talignment\x18\x02 \x01(\x05\x12\x11\n\tsemantics\x18\x03 \x01(\tB\n\n\x08contents"\x81\x01\n\x07Metrics\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\r\n\x05flops\x18\x02 \x01(\x01\x12\x18\n\x10memory_bandwidth\x18\x03 \x01(\x01\x12\x10\n\x08raw_time\x18\x0b \x01(\x01\x12\x11\n\traw_flops\x18\x0c \x01(\x01\x12\x1a\n\x12raw_bytes_accessed\x18\r \x01(\x01b\x06proto3')
_PROFILE = _descriptor.Descriptor(name='Profile', full_name='tensorflow.profiler.op_profile.Profile', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='by_category', full_name='tensorflow.profiler.op_profile.Profile.by_category', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='by_program', full_name='tensorflow.profiler.op_profile.Profile.by_program', index=1, number=4, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='device_type', full_name='tensorflow.profiler.op_profile.Profile.device_type', index=2, number=5, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='by_category_exclude_idle', full_name='tensorflow.profiler.op_profile.Profile.by_category_exclude_idle', index=3, number=6, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='by_program_exclude_idle', full_name='tensorflow.profiler.op_profile.Profile.by_program_exclude_idle', index=4, number=7, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=87, serialized_end=424)
_NODE_INSTRUCTIONCATEGORY = _descriptor.Descriptor(name='InstructionCategory', full_name='tensorflow.profiler.op_profile.Node.InstructionCategory', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=731, serialized_end=752)
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION = _descriptor.Descriptor(name='Dimension', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='size', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension.size', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='alignment', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension.alignment', index=1, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='semantics', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension.semantics', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1044, serialized_end=1107)
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS = _descriptor.Descriptor(name='LayoutAnalysis', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='dimensions', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.dimensions', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[_NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=928, serialized_end=1107)
_NODE_XLAINSTRUCTION = _descriptor.Descriptor(name='XLAInstruction', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='op', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.op', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='expression', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.expression', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='provenance', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.provenance', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='category', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.category', index=3, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='layout', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.layout', index=4, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[_NODE_XLAINSTRUCTION_LAYOUTANALYSIS], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=755, serialized_end=1107)
_NODE = _descriptor.Descriptor(name='Node', full_name='tensorflow.profiler.op_profile.Node', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='tensorflow.profiler.op_profile.Node.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='metrics', full_name='tensorflow.profiler.op_profile.Node.metrics', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='children', full_name='tensorflow.profiler.op_profile.Node.children', index=2, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='category', full_name='tensorflow.profiler.op_profile.Node.category', index=3, number=4, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='xla', full_name='tensorflow.profiler.op_profile.Node.xla', index=4, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='num_children', full_name='tensorflow.profiler.op_profile.Node.num_children', index=5, number=6, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[_NODE_INSTRUCTIONCATEGORY, _NODE_XLAINSTRUCTION], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='contents', full_name='tensorflow.profiler.op_profile.Node.contents', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=427, serialized_end=1119)
_METRICS = _descriptor.Descriptor(name='Metrics', full_name='tensorflow.profiler.op_profile.Metrics', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='time', full_name='tensorflow.profiler.op_profile.Metrics.time', index=0, number=1, type=1, cpp_type=5, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='flops', full_name='tensorflow.profiler.op_profile.Metrics.flops', index=1, number=2, type=1, cpp_type=5, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='memory_bandwidth', full_name='tensorflow.profiler.op_profile.Metrics.memory_bandwidth', index=2, number=3, type=1, cpp_type=5, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='raw_time', full_name='tensorflow.profiler.op_profile.Metrics.raw_time', index=3, number=11, type=1, cpp_type=5, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='raw_flops', full_name='tensorflow.profiler.op_profile.Metrics.raw_flops', index=4, number=12, type=1, cpp_type=5, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='raw_bytes_accessed', full_name='tensorflow.profiler.op_profile.Metrics.raw_bytes_accessed', index=5, number=13, type=1, cpp_type=5, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1122, serialized_end=1251)
_PROFILE.fields_by_name['by_category'].message_type = _NODE
_PROFILE.fields_by_name['by_program'].message_type = _NODE
_PROFILE.fields_by_name['by_category_exclude_idle'].message_type = _NODE
_PROFILE.fields_by_name['by_program_exclude_idle'].message_type = _NODE
_NODE_INSTRUCTIONCATEGORY.containing_type = _NODE
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION.containing_type = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS.fields_by_name['dimensions'].message_type = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS.containing_type = _NODE_XLAINSTRUCTION
_NODE_XLAINSTRUCTION.fields_by_name['layout'].message_type = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS
_NODE_XLAINSTRUCTION.containing_type = _NODE
_NODE.fields_by_name['metrics'].message_type = _METRICS
_NODE.fields_by_name['children'].message_type = _NODE
_NODE.fields_by_name['category'].message_type = _NODE_INSTRUCTIONCATEGORY
_NODE.fields_by_name['xla'].message_type = _NODE_XLAINSTRUCTION
_NODE.oneofs_by_name['contents'].fields.append(_NODE.fields_by_name['category'])
_NODE.fields_by_name['category'].containing_oneof = _NODE.oneofs_by_name['contents']
_NODE.oneofs_by_name['contents'].fields.append(_NODE.fields_by_name['xla'])
_NODE.fields_by_name['xla'].containing_oneof = _NODE.oneofs_by_name['contents']
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Metrics'] = _METRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {'DESCRIPTOR': _PROFILE, '__module__': 'tensorflow.core.profiler.protobuf.op_profile_pb2'})
_sym_db.RegisterMessage(Profile)
Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {'InstructionCategory': _reflection.GeneratedProtocolMessageType('InstructionCategory', (_message.Message,), {'DESCRIPTOR': _NODE_INSTRUCTIONCATEGORY, '__module__': 'tensorflow.core.profiler.protobuf.op_profile_pb2'}), 'XLAInstruction': _reflection.GeneratedProtocolMessageType('XLAInstruction', (_message.Message,), {'LayoutAnalysis': _reflection.GeneratedProtocolMessageType('LayoutAnalysis', (_message.Message,), {'Dimension': _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), {'DESCRIPTOR': _NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION, '__module__': 'tensorflow.core.profiler.protobuf.op_profile_pb2'}), 'DESCRIPTOR': _NODE_XLAINSTRUCTION_LAYOUTANALYSIS, '__module__': 'tensorflow.core.profiler.protobuf.op_profile_pb2'}), 'DESCRIPTOR': _NODE_XLAINSTRUCTION, '__module__': 'tensorflow.core.profiler.protobuf.op_profile_pb2'}), 'DESCRIPTOR': _NODE, '__module__': 'tensorflow.core.profiler.protobuf.op_profile_pb2'})
_sym_db.RegisterMessage(Node)
_sym_db.RegisterMessage(Node.InstructionCategory)
_sym_db.RegisterMessage(Node.XLAInstruction)
_sym_db.RegisterMessage(Node.XLAInstruction.LayoutAnalysis)
_sym_db.RegisterMessage(Node.XLAInstruction.LayoutAnalysis.Dimension)
Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), {'DESCRIPTOR': _METRICS, '__module__': 'tensorflow.core.profiler.protobuf.op_profile_pb2'})
_sym_db.RegisterMessage(Metrics)