# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/stream_executor/dnn.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/stream_executor/dnn.proto',
  package='stream_executor.dnn',
  syntax='proto3',
  serialized_options=b'Z>github.com/tensorflow/tensorflow/tensorflow/go/stream_executor',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$tensorflow/stream_executor/dnn.proto\x12\x13stream_executor.dnn\"\xe1\x01\n\x15TensorDescriptorProto\x12\x12\n\ndimensions\x18\x01 \x03(\x03\x12\x30\n\tdata_type\x18\x02 \x01(\x0e\x32\x1d.stream_executor.dnn.DataType\x12\x36\n\x0b\x64\x61ta_layout\x18\x03 \x01(\x0e\x32\x1f.stream_executor.dnn.DataLayoutH\x00\x12:\n\rfilter_layout\x18\x04 \x01(\x0e\x32!.stream_executor.dnn.FilterLayoutH\x00\x42\x0e\n\x0clayout_oneof\"\xaa\x01\n\x0e\x41lgorithmProto\x12\x0f\n\x07\x61lgo_id\x18\x01 \x01(\x03\x12?\n\tmath_type\x18\x02 \x01(\x0e\x32,.stream_executor.dnn.AlgorithmProto.MathType\x12\x14\n\x0c\x65xec_plan_id\x18\x03 \x01(\t\"0\n\x08MathType\x12\x10\n\x0c\x44\x45\x46\x41ULT_MATH\x10\x00\x12\x12\n\x0eTENSOR_OP_MATH\x10\x01\"\xea\x01\n\x1a\x43onvolutionDescriptorProto\x12\x10\n\x08paddings\x18\x01 \x03(\x03\x12\x0f\n\x07strides\x18\x02 \x03(\x03\x12\x11\n\tdilations\x18\x03 \x03(\x03\x12\x33\n\x0c\x63ompute_mode\x18\x04 \x01(\x0e\x32\x1d.stream_executor.dnn.DataType\x12\x13\n\x0bgroup_count\x18\x05 \x01(\x05\x12>\n\x10\x63onvolution_mode\x18\x06 \x01(\x0e\x32$.stream_executor.dnn.ConvolutionMode\x12\x0c\n\x04name\x18\x07 \x01(\t*w\n\x08\x44\x61taType\x12\n\n\x06kFloat\x10\x00\x12\x0b\n\x07kDouble\x10\x01\x12\t\n\x05kHalf\x10\x02\x12\t\n\x05kInt8\x10\x03\x12\n\n\x06kInt32\x10\x04\x12\x11\n\rkComplexFloat\x10\x05\x12\x12\n\x0ekComplexDouble\x10\x06\x12\t\n\x05kBF16\x10\x07*\x81\x01\n\nDataLayout\x12\x11\n\rkYXDepthBatch\x10\x00\x12\x11\n\rkYXBatchDepth\x10\x01\x12\x11\n\rkBatchYXDepth\x10\x02\x12\x11\n\rkBatchDepthYX\x10\x03\x12\x12\n\x0ekBatchDepthYX4\x10\x04\x12\x13\n\x0fkBatchDepthYX32\x10\x05*\x89\x01\n\x0c\x46ilterLayout\x12\x12\n\x0ekOutputInputYX\x10\x00\x12\x12\n\x0ekOutputYXInput\x10\x01\x12\x13\n\x0fkOutputInputYX4\x10\x02\x12\x14\n\x10kOutputInputYX32\x10\x05\x12\x12\n\x0ekInputYXOutput\x10\x03\x12\x12\n\x0ekYXInputOutput\x10\x04*f\n\x0e\x41\x63tivationMode\x12\t\n\x05kNone\x10\x00\x12\x0c\n\x08kSigmoid\x10\x01\x12\t\n\x05kRelu\x10\x02\x12\n\n\x06kRelu6\x10\x03\x12\n\n\x06kReluX\x10\x04\x12\t\n\x05kTanh\x10\x05\x12\r\n\tkBandPass\x10\x06*9\n\x0f\x43onvolutionMode\x12\x15\n\x11\x43ROSS_CORRELATION\x10\x00\x12\x0f\n\x0b\x43ONVOLUTION\x10\x01*p\n\x0f\x43onvolutionKind\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07\x46ORWARD\x10\x01\x12\x13\n\x0f\x42\x41\x43KWARD_FILTER\x10\x02\x12\x11\n\rBACKWARD_DATA\x10\x03\x12\x1b\n\x17\x46ORWARD_BIAS_ACTIVATION\x10\x04\x42@Z>github.com/tensorflow/tensorflow/tensorflow/go/stream_executorb\x06proto3'
)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='stream_executor.dnn.DataType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kFloat', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kDouble', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kHalf', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kInt8', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kInt32', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kComplexFloat', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kComplexDouble', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kBF16', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=699,
  serialized_end=818,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_DATALAYOUT = _descriptor.EnumDescriptor(
  name='DataLayout',
  full_name='stream_executor.dnn.DataLayout',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kYXDepthBatch', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kYXBatchDepth', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kBatchYXDepth', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kBatchDepthYX', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kBatchDepthYX4', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kBatchDepthYX32', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=821,
  serialized_end=950,
)
_sym_db.RegisterEnumDescriptor(_DATALAYOUT)

DataLayout = enum_type_wrapper.EnumTypeWrapper(_DATALAYOUT)
_FILTERLAYOUT = _descriptor.EnumDescriptor(
  name='FilterLayout',
  full_name='stream_executor.dnn.FilterLayout',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kOutputInputYX', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kOutputYXInput', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kOutputInputYX4', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kOutputInputYX32', index=3, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kInputYXOutput', index=4, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kYXInputOutput', index=5, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=953,
  serialized_end=1090,
)
_sym_db.RegisterEnumDescriptor(_FILTERLAYOUT)

FilterLayout = enum_type_wrapper.EnumTypeWrapper(_FILTERLAYOUT)
_ACTIVATIONMODE = _descriptor.EnumDescriptor(
  name='ActivationMode',
  full_name='stream_executor.dnn.ActivationMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kNone', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kSigmoid', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kRelu', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kRelu6', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kReluX', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kTanh', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='kBandPass', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1092,
  serialized_end=1194,
)
_sym_db.RegisterEnumDescriptor(_ACTIVATIONMODE)

ActivationMode = enum_type_wrapper.EnumTypeWrapper(_ACTIVATIONMODE)
_CONVOLUTIONMODE = _descriptor.EnumDescriptor(
  name='ConvolutionMode',
  full_name='stream_executor.dnn.ConvolutionMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CROSS_CORRELATION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVOLUTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1196,
  serialized_end=1253,
)
_sym_db.RegisterEnumDescriptor(_CONVOLUTIONMODE)

ConvolutionMode = enum_type_wrapper.EnumTypeWrapper(_CONVOLUTIONMODE)
_CONVOLUTIONKIND = _descriptor.EnumDescriptor(
  name='ConvolutionKind',
  full_name='stream_executor.dnn.ConvolutionKind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORWARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BACKWARD_FILTER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BACKWARD_DATA', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORWARD_BIAS_ACTIVATION', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1255,
  serialized_end=1367,
)
_sym_db.RegisterEnumDescriptor(_CONVOLUTIONKIND)

ConvolutionKind = enum_type_wrapper.EnumTypeWrapper(_CONVOLUTIONKIND)
kFloat = 0
kDouble = 1
kHalf = 2
kInt8 = 3
kInt32 = 4
kComplexFloat = 5
kComplexDouble = 6
kBF16 = 7
kYXDepthBatch = 0
kYXBatchDepth = 1
kBatchYXDepth = 2
kBatchDepthYX = 3
kBatchDepthYX4 = 4
kBatchDepthYX32 = 5
kOutputInputYX = 0
kOutputYXInput = 1
kOutputInputYX4 = 2
kOutputInputYX32 = 5
kInputYXOutput = 3
kYXInputOutput = 4
kNone = 0
kSigmoid = 1
kRelu = 2
kRelu6 = 3
kReluX = 4
kTanh = 5
kBandPass = 6
CROSS_CORRELATION = 0
CONVOLUTION = 1
INVALID = 0
FORWARD = 1
BACKWARD_FILTER = 2
BACKWARD_DATA = 3
FORWARD_BIAS_ACTIVATION = 4


_ALGORITHMPROTO_MATHTYPE = _descriptor.EnumDescriptor(
  name='MathType',
  full_name='stream_executor.dnn.AlgorithmProto.MathType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_MATH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TENSOR_OP_MATH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=412,
  serialized_end=460,
)
_sym_db.RegisterEnumDescriptor(_ALGORITHMPROTO_MATHTYPE)


_TENSORDESCRIPTORPROTO = _descriptor.Descriptor(
  name='TensorDescriptorProto',
  full_name='stream_executor.dnn.TensorDescriptorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='stream_executor.dnn.TensorDescriptorProto.dimensions', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='stream_executor.dnn.TensorDescriptorProto.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_layout', full_name='stream_executor.dnn.TensorDescriptorProto.data_layout', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_layout', full_name='stream_executor.dnn.TensorDescriptorProto.filter_layout', index=3,
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
    _descriptor.OneofDescriptor(
      name='layout_oneof', full_name='stream_executor.dnn.TensorDescriptorProto.layout_oneof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=62,
  serialized_end=287,
)


_ALGORITHMPROTO = _descriptor.Descriptor(
  name='AlgorithmProto',
  full_name='stream_executor.dnn.AlgorithmProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='algo_id', full_name='stream_executor.dnn.AlgorithmProto.algo_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='math_type', full_name='stream_executor.dnn.AlgorithmProto.math_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exec_plan_id', full_name='stream_executor.dnn.AlgorithmProto.exec_plan_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ALGORITHMPROTO_MATHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=460,
)


_CONVOLUTIONDESCRIPTORPROTO = _descriptor.Descriptor(
  name='ConvolutionDescriptorProto',
  full_name='stream_executor.dnn.ConvolutionDescriptorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='paddings', full_name='stream_executor.dnn.ConvolutionDescriptorProto.paddings', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strides', full_name='stream_executor.dnn.ConvolutionDescriptorProto.strides', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dilations', full_name='stream_executor.dnn.ConvolutionDescriptorProto.dilations', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_mode', full_name='stream_executor.dnn.ConvolutionDescriptorProto.compute_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_count', full_name='stream_executor.dnn.ConvolutionDescriptorProto.group_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='convolution_mode', full_name='stream_executor.dnn.ConvolutionDescriptorProto.convolution_mode', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='stream_executor.dnn.ConvolutionDescriptorProto.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=463,
  serialized_end=697,
)

_TENSORDESCRIPTORPROTO.fields_by_name['data_type'].enum_type = _DATATYPE
_TENSORDESCRIPTORPROTO.fields_by_name['data_layout'].enum_type = _DATALAYOUT
_TENSORDESCRIPTORPROTO.fields_by_name['filter_layout'].enum_type = _FILTERLAYOUT
_TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof'].fields.append(
  _TENSORDESCRIPTORPROTO.fields_by_name['data_layout'])
_TENSORDESCRIPTORPROTO.fields_by_name['data_layout'].containing_oneof = _TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof']
_TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof'].fields.append(
  _TENSORDESCRIPTORPROTO.fields_by_name['filter_layout'])
_TENSORDESCRIPTORPROTO.fields_by_name['filter_layout'].containing_oneof = _TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof']
_ALGORITHMPROTO.fields_by_name['math_type'].enum_type = _ALGORITHMPROTO_MATHTYPE
_ALGORITHMPROTO_MATHTYPE.containing_type = _ALGORITHMPROTO
_CONVOLUTIONDESCRIPTORPROTO.fields_by_name['compute_mode'].enum_type = _DATATYPE
_CONVOLUTIONDESCRIPTORPROTO.fields_by_name['convolution_mode'].enum_type = _CONVOLUTIONMODE
DESCRIPTOR.message_types_by_name['TensorDescriptorProto'] = _TENSORDESCRIPTORPROTO
DESCRIPTOR.message_types_by_name['AlgorithmProto'] = _ALGORITHMPROTO
DESCRIPTOR.message_types_by_name['ConvolutionDescriptorProto'] = _CONVOLUTIONDESCRIPTORPROTO
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
DESCRIPTOR.enum_types_by_name['DataLayout'] = _DATALAYOUT
DESCRIPTOR.enum_types_by_name['FilterLayout'] = _FILTERLAYOUT
DESCRIPTOR.enum_types_by_name['ActivationMode'] = _ACTIVATIONMODE
DESCRIPTOR.enum_types_by_name['ConvolutionMode'] = _CONVOLUTIONMODE
DESCRIPTOR.enum_types_by_name['ConvolutionKind'] = _CONVOLUTIONKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorDescriptorProto = _reflection.GeneratedProtocolMessageType('TensorDescriptorProto', (_message.Message,), {
  'DESCRIPTOR' : _TENSORDESCRIPTORPROTO,
  '__module__' : 'tensorflow.stream_executor.dnn_pb2'
  # @@protoc_insertion_point(class_scope:stream_executor.dnn.TensorDescriptorProto)
  })
_sym_db.RegisterMessage(TensorDescriptorProto)

AlgorithmProto = _reflection.GeneratedProtocolMessageType('AlgorithmProto', (_message.Message,), {
  'DESCRIPTOR' : _ALGORITHMPROTO,
  '__module__' : 'tensorflow.stream_executor.dnn_pb2'
  # @@protoc_insertion_point(class_scope:stream_executor.dnn.AlgorithmProto)
  })
_sym_db.RegisterMessage(AlgorithmProto)

ConvolutionDescriptorProto = _reflection.GeneratedProtocolMessageType('ConvolutionDescriptorProto', (_message.Message,), {
  'DESCRIPTOR' : _CONVOLUTIONDESCRIPTORPROTO,
  '__module__' : 'tensorflow.stream_executor.dnn_pb2'
  # @@protoc_insertion_point(class_scope:stream_executor.dnn.ConvolutionDescriptorProto)
  })
_sym_db.RegisterMessage(ConvolutionDescriptorProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
