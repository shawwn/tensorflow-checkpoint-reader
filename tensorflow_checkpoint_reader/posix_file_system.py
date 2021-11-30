import os
import stat
from abc import ABC
from typing import List

from . import file_system
from . import file_statistics
from . import errors
from . import core

class PosixFileSystem(file_system.FileSystem, ABC):
  def file_exists(self, name) -> errors.Status:
    fname = bytes(self.translate_name(name))
    if os.access(fname, os.F_OK):
      return errors.Status.OK()
    return errors.NotFound(fname, " not found")

  def stat(self, name, stats: file_statistics.FileStatistics) -> errors.Status:
    fname = bytes(self.translate_name(name))
    try:
      sbuf = os.stat(fname)
    except IOError as e:
      return errors.IOError(str(e), e.errno)
    stats.length = sbuf.st_size
    # stats->mtime_nsec = sbuf.st_mtime * 1e9;
    stats.mtime_nsec = sbuf.st_mtime_ns
    stats.is_directory = stat.S_ISDIR(sbuf.st_mode)
    return errors.Status.OK()

  def get_file_size(self, name) -> (errors.Status, int):
    fname = bytes(self.translate_name(name))
    try:
      sbuf = os.stat(fname)
    except IOError as e:
      return errors.IOError(str(e), e.errno), 0
    return errors.Status.OK(), sbuf.st_size

  def get_children(self, dir) -> (errors.Status, List[bytes]):
    fname = bytes(self.translate_name(dir))
    result = []
    try:
      for d in os.scandir(fname):
        entry: os.DirEntry = d
        basename = core.string_view(entry.name).slice()
        if basename not in [b".", b".."]:
          result.append(basename)
    except IOError as e:
      return errors.IOError(str(e), e.errno), result
    return errors.Status.OK(), result






