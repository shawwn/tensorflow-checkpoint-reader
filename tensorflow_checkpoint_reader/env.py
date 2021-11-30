from abc import ABC
from typing import Callable, List, Optional, Dict, NamedTuple, Tuple, Union
from functools import wraps as _wraps
import threading as _threading
import os as _os

from . import file_system
from . import errors
from . import misc
from . import core
from . import io
from . import env_time
from . import port
from . import strings
from . import platform
from . import posix_file_system

_name_mutex = _threading.RLock()

class ThreadOptions(NamedTuple):
  """Options to configure a Thread.

  Note that the options are all hints, and the
  underlying implementation may choose to ignore it."""

  stack_size: int = 0  # Thread stack size to use (in bytes).
  guard_size: int = 0  # Guard area size to use near thread stacks to use (in bytes)
  numa_node: int = port.kNUMANoAffinity

class Thread:
  """Represents a thread used to run a TensorFlow function."""

  def __init__(self, thread: _threading.Thread):
    self._thread = thread

  def release(self):
    """Blocks until the thread of control stops running."""
    if self._thread is not None:
      self._thread.join()
      self._thread = None

  def __del__(self):
    self.release()

  def __enter__(self):
    return self

  def __exit__(self, *args):
    self.release()


class Env(ABC):
  """An interface used by the tensorflow implementation to
  access operating system functionality like the filesystem etc.

  Callers may wish to provide a custom Env object to get fine grain
  control.

  All Env implementations are safe for concurrent access from
  multiple threads without any external synchronization."""
  def __init__(self):
    self._file_system_registry = FileSystemRegistryImpl()

  @classmethod
  def default(cls):
    """Returns a default environment suitable for the current operating
    system.

    Sophisticated users may wish to provide their own Env
    implementation instead of relying on this default environment.

    The result of Default() belongs to this library and must never be deleted."""
    return misc.putattr(cls, '_default_env', WindowsEnv if platform.is_windows_platform() else PosixEnv)

  def get_file_system_for_file(self, fname: bytes) -> Tuple[errors.Status, Optional[file_system.FileSystem]]:
    """Returns the FileSystem object to handle operations on the file
    specified by 'fname'. The FileSystem object is used as the implementa
    for the file system related (non-virtual) functions that follow.
    Returned FileSystem object is still owned by the Env object and will
    (might) be destroyed when the environment is destroyed."""
    scheme, host, path = io.parse_uri(fname)
    file_system = self._file_system_registry.lookup(scheme.bytes())
    if file_system is None:
      if scheme.empty():
        scheme = core.string_view(b"[local]")
      return errors.Unimplemented("File system scheme '", scheme,
                                  "' not implemented (file: '", fname, "')"), None
    return errors.Status.OK(), file_system

  def get_file_size(self, fname) -> Tuple[errors.Status, int]:
    err, fs = self.get_file_system_for_file(fname)
    if not err.ok():
      return err, 0
    return fs.get_file_size(fname)

  def new_random_access_file(self, fname) -> Tuple[errors.Status, Optional[file_system.RandomAccessFile]]:
    err, fs = self.get_file_system_for_file(fname)
    if not err.ok():
      return err, None
    return fs.new_random_access_file(fname)

  def get_registered_file_system_schemes(self, schemes: List[bytes]) -> errors.Status:
    """Returns the file system schemes registered for this Env."""
    return self._file_system_registry.get_registered_file_system_schemes(schemes)

  def register_file_system_factory(self, scheme: str, factory: file_system.FileSystemRegistry.Factory):
    """Register a file system for a scheme."""
    return self._file_system_registry.register_factory(scheme, factory)

  def register_file_system(self, scheme: str, file_system: file_system.FileSystem):
    """Register a modular file system for a scheme.

    Same as `register_file_system_factory` but for filesystems provided by plugins.

    TODO(mihaimaruseac): After all filesystems are converted, make this be the
    canonical registration function."""
    return self._file_system_registry.register_filesystem(scheme, file_system)

  def now_nanos(self) -> int:
    """Returns the number of nano-seconds since the Unix epoch."""
    return env_time.EnvTime.now_nanos()

  def now_micros(self) -> int:
    """Returns the number of micro-seconds since the Unix epoch."""
    return env_time.EnvTime.now_micros()

  def now_seconds(self) -> int:
    """Returns the number of seconds since the Unix epoch."""
    return env_time.EnvTime.now_seconds()
  
  def sleep_for_microseconds(self, micros: int):
    """Sleeps/delays the thread for the prescribed number of micro-seconds."""
    return port.usleep(micros)
  
  def get_process_id(self) -> int:
    """Returns the process ID of the calling process."""
    return _os.getpid()
  
  def start_thread(self, thread_options: ThreadOptions, name: str, fn: Callable[[], None]) -> Thread:
    """Returns a new thread that is running fn() and is identified
    (for debugging/performance-analysis) by "name".

    Caller takes ownership of the result and must delete it eventually
    (the deletion will block until fn() stops running)."""
    return PThread(thread_options, name, fn)

  def get_current_thread_id(self) -> int:
    """Returns the thread id of calling thread.
    Posix: Returns pthread id which is only guaranteed to be unique within a
           process.
    Windows: Returns thread id which is unique."""
    return port.get_current_thread_id()

  def get_current_thread_name(self) -> Optional[str]:
    """Returns the current thread name if possible, otherwise None."""
    with _name_mutex:
      if port.get_current_thread_id() in get_thread_name_registry():
        name = get_thread_name_registry()[port.get_current_thread_id()]
        return name
      return None
  
  def sched_closure(self, closure: Callable[[], None]):
    """Schedules the given closure on a thread-pool.

    NOTE(mrry): This closure may block."""
    _threading.Thread(target=closure, daemon=True).start()

  def sched_closure_after(self, micros: int, closure: Callable[[], None]):
    """Schedules the given closure on a thread-pool after the given number
    of microseconds.

    NOTE(mrry): This closure must not block."""
    @_wraps(closure)
    def thunk():
      self.sleep_for_microseconds(micros)
      closure()
    return self.sched_closure(thunk)

class ThreadParams(NamedTuple):
  name: str
  fn: Callable[[], None]

class PThread(Thread):
  def __init__(self, thread_options: ThreadOptions, name: str, fn: Callable[[], None]):
    params = ThreadParams(name, fn)
    thread = _threading.Thread(target=_thread_fn, args=(params,), daemon=True)
    super().__init__(thread)
    thread.start()

def _thread_fn(params: ThreadParams):
  with _name_mutex:
    get_thread_name_registry()[port.get_current_thread_id()] = params.name
  params.fn()
  with _name_mutex:
    del get_thread_name_registry()[port.get_current_thread_id()]

def get_thread_name_registry() -> Dict[int, str]:
  return misc.putattr(get_thread_name_registry, 'singleton', lambda: dict())

class PosixEnv(Env, ABC):
  pass

class WindowsEnv(Env, ABC):
  pass

class FileSystemRegistryImpl(file_system.FileSystemRegistry):
  _registry: Dict[bytes, file_system.FileSystem]

  def __init__(self):
    self._mu = _threading.RLock()
    self._registry = dict()

  def register_factory(self, scheme: bytes, factory: file_system.FileSystemRegistry.Factory) -> errors.Status:
    with self._mu:
      scheme = core.string_view(scheme).bytes()
      if scheme in self._registry:
        return errors.AlreadyExists("File factory for ", scheme,
                                    " already registered")
      self._registry[scheme] = factory()
      return errors.Status.OK()

  def register_filesystem(self, scheme: bytes, filesystem: file_system.FileSystem) -> errors.Status:
    with self._mu:
      scheme = core.string_view(scheme).bytes()
      if scheme in self._registry:
        return errors.AlreadyExists("File factory for ", scheme,
                                    " already registered")
      self._registry[scheme] = filesystem
      return errors.Status.OK()

  def lookup(self, scheme: bytes) -> Optional[file_system.FileSystem]:
    with self._mu:
      scheme = core.string_view(scheme).bytes()
      if scheme in self._registry:
        return self._registry[scheme]

  def get_registered_file_system_schemes(self, schemes: List[bytes]) -> errors.Status:
    with self._mu:
      for e in self._registry.keys():
        schemes.append(e)
      return errors.Status.OK()


Env.default().register_file_system_factory("", posix_file_system.PosixFileSystem)

def getenv(name: str) -> str:
  return _os.getenv(str(name))

def setenv(name: str, value: str, overwrite: int) -> int:
  if overwrite:
    _os.environ[str(name)] = str(value)
  else:
    _os.environ.setdefault(str(name), str(value))
  return 0

def unsetenv(name: str) -> int:
  _os.unsetenv(str(name))
  return 0
