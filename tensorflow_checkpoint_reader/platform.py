import platform as _platform

# # https://stackoverflow.com/questions/1325581/how-do-i-check-if-im-running-on-windows-in-python
# def is_windows_platform() -> bool:
#   return _os.name == 'nt'

def is_windows_platform() -> bool:
  return _platform.system() == "Windows"

def is_apple_platform() -> bool:
  return _platform.system() == "Darwin"

def is_freebsd_platform() -> bool:
  return _platform.system() == "FreeBSD"

def is_iphone_platform() -> bool:
  return False  # TODO: Does Python run on iOS?

def is_haiku_platform() -> bool:
  return _platform.system() == "Haiku"  # TODO: Is this correct?
