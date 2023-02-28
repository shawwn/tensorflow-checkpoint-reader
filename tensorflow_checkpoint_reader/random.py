import numpy as np
import secrets

def new_64():
  return np.asarray(secrets.token_bytes(8)).view(dtype=np.uint64).item()
