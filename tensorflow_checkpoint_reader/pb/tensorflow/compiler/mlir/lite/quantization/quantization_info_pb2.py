
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/compiler/mlir/lite/quantization/quantization_info.proto', package='mlir.quant', syntax='proto3', serialized_options=b'\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\nBtensorflow/compiler/mlir/lite/quantization/quantization_info.proto\x12\nmlir.quant"\xd2\x04\n\x10QuantizationInfo\x129\n\x07entries\x18\x01 \x03(\x0b2(.mlir.quant.QuantizationInfo.QuantParams\x1a"\n\x06MinMax\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\x1a1\n\x0cAffineParams\x12\r\n\x05scale\x18\x01 \x01(\x02\x12\x12\n\nzero_point\x18\x02 \x01(\x05\x1a\x9b\x01\n\rPerAxisParams\x126\n\x07min_max\x18\x01 \x01(\x0b2#.mlir.quant.QuantizationInfo.MinMaxH\x00\x12B\n\raffine_params\x18\x02 \x01(\x0b2).mlir.quant.QuantizationInfo.AffineParamsH\x00B\x0e\n\x0cparams_oneof\x1aY\n\x08Metadata\x12\x10\n\x08num_bits\x18\x01 \x01(\x05\x12\x15\n\rquantize_axis\x18\x02 \x01(\x05\x12\x11\n\trange_min\x18\x03 \x01(\x05\x12\x11\n\trange_max\x18\x04 \x01(\x05\x1a\xb2\x01\n\x0bQuantParams\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x14\n\nname_regex\x18\x02 \x01(\tH\x00\x12:\n\x06params\x18\x03 \x03(\x0b2*.mlir.quant.QuantizationInfo.PerAxisParams\x123\n\x04meta\x18\x05 \x01(\x0b2%.mlir.quant.QuantizationInfo.MetadataB\x0c\n\nname_oneofB\x03\xf8\x01\x01b\x06proto3')
_QUANTIZATIONINFO_MINMAX = _descriptor.Descriptor(name='MinMax', full_name='mlir.quant.QuantizationInfo.MinMax', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='min', full_name='mlir.quant.QuantizationInfo.MinMax.min', index=0, number=1, type=2, cpp_type=6, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='max', full_name='mlir.quant.QuantizationInfo.MinMax.max', index=1, number=2, type=2, cpp_type=6, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=162, serialized_end=196)
_QUANTIZATIONINFO_AFFINEPARAMS = _descriptor.Descriptor(name='AffineParams', full_name='mlir.quant.QuantizationInfo.AffineParams', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='scale', full_name='mlir.quant.QuantizationInfo.AffineParams.scale', index=0, number=1, type=2, cpp_type=6, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='zero_point', full_name='mlir.quant.QuantizationInfo.AffineParams.zero_point', index=1, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=198, serialized_end=247)
_QUANTIZATIONINFO_PERAXISPARAMS = _descriptor.Descriptor(name='PerAxisParams', full_name='mlir.quant.QuantizationInfo.PerAxisParams', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='min_max', full_name='mlir.quant.QuantizationInfo.PerAxisParams.min_max', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='affine_params', full_name='mlir.quant.QuantizationInfo.PerAxisParams.affine_params', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='params_oneof', full_name='mlir.quant.QuantizationInfo.PerAxisParams.params_oneof', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=250, serialized_end=405)
_QUANTIZATIONINFO_METADATA = _descriptor.Descriptor(name='Metadata', full_name='mlir.quant.QuantizationInfo.Metadata', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='num_bits', full_name='mlir.quant.QuantizationInfo.Metadata.num_bits', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='quantize_axis', full_name='mlir.quant.QuantizationInfo.Metadata.quantize_axis', index=1, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='range_min', full_name='mlir.quant.QuantizationInfo.Metadata.range_min', index=2, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='range_max', full_name='mlir.quant.QuantizationInfo.Metadata.range_max', index=3, number=4, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=407, serialized_end=496)
_QUANTIZATIONINFO_QUANTPARAMS = _descriptor.Descriptor(name='QuantParams', full_name='mlir.quant.QuantizationInfo.QuantParams', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='mlir.quant.QuantizationInfo.QuantParams.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='name_regex', full_name='mlir.quant.QuantizationInfo.QuantParams.name_regex', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='params', full_name='mlir.quant.QuantizationInfo.QuantParams.params', index=2, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='meta', full_name='mlir.quant.QuantizationInfo.QuantParams.meta', index=3, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='name_oneof', full_name='mlir.quant.QuantizationInfo.QuantParams.name_oneof', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=499, serialized_end=677)
_QUANTIZATIONINFO = _descriptor.Descriptor(name='QuantizationInfo', full_name='mlir.quant.QuantizationInfo', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='entries', full_name='mlir.quant.QuantizationInfo.entries', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[_QUANTIZATIONINFO_MINMAX, _QUANTIZATIONINFO_AFFINEPARAMS, _QUANTIZATIONINFO_PERAXISPARAMS, _QUANTIZATIONINFO_METADATA, _QUANTIZATIONINFO_QUANTPARAMS], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=83, serialized_end=677)
_QUANTIZATIONINFO_MINMAX.containing_type = _QUANTIZATIONINFO
_QUANTIZATIONINFO_AFFINEPARAMS.containing_type = _QUANTIZATIONINFO
_QUANTIZATIONINFO_PERAXISPARAMS.fields_by_name['min_max'].message_type = _QUANTIZATIONINFO_MINMAX
_QUANTIZATIONINFO_PERAXISPARAMS.fields_by_name['affine_params'].message_type = _QUANTIZATIONINFO_AFFINEPARAMS
_QUANTIZATIONINFO_PERAXISPARAMS.containing_type = _QUANTIZATIONINFO
_QUANTIZATIONINFO_PERAXISPARAMS.oneofs_by_name['params_oneof'].fields.append(_QUANTIZATIONINFO_PERAXISPARAMS.fields_by_name['min_max'])
_QUANTIZATIONINFO_PERAXISPARAMS.fields_by_name['min_max'].containing_oneof = _QUANTIZATIONINFO_PERAXISPARAMS.oneofs_by_name['params_oneof']
_QUANTIZATIONINFO_PERAXISPARAMS.oneofs_by_name['params_oneof'].fields.append(_QUANTIZATIONINFO_PERAXISPARAMS.fields_by_name['affine_params'])
_QUANTIZATIONINFO_PERAXISPARAMS.fields_by_name['affine_params'].containing_oneof = _QUANTIZATIONINFO_PERAXISPARAMS.oneofs_by_name['params_oneof']
_QUANTIZATIONINFO_METADATA.containing_type = _QUANTIZATIONINFO
_QUANTIZATIONINFO_QUANTPARAMS.fields_by_name['params'].message_type = _QUANTIZATIONINFO_PERAXISPARAMS
_QUANTIZATIONINFO_QUANTPARAMS.fields_by_name['meta'].message_type = _QUANTIZATIONINFO_METADATA
_QUANTIZATIONINFO_QUANTPARAMS.containing_type = _QUANTIZATIONINFO
_QUANTIZATIONINFO_QUANTPARAMS.oneofs_by_name['name_oneof'].fields.append(_QUANTIZATIONINFO_QUANTPARAMS.fields_by_name['name'])
_QUANTIZATIONINFO_QUANTPARAMS.fields_by_name['name'].containing_oneof = _QUANTIZATIONINFO_QUANTPARAMS.oneofs_by_name['name_oneof']
_QUANTIZATIONINFO_QUANTPARAMS.oneofs_by_name['name_oneof'].fields.append(_QUANTIZATIONINFO_QUANTPARAMS.fields_by_name['name_regex'])
_QUANTIZATIONINFO_QUANTPARAMS.fields_by_name['name_regex'].containing_oneof = _QUANTIZATIONINFO_QUANTPARAMS.oneofs_by_name['name_oneof']
_QUANTIZATIONINFO.fields_by_name['entries'].message_type = _QUANTIZATIONINFO_QUANTPARAMS
DESCRIPTOR.message_types_by_name['QuantizationInfo'] = _QUANTIZATIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
QuantizationInfo = _reflection.GeneratedProtocolMessageType('QuantizationInfo', (_message.Message,), {'MinMax': _reflection.GeneratedProtocolMessageType('MinMax', (_message.Message,), {'DESCRIPTOR': _QUANTIZATIONINFO_MINMAX, '__module__': 'tensorflow.compiler.mlir.lite.quantization.quantization_info_pb2'}), 'AffineParams': _reflection.GeneratedProtocolMessageType('AffineParams', (_message.Message,), {'DESCRIPTOR': _QUANTIZATIONINFO_AFFINEPARAMS, '__module__': 'tensorflow.compiler.mlir.lite.quantization.quantization_info_pb2'}), 'PerAxisParams': _reflection.GeneratedProtocolMessageType('PerAxisParams', (_message.Message,), {'DESCRIPTOR': _QUANTIZATIONINFO_PERAXISPARAMS, '__module__': 'tensorflow.compiler.mlir.lite.quantization.quantization_info_pb2'}), 'Metadata': _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {'DESCRIPTOR': _QUANTIZATIONINFO_METADATA, '__module__': 'tensorflow.compiler.mlir.lite.quantization.quantization_info_pb2'}), 'QuantParams': _reflection.GeneratedProtocolMessageType('QuantParams', (_message.Message,), {'DESCRIPTOR': _QUANTIZATIONINFO_QUANTPARAMS, '__module__': 'tensorflow.compiler.mlir.lite.quantization.quantization_info_pb2'}), 'DESCRIPTOR': _QUANTIZATIONINFO, '__module__': 'tensorflow.compiler.mlir.lite.quantization.quantization_info_pb2'})
_sym_db.RegisterMessage(QuantizationInfo)
_sym_db.RegisterMessage(QuantizationInfo.MinMax)
_sym_db.RegisterMessage(QuantizationInfo.AffineParams)
_sym_db.RegisterMessage(QuantizationInfo.PerAxisParams)
_sym_db.RegisterMessage(QuantizationInfo.Metadata)
_sym_db.RegisterMessage(QuantizationInfo.QuantParams)
DESCRIPTOR._options = None
