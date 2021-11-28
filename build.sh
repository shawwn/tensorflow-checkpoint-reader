protoc --proto_path=tensorflow_checkpoint_reader/pb --python_out=tensorflow_checkpoint_reader/pb tensorflow_checkpoint_reader/pb/tensorflow/core/protobuf/tensor_bundle.proto
for x in allocation_description.proto \
api_def.proto \
attr_value.proto \
cost_graph.proto \
dataset_options.proto \
device_attributes.proto \
full_type.proto \
function.proto \
graph.proto \
graph_transfer_info.proto \
kernel_def.proto \
log_memory.proto \
model.proto \
node_def.proto \
op_def.proto \
reader_base.proto \
resource_handle.proto \
step_stats.proto \
summary.proto \
tensor.proto \
tensor_description.proto \
tensor_shape.proto \
tensor_slice.proto \
types.proto \
variable.proto \
versions.proto
do
  echo $x
  protoc --proto_path=tensorflow_checkpoint_reader/pb --python_out=tensorflow_checkpoint_reader/pb tensorflow_checkpoint_reader/pb/tensorflow/core/framework/$x
done
