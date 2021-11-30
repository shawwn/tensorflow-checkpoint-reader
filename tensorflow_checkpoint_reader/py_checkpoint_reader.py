from . import bundle_reader
from . import env
from . import core

class NewCheckpointReader:
  def __init__(self, filename):
    self._reader = bundle_reader.BundleReader(env.Env.default(), filename)

  def get_variable_to_shape_map(self):
    return {name.decode('utf-8'): arr.shape for name, arr in self._reader._tensors}

  def get_variable_to_dtype_map(self):
    return {name.decode('utf-8'): arr.dtype for name, arr in self._reader._tensors}

  def get_tensor(self, name):
    name = core.string_view(name).bytes()
    for k, v in self._reader._tensors:
      if k == name:
        return v

