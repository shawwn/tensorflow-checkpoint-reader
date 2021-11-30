from typing import Callable, Optional, List
from fnmatch import fnmatch
from abc import ABC, abstractmethod
import os
import stat

from . import errors
from . import core
from . import io
from . import file_statistics

class FileSystem(ABC):
  def parse_uri(self, name) -> (core.StringPiece, core.StringPiece, core.StringPiece):
    return io.parse_uri(name)

  def match(self, filename, pattern):
    filename = core.string_view(filename)
    pattern = core.string_view(pattern)
    return fnmatch(filename.slice(), pattern.slice())

  def translate_name(self, name) -> core.StringPiece:
    name = core.string_view(name)
    # If the name is empty, CleanPath returns "." which is incorrect and
    # we should return the empty path instead.
    if name.empty():
      return name
    # Otherwise, properly separate the URI components and clean the path one
    scheme, host, path = self.parse_uri(name)
    # If `path` becomes empty, return `/` (`file://` should be `/`), not `.`.
    if path.empty():
      return core.string_view("/")
    
    return self.clean_path(path)

  def clean_path(self, name) -> core.StringPiece:
    name = core.string_view(name)
    result = os.path.normpath(bytes(name))
    return core.string_view(result)

  @abstractmethod
  def get_file_size(self, name) -> (errors.Status, int):
    return errors.Status.OK(), 0

  @abstractmethod
  def file_exists(self, name) -> errors.Status:
    return errors.Status.OK()

  @abstractmethod
  def stat(self, name, stats: file_statistics.FileStatistics) -> errors.Status:
    return errors.Status.OK()

  @abstractmethod
  def get_children(self, dir) -> (errors.Status, List[bytes]):
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


class FileSystemRegistry:
  Factory = Callable[[], FileSystem]

  def register_factory(self, scheme: str, factory: Factory) -> errors.Status:
    raise NotImplementedError()

  def register_filesystem(self, scheme: str, filesystem: FileSystem) -> errors.Status:
    raise NotImplementedError()

  def lookup(self, scheme: str) -> Optional[FileSystem]:
    raise NotImplementedError()

  def get_registered_file_system_schemes(self, schemes: List[str]) -> errors.Status:
    raise NotImplementedError()
