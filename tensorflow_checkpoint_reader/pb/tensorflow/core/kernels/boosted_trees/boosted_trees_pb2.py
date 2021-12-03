
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='tensorflow/core/kernels/boosted_trees/boosted_trees.proto', package='tensorflow.boosted_trees', syntax='proto3', serialized_options=b'\n\x18org.tensorflow.frameworkB\x12BoostedTreesProtosP\x01\xf8\x01\x01', create_key=_descriptor._internal_create_key, serialized_pb=b'\n9tensorflow/core/kernels/boosted_trees/boosted_trees.proto\x12\x18tensorflow.boosted_trees"\xc6\x02\n\x04Node\x12.\n\x04leaf\x18\x01 \x01(\x0b2\x1e.tensorflow.boosted_trees.LeafH\x00\x12E\n\x10bucketized_split\x18\x02 \x01(\x0b2).tensorflow.boosted_trees.BucketizedSplitH\x00\x12G\n\x11categorical_split\x18\x03 \x01(\x0b2*.tensorflow.boosted_trees.CategoricalSplitH\x00\x12;\n\x0bdense_split\x18\x04 \x01(\x0b2$.tensorflow.boosted_trees.DenseSplitH\x00\x129\n\x08metadata\x18\x89\x06 \x01(\x0b2&.tensorflow.boosted_trees.NodeMetadataB\x06\n\x04node"S\n\x0cNodeMetadata\x12\x0c\n\x04gain\x18\x01 \x01(\x02\x125\n\roriginal_leaf\x18\x02 \x01(\x0b2\x1e.tensorflow.boosted_trees.Leaf"\x93\x01\n\x04Leaf\x122\n\x06vector\x18\x01 \x01(\x0b2 .tensorflow.boosted_trees.VectorH\x00\x12?\n\rsparse_vector\x18\x02 \x01(\x0b2&.tensorflow.boosted_trees.SparseVectorH\x00\x12\x0e\n\x06scalar\x18\x03 \x01(\x02B\x06\n\x04leaf"\x17\n\x06Vector\x12\r\n\x05value\x18\x01 \x03(\x02",\n\x0cSparseVector\x12\r\n\x05index\x18\x01 \x03(\x05\x12\r\n\x05value\x18\x02 \x03(\x02"\xb8\x01\n\x0fBucketizedSplit\x12\x12\n\nfeature_id\x18\x01 \x01(\x05\x12\x11\n\tthreshold\x18\x02 \x01(\x05\x12\x14\n\x0cdimension_id\x18\x05 \x01(\x05\x12E\n\x11default_direction\x18\x06 \x01(\x0e2*.tensorflow.boosted_trees.DefaultDirection\x12\x0f\n\x07left_id\x18\x03 \x01(\x05\x12\x10\n\x08right_id\x18\x04 \x01(\x05"n\n\x10CategoricalSplit\x12\x12\n\nfeature_id\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\x12\x14\n\x0cdimension_id\x18\x05 \x01(\x05\x12\x0f\n\x07left_id\x18\x03 \x01(\x05\x12\x10\n\x08right_id\x18\x04 \x01(\x05"V\n\nDenseSplit\x12\x12\n\nfeature_id\x18\x01 \x01(\x05\x12\x11\n\tthreshold\x18\x02 \x01(\x02\x12\x0f\n\x07left_id\x18\x03 \x01(\x05\x12\x10\n\x08right_id\x18\x04 \x01(\x05"5\n\x04Tree\x12-\n\x05nodes\x18\x01 \x03(\x0b2\x1e.tensorflow.boosted_trees.Node"\xdc\x01\n\x0cTreeMetadata\x12\x18\n\x10num_layers_grown\x18\x02 \x01(\x05\x12\x14\n\x0cis_finalized\x18\x03 \x01(\x08\x12Z\n\x16post_pruned_nodes_meta\x18\x04 \x03(\x0b2:.tensorflow.boosted_trees.TreeMetadata.PostPruneNodeUpdate\x1a@\n\x13PostPruneNodeUpdate\x12\x13\n\x0bnew_node_id\x18\x01 \x01(\x05\x12\x14\n\x0clogit_change\x18\x02 \x03(\x02"\x88\x01\n\x0fGrowingMetadata\x12\x1b\n\x13num_trees_attempted\x18\x01 \x01(\x03\x12\x1c\n\x14num_layers_attempted\x18\x02 \x01(\x03\x12\x1d\n\x15last_layer_node_start\x18\x03 \x01(\x05\x12\x1b\n\x13last_layer_node_end\x18\x04 \x01(\x05"\xd7\x01\n\x0cTreeEnsemble\x12-\n\x05trees\x18\x01 \x03(\x0b2\x1e.tensorflow.boosted_trees.Tree\x12\x14\n\x0ctree_weights\x18\x02 \x03(\x02\x12=\n\rtree_metadata\x18\x03 \x03(\x0b2&.tensorflow.boosted_trees.TreeMetadata\x12C\n\x10growing_metadata\x18\x04 \x01(\x0b2).tensorflow.boosted_trees.GrowingMetadata"N\n\x0bDebugOutput\x12\x13\n\x0bfeature_ids\x18\x01 \x03(\x05\x12\x13\n\x0blogits_path\x18\x02 \x03(\x02\x12\x15\n\rleaf_node_ids\x18\x03 \x03(\x05*m\n\x14SplitTypeWithDefault\x12\x1b\n\x17INEQUALITY_DEFAULT_LEFT\x10\x00\x12\x1c\n\x18INEQUALITY_DEFAULT_RIGHT\x10\x01\x12\x1a\n\x16EQUALITY_DEFAULT_RIGHT\x10\x03*7\n\x10DefaultDirection\x12\x10\n\x0cDEFAULT_LEFT\x10\x00\x12\x11\n\rDEFAULT_RIGHT\x10\x01B3\n\x18org.tensorflow.frameworkB\x12BoostedTreesProtosP\x01\xf8\x01\x01b\x06proto3')
_SPLITTYPEWITHDEFAULT = _descriptor.EnumDescriptor(name='SplitTypeWithDefault', full_name='tensorflow.boosted_trees.SplitTypeWithDefault', filename=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key, values=[_descriptor.EnumValueDescriptor(name='INEQUALITY_DEFAULT_LEFT', index=0, number=0, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='INEQUALITY_DEFAULT_RIGHT', index=1, number=1, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='EQUALITY_DEFAULT_RIGHT', index=2, number=3, serialized_options=None, type=None, create_key=_descriptor._internal_create_key)], containing_type=None, serialized_options=None, serialized_start=1824, serialized_end=1933)
_sym_db.RegisterEnumDescriptor(_SPLITTYPEWITHDEFAULT)
SplitTypeWithDefault = enum_type_wrapper.EnumTypeWrapper(_SPLITTYPEWITHDEFAULT)
_DEFAULTDIRECTION = _descriptor.EnumDescriptor(name='DefaultDirection', full_name='tensorflow.boosted_trees.DefaultDirection', filename=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key, values=[_descriptor.EnumValueDescriptor(name='DEFAULT_LEFT', index=0, number=0, serialized_options=None, type=None, create_key=_descriptor._internal_create_key), _descriptor.EnumValueDescriptor(name='DEFAULT_RIGHT', index=1, number=1, serialized_options=None, type=None, create_key=_descriptor._internal_create_key)], containing_type=None, serialized_options=None, serialized_start=1935, serialized_end=1990)
_sym_db.RegisterEnumDescriptor(_DEFAULTDIRECTION)
DefaultDirection = enum_type_wrapper.EnumTypeWrapper(_DEFAULTDIRECTION)
INEQUALITY_DEFAULT_LEFT = 0
INEQUALITY_DEFAULT_RIGHT = 1
EQUALITY_DEFAULT_RIGHT = 3
DEFAULT_LEFT = 0
DEFAULT_RIGHT = 1
_NODE = _descriptor.Descriptor(name='Node', full_name='tensorflow.boosted_trees.Node', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='leaf', full_name='tensorflow.boosted_trees.Node.leaf', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='bucketized_split', full_name='tensorflow.boosted_trees.Node.bucketized_split', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='categorical_split', full_name='tensorflow.boosted_trees.Node.categorical_split', index=2, number=3, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='dense_split', full_name='tensorflow.boosted_trees.Node.dense_split', index=3, number=4, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='metadata', full_name='tensorflow.boosted_trees.Node.metadata', index=4, number=777, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='node', full_name='tensorflow.boosted_trees.Node.node', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=88, serialized_end=414)
_NODEMETADATA = _descriptor.Descriptor(name='NodeMetadata', full_name='tensorflow.boosted_trees.NodeMetadata', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='gain', full_name='tensorflow.boosted_trees.NodeMetadata.gain', index=0, number=1, type=2, cpp_type=6, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='original_leaf', full_name='tensorflow.boosted_trees.NodeMetadata.original_leaf', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=416, serialized_end=499)
_LEAF = _descriptor.Descriptor(name='Leaf', full_name='tensorflow.boosted_trees.Leaf', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='vector', full_name='tensorflow.boosted_trees.Leaf.vector', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='sparse_vector', full_name='tensorflow.boosted_trees.Leaf.sparse_vector', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='scalar', full_name='tensorflow.boosted_trees.Leaf.scalar', index=2, number=3, type=2, cpp_type=6, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='leaf', full_name='tensorflow.boosted_trees.Leaf.leaf', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=502, serialized_end=649)
_VECTOR = _descriptor.Descriptor(name='Vector', full_name='tensorflow.boosted_trees.Vector', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='value', full_name='tensorflow.boosted_trees.Vector.value', index=0, number=1, type=2, cpp_type=6, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=651, serialized_end=674)
_SPARSEVECTOR = _descriptor.Descriptor(name='SparseVector', full_name='tensorflow.boosted_trees.SparseVector', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='index', full_name='tensorflow.boosted_trees.SparseVector.index', index=0, number=1, type=5, cpp_type=1, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='value', full_name='tensorflow.boosted_trees.SparseVector.value', index=1, number=2, type=2, cpp_type=6, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=676, serialized_end=720)
_BUCKETIZEDSPLIT = _descriptor.Descriptor(name='BucketizedSplit', full_name='tensorflow.boosted_trees.BucketizedSplit', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='feature_id', full_name='tensorflow.boosted_trees.BucketizedSplit.feature_id', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='threshold', full_name='tensorflow.boosted_trees.BucketizedSplit.threshold', index=1, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='dimension_id', full_name='tensorflow.boosted_trees.BucketizedSplit.dimension_id', index=2, number=5, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='default_direction', full_name='tensorflow.boosted_trees.BucketizedSplit.default_direction', index=3, number=6, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='left_id', full_name='tensorflow.boosted_trees.BucketizedSplit.left_id', index=4, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='right_id', full_name='tensorflow.boosted_trees.BucketizedSplit.right_id', index=5, number=4, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=723, serialized_end=907)
_CATEGORICALSPLIT = _descriptor.Descriptor(name='CategoricalSplit', full_name='tensorflow.boosted_trees.CategoricalSplit', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='feature_id', full_name='tensorflow.boosted_trees.CategoricalSplit.feature_id', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='value', full_name='tensorflow.boosted_trees.CategoricalSplit.value', index=1, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='dimension_id', full_name='tensorflow.boosted_trees.CategoricalSplit.dimension_id', index=2, number=5, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='left_id', full_name='tensorflow.boosted_trees.CategoricalSplit.left_id', index=3, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='right_id', full_name='tensorflow.boosted_trees.CategoricalSplit.right_id', index=4, number=4, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=909, serialized_end=1019)
_DENSESPLIT = _descriptor.Descriptor(name='DenseSplit', full_name='tensorflow.boosted_trees.DenseSplit', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='feature_id', full_name='tensorflow.boosted_trees.DenseSplit.feature_id', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='threshold', full_name='tensorflow.boosted_trees.DenseSplit.threshold', index=1, number=2, type=2, cpp_type=6, label=1, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='left_id', full_name='tensorflow.boosted_trees.DenseSplit.left_id', index=2, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='right_id', full_name='tensorflow.boosted_trees.DenseSplit.right_id', index=3, number=4, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1021, serialized_end=1107)
_TREE = _descriptor.Descriptor(name='Tree', full_name='tensorflow.boosted_trees.Tree', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='nodes', full_name='tensorflow.boosted_trees.Tree.nodes', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1109, serialized_end=1162)
_TREEMETADATA_POSTPRUNENODEUPDATE = _descriptor.Descriptor(name='PostPruneNodeUpdate', full_name='tensorflow.boosted_trees.TreeMetadata.PostPruneNodeUpdate', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='new_node_id', full_name='tensorflow.boosted_trees.TreeMetadata.PostPruneNodeUpdate.new_node_id', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='logit_change', full_name='tensorflow.boosted_trees.TreeMetadata.PostPruneNodeUpdate.logit_change', index=1, number=2, type=2, cpp_type=6, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1321, serialized_end=1385)
_TREEMETADATA = _descriptor.Descriptor(name='TreeMetadata', full_name='tensorflow.boosted_trees.TreeMetadata', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='num_layers_grown', full_name='tensorflow.boosted_trees.TreeMetadata.num_layers_grown', index=0, number=2, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='is_finalized', full_name='tensorflow.boosted_trees.TreeMetadata.is_finalized', index=1, number=3, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='post_pruned_nodes_meta', full_name='tensorflow.boosted_trees.TreeMetadata.post_pruned_nodes_meta', index=2, number=4, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[_TREEMETADATA_POSTPRUNENODEUPDATE], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1165, serialized_end=1385)
_GROWINGMETADATA = _descriptor.Descriptor(name='GrowingMetadata', full_name='tensorflow.boosted_trees.GrowingMetadata', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='num_trees_attempted', full_name='tensorflow.boosted_trees.GrowingMetadata.num_trees_attempted', index=0, number=1, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='num_layers_attempted', full_name='tensorflow.boosted_trees.GrowingMetadata.num_layers_attempted', index=1, number=2, type=3, cpp_type=2, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='last_layer_node_start', full_name='tensorflow.boosted_trees.GrowingMetadata.last_layer_node_start', index=2, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='last_layer_node_end', full_name='tensorflow.boosted_trees.GrowingMetadata.last_layer_node_end', index=3, number=4, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1388, serialized_end=1524)
_TREEENSEMBLE = _descriptor.Descriptor(name='TreeEnsemble', full_name='tensorflow.boosted_trees.TreeEnsemble', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='trees', full_name='tensorflow.boosted_trees.TreeEnsemble.trees', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='tree_weights', full_name='tensorflow.boosted_trees.TreeEnsemble.tree_weights', index=1, number=2, type=2, cpp_type=6, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='tree_metadata', full_name='tensorflow.boosted_trees.TreeEnsemble.tree_metadata', index=2, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='growing_metadata', full_name='tensorflow.boosted_trees.TreeEnsemble.growing_metadata', index=3, number=4, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1527, serialized_end=1742)
_DEBUGOUTPUT = _descriptor.Descriptor(name='DebugOutput', full_name='tensorflow.boosted_trees.DebugOutput', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='feature_ids', full_name='tensorflow.boosted_trees.DebugOutput.feature_ids', index=0, number=1, type=5, cpp_type=1, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='logits_path', full_name='tensorflow.boosted_trees.DebugOutput.logits_path', index=1, number=2, type=2, cpp_type=6, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='leaf_node_ids', full_name='tensorflow.boosted_trees.DebugOutput.leaf_node_ids', index=2, number=3, type=5, cpp_type=1, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1744, serialized_end=1822)
_NODE.fields_by_name['leaf'].message_type = _LEAF
_NODE.fields_by_name['bucketized_split'].message_type = _BUCKETIZEDSPLIT
_NODE.fields_by_name['categorical_split'].message_type = _CATEGORICALSPLIT
_NODE.fields_by_name['dense_split'].message_type = _DENSESPLIT
_NODE.fields_by_name['metadata'].message_type = _NODEMETADATA
_NODE.oneofs_by_name['node'].fields.append(_NODE.fields_by_name['leaf'])
_NODE.fields_by_name['leaf'].containing_oneof = _NODE.oneofs_by_name['node']
_NODE.oneofs_by_name['node'].fields.append(_NODE.fields_by_name['bucketized_split'])
_NODE.fields_by_name['bucketized_split'].containing_oneof = _NODE.oneofs_by_name['node']
_NODE.oneofs_by_name['node'].fields.append(_NODE.fields_by_name['categorical_split'])
_NODE.fields_by_name['categorical_split'].containing_oneof = _NODE.oneofs_by_name['node']
_NODE.oneofs_by_name['node'].fields.append(_NODE.fields_by_name['dense_split'])
_NODE.fields_by_name['dense_split'].containing_oneof = _NODE.oneofs_by_name['node']
_NODEMETADATA.fields_by_name['original_leaf'].message_type = _LEAF
_LEAF.fields_by_name['vector'].message_type = _VECTOR
_LEAF.fields_by_name['sparse_vector'].message_type = _SPARSEVECTOR
_LEAF.oneofs_by_name['leaf'].fields.append(_LEAF.fields_by_name['vector'])
_LEAF.fields_by_name['vector'].containing_oneof = _LEAF.oneofs_by_name['leaf']
_LEAF.oneofs_by_name['leaf'].fields.append(_LEAF.fields_by_name['sparse_vector'])
_LEAF.fields_by_name['sparse_vector'].containing_oneof = _LEAF.oneofs_by_name['leaf']
_BUCKETIZEDSPLIT.fields_by_name['default_direction'].enum_type = _DEFAULTDIRECTION
_TREE.fields_by_name['nodes'].message_type = _NODE
_TREEMETADATA_POSTPRUNENODEUPDATE.containing_type = _TREEMETADATA
_TREEMETADATA.fields_by_name['post_pruned_nodes_meta'].message_type = _TREEMETADATA_POSTPRUNENODEUPDATE
_TREEENSEMBLE.fields_by_name['trees'].message_type = _TREE
_TREEENSEMBLE.fields_by_name['tree_metadata'].message_type = _TREEMETADATA
_TREEENSEMBLE.fields_by_name['growing_metadata'].message_type = _GROWINGMETADATA
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['NodeMetadata'] = _NODEMETADATA
DESCRIPTOR.message_types_by_name['Leaf'] = _LEAF
DESCRIPTOR.message_types_by_name['Vector'] = _VECTOR
DESCRIPTOR.message_types_by_name['SparseVector'] = _SPARSEVECTOR
DESCRIPTOR.message_types_by_name['BucketizedSplit'] = _BUCKETIZEDSPLIT
DESCRIPTOR.message_types_by_name['CategoricalSplit'] = _CATEGORICALSPLIT
DESCRIPTOR.message_types_by_name['DenseSplit'] = _DENSESPLIT
DESCRIPTOR.message_types_by_name['Tree'] = _TREE
DESCRIPTOR.message_types_by_name['TreeMetadata'] = _TREEMETADATA
DESCRIPTOR.message_types_by_name['GrowingMetadata'] = _GROWINGMETADATA
DESCRIPTOR.message_types_by_name['TreeEnsemble'] = _TREEENSEMBLE
DESCRIPTOR.message_types_by_name['DebugOutput'] = _DEBUGOUTPUT
DESCRIPTOR.enum_types_by_name['SplitTypeWithDefault'] = _SPLITTYPEWITHDEFAULT
DESCRIPTOR.enum_types_by_name['DefaultDirection'] = _DEFAULTDIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {'DESCRIPTOR': _NODE, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(Node)
NodeMetadata = _reflection.GeneratedProtocolMessageType('NodeMetadata', (_message.Message,), {'DESCRIPTOR': _NODEMETADATA, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(NodeMetadata)
Leaf = _reflection.GeneratedProtocolMessageType('Leaf', (_message.Message,), {'DESCRIPTOR': _LEAF, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(Leaf)
Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), {'DESCRIPTOR': _VECTOR, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(Vector)
SparseVector = _reflection.GeneratedProtocolMessageType('SparseVector', (_message.Message,), {'DESCRIPTOR': _SPARSEVECTOR, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(SparseVector)
BucketizedSplit = _reflection.GeneratedProtocolMessageType('BucketizedSplit', (_message.Message,), {'DESCRIPTOR': _BUCKETIZEDSPLIT, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(BucketizedSplit)
CategoricalSplit = _reflection.GeneratedProtocolMessageType('CategoricalSplit', (_message.Message,), {'DESCRIPTOR': _CATEGORICALSPLIT, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(CategoricalSplit)
DenseSplit = _reflection.GeneratedProtocolMessageType('DenseSplit', (_message.Message,), {'DESCRIPTOR': _DENSESPLIT, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(DenseSplit)
Tree = _reflection.GeneratedProtocolMessageType('Tree', (_message.Message,), {'DESCRIPTOR': _TREE, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(Tree)
TreeMetadata = _reflection.GeneratedProtocolMessageType('TreeMetadata', (_message.Message,), {'PostPruneNodeUpdate': _reflection.GeneratedProtocolMessageType('PostPruneNodeUpdate', (_message.Message,), {'DESCRIPTOR': _TREEMETADATA_POSTPRUNENODEUPDATE, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'}), 'DESCRIPTOR': _TREEMETADATA, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(TreeMetadata)
_sym_db.RegisterMessage(TreeMetadata.PostPruneNodeUpdate)
GrowingMetadata = _reflection.GeneratedProtocolMessageType('GrowingMetadata', (_message.Message,), {'DESCRIPTOR': _GROWINGMETADATA, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(GrowingMetadata)
TreeEnsemble = _reflection.GeneratedProtocolMessageType('TreeEnsemble', (_message.Message,), {'DESCRIPTOR': _TREEENSEMBLE, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(TreeEnsemble)
DebugOutput = _reflection.GeneratedProtocolMessageType('DebugOutput', (_message.Message,), {'DESCRIPTOR': _DEBUGOUTPUT, '__module__': 'tensorflow.core.kernels.boosted_trees.boosted_trees_pb2'})
_sym_db.RegisterMessage(DebugOutput)
DESCRIPTOR._options = None
