import socket as _socket
import time as _time
import threading as _threading
import platform as _platform

from . import load_library

kNUMANoAffinity = -1

def hostname() -> str:
  return _socket.gethostname()

def usleep(micros: int):
  if _usleep is not None:
    _usleep(int(micros))
  else:
    _time.sleep(micros / 1000000.0)

def get_current_thread_id() -> int:
  return _threading.get_ident()

# # https://stackoverflow.com/questions/1325581/how-do-i-check-if-im-running-on-windows-in-python
# def is_windows_platform() -> bool:
#   return _os.name == 'nt'

def is_windows_platform() -> bool:
  return _platform.system() == "Windows"

def is_apple_platform() -> bool:
  return _platform.system() == "Darwin"


_status, libc = load_library.load_dynamic_library(load_library.format_library_file_name('c', ''))
if not _status.ok():
  _status, libc = load_library.load_dynamic_library(load_library.format_library_file_name('c', '6'))
_status, _usleep = load_library.get_symbol_from_library(libc, 'usleep')
del _status
