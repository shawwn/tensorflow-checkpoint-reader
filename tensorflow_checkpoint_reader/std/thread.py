import os
import os as _os

if hasattr(_os, 'sched_getaffinity'):
  def hardware_concurrency():
    return len(_os.sched_getaffinity(0))
else:
  def hardware_concurrency():
    return os.cpu_count()
