from tensorflow_checkpoint_reader import py_checkpoint_reader
from pprint import pprint as pp
import numpy as np
import sys

if __name__ == '__main__':
  args = sys.argv[1:]
  model = '117M' if len(args) < 1 else args[0]
  reader = py_checkpoint_reader.NewCheckpointReader(f'models/{model}/model.ckpt')
  values = {name: reader.get_tensor(name) for name in reader.get_variable_to_shape_map().keys()}
  pp(reader.get_variable_to_shape_map())
  pp(reader.get_variable_to_dtype_map())
  pp({name: (v.dtype, '{:,} params'.format(np.prod(v.shape)), v.shape, v) for name, v in values.items()})
  print('Total params: {:,}'.format(sum([np.prod(x.shape) for x in values.values()])))
