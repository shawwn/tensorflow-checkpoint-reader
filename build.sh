# protoc can't generate relative imports.
# See https://github.com/protocolbuffers/protobuf/issues/1491
#
# set -ex
# find . -type f -name '*.proto' -print0 | xargs -0 protoc --python_out=tensorflow_checkpoint_reader/pb --proto_path=tensorflow_checkpoint_reader/pb

# let's try this solution:
# https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-977985256
# pip3 install protoletariat
#
set -ex
find . -type f -name '*.proto' -print0 | xargs -0 protol --in-place --python-out tensorflow_checkpoint_reader/pb protoc --proto-path=tensorflow_checkpoint_reader/pb
