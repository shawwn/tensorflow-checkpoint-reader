from typing import Callable, Optional, List, Tuple
from fnmatch import fnmatch
from abc import ABC, abstractmethod
import os

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

class WritableFile(ABC):
  """A file abstraction for sequential writing.

  The implementation must provide buffering since callers may append
  small fragments at a time to the file."""

  def name(self) -> Tuple[errors.Status, core.StringPiece]:
    """Returns the name of the file.

    This is an optional operation that may not be implemented by every
    filesystem."""
    return errors.Unimplemented("This filesystem does not support name()"), core.StringPiece()

  @abstractmethod
  def close(self) -> errors.Status:
    """Close the file.

    Flush() and de-allocate resources associated with this file

    Typical return codes (not guaranteed to be exhaustive):
     * OK
     * Other codes, as returned from Flush()
    """
    return errors.Unimplemented("This filesystem does not support close()")

  @abstractmethod
  def append(self, data: core.StringPiece) -> errors.Status:
    """Append 'data' to the file."""
    return errors.Unimplemented("This filesystem does not support append()")

  @abstractmethod
  def flush(self) -> errors.Status:
    """Flushes the file and optionally syncs contents to filesystem.

    This should flush any local buffers whose contents have not been
    delivered to the filesystem.

    If the process terminates after a successful flush, the contents
    may still be persisted, since the underlying filesystem may
    eventually flush the contents.  If the OS or machine crashes
    after a successful flush, the contents may or may not be
    persisted, depending on the implementation.
    """
    return errors.Unimplemented("This filesystem does not support flush()")

  @abstractmethod
  def sync(self) -> errors.Status:
    """Syncs contents of file to filesystem.

    This waits for confirmation from the filesystem that the contents
    of the file have been persisted to the filesystem; if the OS
    or machine crashes after a successful Sync, the contents should
    be properly saved."""
    return errors.Unimplemented("This filesystem does not support sync()")

  @abstractmethod
  def tell(self) -> Tuple[errors.Status, int]:
    """Retrieves the current write position in the file, or -1 on error.

    This is an optional operation, subclasses may choose to return
    errors::Unimplemented.
    """
    return errors.Unimplemented("This filesystem does not support tell()"), -1

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
    return fnmatch(filename.bytes(), pattern.bytes())

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
  def new_writable_file(self, name) -> Tuple[errors.Status, Optional[WritableFile]]:
    return errors.Unimplemented("This filesystem does not support new_writable_file()"), None

  def has_atomic_move(self, name) -> Tuple[errors.Status, bool]:
    return errors.Status.OK(), True

  @abstractmethod
  def rename_file(self, src, target) -> errors.Status:
    return errors.Status.OK()

  @abstractmethod
  def get_file_size(self, name) -> Tuple[errors.Status, int]:
    return errors.Status.OK(), 0

  @abstractmethod
  def delete_file(self, name) -> errors.Status:
    return errors.Status.OK()

  @abstractmethod
  def file_exists(self, name) -> errors.Status:
    return errors.Status.OK()

  @abstractmethod
  def get_matching_paths(self, pattern) -> Tuple[errors.Status, Optional[List]]:
    """Given a pattern, stores in *results the set of paths that matches
    that pattern. *results is cleared.

    pattern must match all of a name, not just a substring.

    pattern: { term }
    term:
      '*': matches any sequence of non-'/' characters
      '?': matches a single non-'/' character
      '[' [ '^' ] { match-list } ']':
           matches any single character (not) on the list
      c: matches character c (c != '*', '?', '\\', '[')
      '\\' c: matches character c
    character-range:
      c: matches character c (c != '\\', '-', ']')
      '\\' c: matches character c
      lo '-' hi: matches character c for lo <= c <= hi

    Typical return codes:
     * OK - no errors
     * UNIMPLEMENTED - Some underlying functions (like GetChildren) are not
                       implemented
    """
    return errors.Status.OK(), []

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
