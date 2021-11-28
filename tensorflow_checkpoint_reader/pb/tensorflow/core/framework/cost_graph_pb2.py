# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/cost_graph.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from . import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/cost_graph.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB\017CostGraphProtosP\001ZQgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/cost_graph_go_proto\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*tensorflow/core/framework/cost_graph.proto\x12\ntensorflow\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"\xca\x06\n\x0c\x43ostGraphDef\x12+\n\x04node\x18\x01 \x03(\x0b\x32\x1d.tensorflow.CostGraphDef.Node\x12\x35\n\x04\x63ost\x18\x02 \x03(\x0b\x32\'.tensorflow.CostGraphDef.AggregatedCost\x1a\xa2\x05\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\x12;\n\ninput_info\x18\x04 \x03(\x0b\x32\'.tensorflow.CostGraphDef.Node.InputInfo\x12=\n\x0boutput_info\x18\x05 \x03(\x0b\x32(.tensorflow.CostGraphDef.Node.OutputInfo\x12\x1d\n\x15temporary_memory_size\x18\x06 \x01(\x03\x12\x1e\n\x16persistent_memory_size\x18\x0c \x01(\x03\x12!\n\x15host_temp_memory_size\x18\n \x01(\x03\x42\x02\x18\x01\x12#\n\x17\x64\x65vice_temp_memory_size\x18\x0b \x01(\x03\x42\x02\x18\x01\x12)\n\x1d\x64\x65vice_persistent_memory_size\x18\x10 \x01(\x03\x42\x02\x18\x01\x12\x14\n\x0c\x63ompute_cost\x18\t \x01(\x03\x12\x14\n\x0c\x63ompute_time\x18\x0e \x01(\x03\x12\x13\n\x0bmemory_time\x18\x0f \x01(\x03\x12\x10\n\x08is_final\x18\x07 \x01(\x08\x12\x15\n\rcontrol_input\x18\x08 \x03(\x05\x12\x12\n\ninaccurate\x18\x11 \x01(\x08\x1a;\n\tInputInfo\x12\x16\n\x0epreceding_node\x18\x01 \x01(\x05\x12\x16\n\x0epreceding_port\x18\x02 \x01(\x05\x1a\x86\x01\n\nOutputInfo\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x18\n\x10\x61lias_input_port\x18\x02 \x01(\x03\x12+\n\x05shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12#\n\x05\x64type\x18\x04 \x01(\x0e\x32\x14.tensorflow.DataType\x1a\x31\n\x0e\x41ggregatedCost\x12\x0c\n\x04\x63ost\x18\x01 \x01(\x02\x12\x11\n\tdimension\x18\x02 \x01(\tB\x83\x01\n\x18org.tensorflow.frameworkB\x0f\x43ostGraphProtosP\x01ZQgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/cost_graph_go_proto\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_COSTGRAPHDEF_NODE_INPUTINFO = _descriptor.Descriptor(
  name='InputInfo',
  full_name='tensorflow.CostGraphDef.Node.InputInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='preceding_node', full_name='tensorflow.CostGraphDef.Node.InputInfo.preceding_node', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preceding_port', full_name='tensorflow.CostGraphDef.Node.InputInfo.preceding_port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=739,
  serialized_end=798,
)

_COSTGRAPHDEF_NODE_OUTPUTINFO = _descriptor.Descriptor(
  name='OutputInfo',
  full_name='tensorflow.CostGraphDef.Node.OutputInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='tensorflow.CostGraphDef.Node.OutputInfo.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alias_input_port', full_name='tensorflow.CostGraphDef.Node.OutputInfo.alias_input_port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.CostGraphDef.Node.OutputInfo.shape', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.CostGraphDef.Node.OutputInfo.dtype', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=935,
)

_COSTGRAPHDEF_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='tensorflow.CostGraphDef.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.CostGraphDef.Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='tensorflow.CostGraphDef.Node.device', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.CostGraphDef.Node.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_info', full_name='tensorflow.CostGraphDef.Node.input_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_info', full_name='tensorflow.CostGraphDef.Node.output_info', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temporary_memory_size', full_name='tensorflow.CostGraphDef.Node.temporary_memory_size', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='persistent_memory_size', full_name='tensorflow.CostGraphDef.Node.persistent_memory_size', index=6,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_temp_memory_size', full_name='tensorflow.CostGraphDef.Node.host_temp_memory_size', index=7,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_temp_memory_size', full_name='tensorflow.CostGraphDef.Node.device_temp_memory_size', index=8,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_persistent_memory_size', full_name='tensorflow.CostGraphDef.Node.device_persistent_memory_size', index=9,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_cost', full_name='tensorflow.CostGraphDef.Node.compute_cost', index=10,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_time', full_name='tensorflow.CostGraphDef.Node.compute_time', index=11,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory_time', full_name='tensorflow.CostGraphDef.Node.memory_time', index=12,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_final', full_name='tensorflow.CostGraphDef.Node.is_final', index=13,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='control_input', full_name='tensorflow.CostGraphDef.Node.control_input', index=14,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inaccurate', full_name='tensorflow.CostGraphDef.Node.inaccurate', index=15,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COSTGRAPHDEF_NODE_INPUTINFO, _COSTGRAPHDEF_NODE_OUTPUTINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=935,
)

_COSTGRAPHDEF_AGGREGATEDCOST = _descriptor.Descriptor(
  name='AggregatedCost',
  full_name='tensorflow.CostGraphDef.AggregatedCost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost', full_name='tensorflow.CostGraphDef.AggregatedCost.cost', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dimension', full_name='tensorflow.CostGraphDef.AggregatedCost.dimension', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=937,
  serialized_end=986,
)

_COSTGRAPHDEF = _descriptor.Descriptor(
  name='CostGraphDef',
  full_name='tensorflow.CostGraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='tensorflow.CostGraphDef.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost', full_name='tensorflow.CostGraphDef.cost', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COSTGRAPHDEF_NODE, _COSTGRAPHDEF_AGGREGATEDCOST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=986,
)

_COSTGRAPHDEF_NODE_INPUTINFO.containing_type = _COSTGRAPHDEF_NODE
_COSTGRAPHDEF_NODE_OUTPUTINFO.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_COSTGRAPHDEF_NODE_OUTPUTINFO.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_COSTGRAPHDEF_NODE_OUTPUTINFO.containing_type = _COSTGRAPHDEF_NODE
_COSTGRAPHDEF_NODE.fields_by_name['input_info'].message_type = _COSTGRAPHDEF_NODE_INPUTINFO
_COSTGRAPHDEF_NODE.fields_by_name['output_info'].message_type = _COSTGRAPHDEF_NODE_OUTPUTINFO
_COSTGRAPHDEF_NODE.containing_type = _COSTGRAPHDEF
_COSTGRAPHDEF_AGGREGATEDCOST.containing_type = _COSTGRAPHDEF
_COSTGRAPHDEF.fields_by_name['node'].message_type = _COSTGRAPHDEF_NODE
_COSTGRAPHDEF.fields_by_name['cost'].message_type = _COSTGRAPHDEF_AGGREGATEDCOST
DESCRIPTOR.message_types_by_name['CostGraphDef'] = _COSTGRAPHDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CostGraphDef = _reflection.GeneratedProtocolMessageType('CostGraphDef', (_message.Message,), {

  'Node' : _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {

    'InputInfo' : _reflection.GeneratedProtocolMessageType('InputInfo', (_message.Message,), {
      'DESCRIPTOR' : _COSTGRAPHDEF_NODE_INPUTINFO,
      '__module__' : 'tensorflow.core.framework.cost_graph_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef.Node.InputInfo)
      })
    ,

    'OutputInfo' : _reflection.GeneratedProtocolMessageType('OutputInfo', (_message.Message,), {
      'DESCRIPTOR' : _COSTGRAPHDEF_NODE_OUTPUTINFO,
      '__module__' : 'tensorflow.core.framework.cost_graph_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef.Node.OutputInfo)
      })
    ,
    'DESCRIPTOR' : _COSTGRAPHDEF_NODE,
    '__module__' : 'tensorflow.core.framework.cost_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef.Node)
    })
  ,

  'AggregatedCost' : _reflection.GeneratedProtocolMessageType('AggregatedCost', (_message.Message,), {
    'DESCRIPTOR' : _COSTGRAPHDEF_AGGREGATEDCOST,
    '__module__' : 'tensorflow.core.framework.cost_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef.AggregatedCost)
    })
  ,
  'DESCRIPTOR' : _COSTGRAPHDEF,
  '__module__' : 'tensorflow.core.framework.cost_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef)
  })
_sym_db.RegisterMessage(CostGraphDef)
_sym_db.RegisterMessage(CostGraphDef.Node)
_sym_db.RegisterMessage(CostGraphDef.Node.InputInfo)
_sym_db.RegisterMessage(CostGraphDef.Node.OutputInfo)
_sym_db.RegisterMessage(CostGraphDef.AggregatedCost)


DESCRIPTOR._options = None
_COSTGRAPHDEF_NODE.fields_by_name['host_temp_memory_size']._options = None
_COSTGRAPHDEF_NODE.fields_by_name['device_temp_memory_size']._options = None
_COSTGRAPHDEF_NODE.fields_by_name['device_persistent_memory_size']._options = None
# @@protoc_insertion_point(module_scope)
