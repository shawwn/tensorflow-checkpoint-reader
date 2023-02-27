from tensorflow_checkpoint_reader import py_checkpoint_reader
from pprint import pprint as pp
import numpy as np
import sys

if __name__ == '__main__':
  args = sys.argv[1:]
  filename = 'models/117M/model.ckpt' if len(args) < 1 else args[0]
  reader = py_checkpoint_reader.NewCheckpointReader(filename)
  values = {name: reader.get_tensor(name) for name in reader.get_variable_to_shape_map().keys()}
  # pp(reader.get_variable_to_shape_map())
  # pp(reader.get_variable_to_dtype_map())
  for name, v in values.items():
    print(name + ':\t', str(v.dtype).replace('float', 'f').replace('int', 'i') + str(list(v.shape)).replace(' ', ''), '= {:,}'.format(np.prod(v.shape)) if len(v.shape) > 1 else '')
    # print('', v)
  print('Total params: {:,}'.format(sum([np.prod(x.shape) for x in values.values()])))
