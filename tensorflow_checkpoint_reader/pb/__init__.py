# If tensorflow has already been imported, use their _pb2 moduels to avoid duplicate protobuf registry entries.
import sys
if 'tensorflow' in sys.modules:
  for k, v in list(sys.modules.items()):
    if k.startswith('tensorflow.') and k.endswith('_pb2'):
      sys.modules[__name__ + '.' + k] = v
  del k, v
del sys
