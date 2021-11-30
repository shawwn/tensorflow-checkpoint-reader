from typing import Callable, Optional, List, Tuple
from fnmatch import fnmatch
from abc import ABC, abstractmethod
import os
import stat

from . import errors
from . import core
from . import io
from . import file_statistics


class RandomAccessFile(ABC):
  """A file abstraction for randomly reading the contents of a file."""

  def name(self) -> Tuple[errors.Status, core.StringPiece]:
    """Returns the name of the file.

    This is an optional operation that may not be implemented by every
    filesystem."""
    return errors.Unimplemented("This filesystem does not support name()"), core.StringPiece()

  @abstractmethod
  def close(self) -> errors.Status:
    return errors.Unimplemented("This filesystem does not support close()")

  @abstractmethod
  def read(self, offset: int, n: int) -> Tuple[errors.Status, core.StringPiece]:
    """Reads up to `n` bytes from the file starting at `offset`.

    Returns `OUT_OF_RANGE` if fewer than n bytes were stored in `*result`
    because of EOF.

    Safe for concurrent use by multiple threads."""
    return errors.Unimplemented("This filesystem does not support read()"), core.StringPiece()

  def __enter__(self):
    return self

  def __exit__(self, *args):
    errors.raise_if_error(self.close())

  def __del__(self):
    errors.raise_if_error(self.close())


class FileSystem(ABC):
  def parse_uri(self, name) -> Tuple[core.StringPiece, core.StringPiece, core.StringPiece]:
    return io.parse_uri(name)

  def match(self, filename, pattern):
    filename = core.string_view(filename)
    pattern = core.string_view(pattern)
    return fnmatch(filename.slice(), pattern.slice())

  def translate_name(self, name) -> bytes:
    name = core.string_view(name)
    # If the name is empty, CleanPath returns "." which is incorrect and
    # we should return the empty path instead.
    if name.empty():
      return name.bytes()
    # Otherwise, properly separate the URI components and clean the path one
    scheme, host, path = self.parse_uri(name)
    # If `path` becomes empty, return `/` (`file://` should be `/`), not `.`.
    if path.empty():
      return b"/"
    
    return self.clean_path(path)

  def clean_path(self, name) -> bytes:
    name = core.string_view(name)
    result = os.path.normpath(name.bytes())
    return result

  @abstractmethod
  def new_random_access_file(self, name) -> Tuple[errors.Status, Optional[RandomAccessFile]]:
    return errors.Unimplemented("This filesystem does not support new_random_access_file()"), None

  @abstractmethod
  def get_file_size(self, name) -> Tuple[errors.Status, int]:
    return errors.Status.OK(), 0

  @abstractmethod
  def file_exists(self, name) -> errors.Status:
    return errors.Status.OK()

  @abstractmethod
  def stat(self, name, stats: file_statistics.FileStatistics) -> errors.Status:
    return errors.Status.OK()

  @abstractmethod
  def get_children(self, dir) -> Tuple[errors.Status, List[bytes]]:
    return errors.Status.OK(), []

  def is_directory(self, name) -> errors.Status:
    err = self.file_exists(name)
    if not err.ok():
      return err
    stat = file_statistics.FileStatistics()
    err = self.stat(name, stat)
    if not err.ok():
      return err
    if stat.is_directory:
      return errors.Status.OK()
    return errors.FailedPrecondition("Not a directory")


class FileSystemRegistry(ABC):
  Factory = Callable[[], FileSystem]

  @abstractmethod
  def register_factory(self, scheme: str, factory: Factory) -> errors.Status:
    raise NotImplementedError()

  @abstractmethod
  def register_filesystem(self, scheme: str, filesystem: FileSystem) -> errors.Status:
    raise NotImplementedError()

  @abstractmethod
  def lookup(self, scheme: str) -> Optional[FileSystem]:
    raise NotImplementedError()

  @abstractmethod
  def get_registered_file_system_schemes(self, schemes: List[str]) -> errors.Status:
    raise NotImplementedError()
