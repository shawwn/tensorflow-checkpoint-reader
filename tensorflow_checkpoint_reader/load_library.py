import platform as _platform
from typing import Any, Tuple

from . import errors

def load_dynamic_library(library_filename: str) -> Tuple[errors.Status, Any]:
  import ctypes
  try:
    return errors.Status.OK(), ctypes.CDLL(str(library_filename))
  except OSError:
    return errors.NotFound(library_filename), None

def get_symbol_from_library(handle, symbol_name: str) -> Tuple[errors.Status, Any]:
  try:
    return errors.Status.OK(), getattr(handle, str(symbol_name))
  except AttributeError:
    return errors.NotFound(symbol_name), None

def format_library_file_name(name: str, version: str = None) -> str:
  name = str(name)
  version = str(version) if version is not None else ''
  if _platform.system() == "Darwin":
    if version:
      filename = "lib" + name + "." + version + ".dylib"
    else:
      filename = "lib" + name + ".dylib"
  else:
    if version:
      filename = "lib" + name + ".so." + version
    else:
      filename = "lib" + name + ".so"
  return filename

