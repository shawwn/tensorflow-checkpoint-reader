from __future__ import annotations
import os
import io as _io
import stat
import errno as _errno
from typing import List, Tuple, Optional, cast as _cast

from . import file_system
from . import file_system_helper
from . import file_statistics
from . import errors
from . import core
from . import std

# 128KB of copy buffer
kPosixCopyFileBufferSize = 128 * 1024

# pread() based random-access
class PosixRandomAccessFile(file_system.RandomAccessFile):
  def __init__(self, fname, fd):
    self._filename = core.string_view(fname).bytes()
    self._fd = fd
    self._closed = False

  def __repr__(self):
    return (f"PosixRandomAccessFile(fd={self._fd!r}, filename={self._filename!r}"
            + (", closed" if self._closed else "") + ")")

  def name(self) -> Tuple[errors.Status, bytes]:
    return errors.Status.OK(), self._filename

  def close(self) -> errors.Status:
    closed, self._closed = self._closed, True
    if not closed:
      try:
        os.close(self._fd)
      except IOError as e:
        return errors.IOError(self._filename, e.errno)
    return errors.Status.OK()

  def read(self, offset: int, n: int) -> Tuple[errors.Status, core.StringPiece]:
    fd = self._fd
    s = errors.Status.OK()
    dst = b''
    while n > 0 and s.ok():
      # Some platforms, notably macs, throw EINVAL if pread is asked to read
      # more than fits in a 32-bit integer.
      if n > std.INT32_MAX:
        requested_read_length = std.INT32_MAX
      else:
        requested_read_length = n
      errno = None
      try:
        ret = os.pread(fd, requested_read_length, offset)
        r = len(ret)
        if r < requested_read_length:
          r = 0
      except IOError as e:
        ret = b""
        r = -1
        errno = e.errno
      if r > 0:
        dst += ret
        n -= r
        offset += r
      elif r == 0:
        s = errors.OutOfRange("Read less bytes than requested")
      elif errno == _errno.EINTR or errno == _errno.EAGAIN:
        # Retry
        pass
      else:
        assert errno is not None
        s = errors.IOError(self._filename, errno)
    result = core.StringPiece(dst)
    return s, result

class PosixWritableFile(file_system.WritableFile):
  def __init__(self, fname, file: _io.BufferedWriter):
    self._filename = core.string_view(fname).bytes()
    self._file = file

  def __del__(self):
    # if (file_ != nullptr) {
    if self._file is not None:
      # // Ignoring any potential errors
      # fclose(file_);
      self._file.close()
    # }

  def __repr__(self):
    return f"PosixWritableFile(file={self._file!r}, filename={self._filename!r})"

  def append(self, data) -> errors.Status:
    data = core.string_view(data)
    r = self._file.write(data.bytes())
    if r != data.size():
      import ctypes
      errno = ctypes.get_errno()
      return errors.IOError(self._filename, errno)
    return errors.Status.OK()

  def name(self) -> Tuple[errors.Status, bytes]:
    return errors.Status.OK(), self._filename

  def close(self) -> errors.Status:
    if self._file is None:
      return errors.IOError(self._filename, _errno.EBADF)
    self._file.close()
    self._file = None
    return errors.Status.OK()

  def flush(self) -> errors.Status:
    try:
      self._file.flush()
      return errors.Status.OK()
    except IOError as e:
      return errors.IOError(self._filename, e.errno)

  def sync(self) -> errors.Status:
    try:
      self._file.flush()
      return errors.Status.OK()
    except IOError as e:
      return errors.IOError(self._filename, e.errno)

  def tell(self) -> Tuple[errors.Status, int]:
    try:
      return errors.Status.OK(), self._file.tell()
    except IOError as e:
      return errors.IOError(self._filename, e.errno), -1

class PosixFileSystem(file_system.FileSystem):
  def new_random_access_file(self, name) -> Tuple[errors.Status, Optional[file_system.RandomAccessFile]]:
    fname = self.translate_name(name)
    try:
      errno = None
      fd = os.open(fname, os.O_RDONLY)
    except IOError as e:
      errno = e.errno
      fd = -1
    if fd < 0:
      return errors.IOError(fname, errno), None
    else:
      result = PosixRandomAccessFile(fname, fd)
      return errors.Status.OK(), result

  def new_writable_file(self, name) -> Tuple[errors.Status, Optional[file_system.WritableFile]]:
    fname = self.translate_name(name)
    try:
      file = open(fname, "wb")
      result = PosixWritableFile(fname, _cast(_io.BufferedWriter, file))
      return errors.Status.OK(), result
    except IOError as e:
      return errors.IOError(fname, e.errno), None

  def rename_file(self, src, target) -> errors.Status:
    try:
      os.rename(self.translate_name(src), self.translate_name(target))
      return errors.Status.OK()
    except IOError as e:
      return errors.IOError(src, e.errno)

  def delete_file(self, name) -> errors.Status:
    try:
      os.unlink(self.translate_name(name))
      return errors.Status.OK()
    except IOError as e:
      return errors.IOError(name, e.errno)

  def file_exists(self, fname) -> errors.Status:
    if os.access(self.translate_name(fname), os.F_OK):
      return errors.Status.OK()
    return errors.NotFound(fname, " not found")

  def get_matching_paths(self, pattern) -> Tuple[errors.Status, Optional[List]]:
    from . import env # import here due to circular import
    return file_system_helper.get_matching_paths(self, env.Env.default(), pattern)

  def stat(self, name, stats: file_statistics.FileStatistics) -> errors.Status:
    fname = self.translate_name(name)
    try:
      sbuf = os.stat(fname)
    except IOError as e:
      return errors.IOError(fname, e.errno)
    stats.length = sbuf.st_size
    # stats->mtime_nsec = sbuf.st_mtime * 1e9;
    stats.mtime_nsec = sbuf.st_mtime_ns
    stats.is_directory = stat.S_ISDIR(sbuf.st_mode)
    return errors.Status.OK()

  def get_file_size(self, name) -> Tuple[errors.Status, int]:
    fname = self.translate_name(name)
    try:
      sbuf = os.stat(fname)
    except IOError as e:
      return errors.IOError(fname, e.errno), 0
    return errors.Status.OK(), sbuf.st_size

  def get_children(self, dir) -> Tuple[errors.Status, List[bytes]]:
    fname = self.translate_name(dir)
    result = []
    try:
      for d in os.scandir(fname):
        entry: os.DirEntry = d
        basename = core.string_view(entry.name).bytes()
        if basename not in [b".", b".."]:
          result.append(basename)
    except IOError as e:
      return errors.IOError(fname, e.errno), result
    return errors.Status.OK(), result






