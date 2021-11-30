import socket as _socket
import time as _time
import threading as _threading
import sys as _sys
import os as _os

from . import load_library
from . import std

kNUMANoAffinity = -1

def hostname() -> str:
  return _socket.gethostname()

def job_name() -> str:
  return _os.getenv("TF_JOB_NAME") or ""

def num_schedulable_cpus() -> int:
  count = std.thread.hardware_concurrency()
  if count > 0:
    return count
  kDefaultCores = 4  # Semi-conservative guess
  print("can't determine number of CPU cores: assuming %d" % kDefaultCores, file=_sys.stderr)
  return kDefaultCores

def max_parallelism(numa_node: int = kNUMANoAffinity) -> int:
  if numa_node != kNUMANoAffinity:
    # Assume that CPUs are equally distributed over available NUMA nodes.
    # This may not be true, but there isn't currently a better way of
    # determining the number of CPUs specific to the requested node.
    return num_schedulable_cpus() // numa_num_nodes()
  return num_schedulable_cpus()

def num_total_cpus() -> int:
  return _os.cpu_count()

def numa_enabled() -> bool:
  return numa_num_nodes() > 1

def numa_num_nodes() -> int:
  return 1  # NUMA not yet implemented

def usleep(micros: int):
  if _usleep is not None:
    _usleep(int(micros))
  else:
    _time.sleep(micros / 1000000.0)

def get_current_thread_id() -> int:
  return _threading.get_ident()


_status, libc = load_library.load_dynamic_library(load_library.format_library_file_name('c', ''))
if not _status.ok():
  _status, libc = load_library.load_dynamic_library(load_library.format_library_file_name('c', '6'))
_status, _usleep = load_library.get_symbol_from_library(libc, 'usleep')
del _status
