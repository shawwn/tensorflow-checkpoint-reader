from typing import Callable, Optional, List

from . import errors

class FileSystem:
  pass

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
