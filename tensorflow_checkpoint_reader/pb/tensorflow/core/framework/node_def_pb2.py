# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/node_def.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import attr_value_pb2 as tensorflow_dot_core_dot_framework_dot_attr__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/node_def.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB\tNodeProtoP\001ZOgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/node_def_go_proto\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(tensorflow/core/framework/node_def.proto\x12\ntensorflow\x1a*tensorflow/core/framework/attr_value.proto\"\xd2\x02\n\x07NodeDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12\r\n\x05input\x18\x03 \x03(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12+\n\x04\x61ttr\x18\x05 \x03(\x0b\x32\x1d.tensorflow.NodeDef.AttrEntry\x12J\n\x17\x65xperimental_debug_info\x18\x06 \x01(\x0b\x32).tensorflow.NodeDef.ExperimentalDebugInfo\x1a\x42\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.tensorflow.AttrValue:\x02\x38\x01\x1aQ\n\x15\x45xperimentalDebugInfo\x12\x1b\n\x13original_node_names\x18\x01 \x03(\t\x12\x1b\n\x13original_func_names\x18\x02 \x03(\tB{\n\x18org.tensorflow.frameworkB\tNodeProtoP\x01ZOgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/node_def_go_proto\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_attr__value__pb2.DESCRIPTOR,])




_NODEDEF_ATTRENTRY = _descriptor.Descriptor(
  name='AttrEntry',
  full_name='tensorflow.NodeDef.AttrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.NodeDef.AttrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.NodeDef.AttrEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=356,
)

_NODEDEF_EXPERIMENTALDEBUGINFO = _descriptor.Descriptor(
  name='ExperimentalDebugInfo',
  full_name='tensorflow.NodeDef.ExperimentalDebugInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_node_names', full_name='tensorflow.NodeDef.ExperimentalDebugInfo.original_node_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_func_names', full_name='tensorflow.NodeDef.ExperimentalDebugInfo.original_func_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=358,
  serialized_end=439,
)

_NODEDEF = _descriptor.Descriptor(
  name='NodeDef',
  full_name='tensorflow.NodeDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.NodeDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='op', full_name='tensorflow.NodeDef.op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input', full_name='tensorflow.NodeDef.input', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='tensorflow.NodeDef.device', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attr', full_name='tensorflow.NodeDef.attr', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experimental_debug_info', full_name='tensorflow.NodeDef.experimental_debug_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NODEDEF_ATTRENTRY, _NODEDEF_EXPERIMENTALDEBUGINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=439,
)

_NODEDEF_ATTRENTRY.fields_by_name['value'].message_type = tensorflow_dot_core_dot_framework_dot_attr__value__pb2._ATTRVALUE
_NODEDEF_ATTRENTRY.containing_type = _NODEDEF
_NODEDEF_EXPERIMENTALDEBUGINFO.containing_type = _NODEDEF
_NODEDEF.fields_by_name['attr'].message_type = _NODEDEF_ATTRENTRY
_NODEDEF.fields_by_name['experimental_debug_info'].message_type = _NODEDEF_EXPERIMENTALDEBUGINFO
DESCRIPTOR.message_types_by_name['NodeDef'] = _NODEDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeDef = _reflection.GeneratedProtocolMessageType('NodeDef', (_message.Message,), {

  'AttrEntry' : _reflection.GeneratedProtocolMessageType('AttrEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODEDEF_ATTRENTRY,
    '__module__' : 'tensorflow.core.framework.node_def_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.NodeDef.AttrEntry)
    })
  ,

  'ExperimentalDebugInfo' : _reflection.GeneratedProtocolMessageType('ExperimentalDebugInfo', (_message.Message,), {
    'DESCRIPTOR' : _NODEDEF_EXPERIMENTALDEBUGINFO,
    '__module__' : 'tensorflow.core.framework.node_def_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.NodeDef.ExperimentalDebugInfo)
    })
  ,
  'DESCRIPTOR' : _NODEDEF,
  '__module__' : 'tensorflow.core.framework.node_def_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.NodeDef)
  })
_sym_db.RegisterMessage(NodeDef)
_sym_db.RegisterMessage(NodeDef.AttrEntry)
_sym_db.RegisterMessage(NodeDef.ExperimentalDebugInfo)


DESCRIPTOR._options = None
_NODEDEF_ATTRENTRY._options = None
# @@protoc_insertion_point(module_scope)
