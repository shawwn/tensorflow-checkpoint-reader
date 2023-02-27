import random
import numpy as np

def new_64():
  return np.asarray(random.randbytes(8)).view(dtype=np.uint64).item()