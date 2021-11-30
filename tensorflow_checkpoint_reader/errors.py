from typing import Union, NamedTuple, Tuple
import errno
import os

from .pb.tensorflow.core.protobuf import error_codes_pb2 as error
from . import core, strings, platform

ErrorType = int
MsgType = Union[str, core.StringPiece]

def error_name(code: ErrorType) -> str:
  if code == error.OK:
    return "OK"
  elif code == error.CANCELLED:
    return "Cancelled"
  elif code == error.UNKNOWN:
    return "Unknown"
  elif code == error.INVALID_ARGUMENT:
    return "Invalid argument"
  elif code == error.DEADLINE_EXCEEDED:
    return "Deadline exceeded"
  elif code == error.NOT_FOUND:
    return "Not found"
  elif code == error.ALREADY_EXISTS:
    return "Already exists"
  elif code == error.PERMISSION_DENIED:
    return "Permission denied"
  elif code == error.UNAUTHENTICATED:
    return "Unauthenticated"
  elif code == error.RESOURCE_EXHAUSTED:
    return "Resource exhausted"
  elif code == error.FAILED_PRECONDITION:
    return "Failed precondition"
  elif code == error.ABORTED:
    return "Aborted"
  elif code == error.OUT_OF_RANGE:
    return "Out of range"
  elif code == error.UNIMPLEMENTED:
    return "Unimplemented"
  elif code == error.INTERNAL:
    return "Internal"
  elif code == error.UNAVAILABLE:
    return "Unavailable"
  elif code == error.DATA_LOSS:
    return "Data loss"
  else:
    return "Unknown code(%d)" % code


class Status(Exception):
  class State(NamedTuple):
    code: ErrorType
    msg: str

  def __init__(self, code: ErrorType = error.OK, msg: MsgType = None):
    if code == error.OK:
      self._state = None
      super().__init__()
    else:
      assert msg is not None
      self._state = None if code == error.OK else Status.State(code, str(msg))
      super().__init__(self._state.msg)

  @staticmethod
  def OK():
    return Status()

  def ok(self) -> bool:
    return self._state is None

  def code(self) -> ErrorType:
    return error.OK if self.ok() else self._state.code

  def error_message(self) -> str:
    return "" if self.ok() else self._state.msg

  def update(self, other):
    """If `ok()`, stores `new_status` into `*this`.  If `!ok()`,
    preserves the current status, but may augment with additional
    information about `new_status`.
    Convenient way of keeping track of the first error encountered.
    Instead of:
      `if (overall_status.ok()) overall_status = new_status`
    Use:
      `overall_status.Update(new_status);`"""
    if self.ok():
      self._state = other._state

  def to_string(self) -> str:
    """Return a string representation of this status suitable for
    printing. Returns the string `"OK"` for success."""
    if self._state is None:
      return "OK"
    else:
      result = error_name(self.code())
      result += ": "
      result += self._state.msg
      return result

  def __str__(self):
    return self.to_string()

  def __repr__(self):
    return f"Status({self.to_string()!r})"

  def __eq__(self, other):
    return isinstance(other, Status) and (self._state == other._state or self.to_string() == other.to_string())

  def __ne__(self, other):
    return not (self == other)


# DECLARE_ERROR(InvalidArgument, INVALID_ARGUMENT)
class InvalidArgument(Status):
  def __init__(self, *msg):
    super().__init__(error.INVALID_ARGUMENT, strings.str_cat(*msg))

def is_invalid_argument(status: Status):
  return status.code() == error.INVALID_ARGUMENT


# DECLARE_ERROR(NotFound, NOT_FOUND)
class NotFound(Status):
  def __init__(self, *msg):
    super().__init__(error.NOT_FOUND, strings.str_cat(*msg))

def is_not_found(status: Status):
  return status.code() == error.NOT_FOUND


# DECLARE_ERROR(AlreadyExists, ALREADY_EXISTS)
class AlreadyExists(Status):
  def __init__(self, *msg):
    super().__init__(error.ALREADY_EXISTS, strings.str_cat(*msg))

def is_already_exists(status: Status):
  return status.code() == error.ALREADY_EXISTS


# DECLARE_ERROR(ResourceExhausted, RESOURCE_EXHAUSTED)
class ResourceExhausted(Status):
  def __init__(self, *msg):
    super().__init__(error.RESOURCE_EXHAUSTED, strings.str_cat(*msg))

def is_resource_exhausted(status: Status):
  return status.code() == error.RESOURCE_EXHAUSTED


# DECLARE_ERROR(Unavailable, UNAVAILABLE)
class Unavailable(Status):
  def __init__(self, *msg):
    super().__init__(error.UNAVAILABLE, strings.str_cat(*msg))

def is_unavailable(status: Status):
  return status.code() == error.UNAVAILABLE


# DECLARE_ERROR(FailedPrecondition, FAILED_PRECONDITION)
class FailedPrecondition(Status):
  def __init__(self, *msg):
    super().__init__(error.FAILED_PRECONDITION, strings.str_cat(*msg))

def is_failed_precondition(status: Status):
  return status.code() == error.FAILED_PRECONDITION


# DECLARE_ERROR(OutOfRange, OUT_OF_RANGE)
class OutOfRange(Status):
  def __init__(self, *msg):
    super().__init__(error.OUT_OF_RANGE, strings.str_cat(*msg))

def is_out_of_range(status: Status):
  return status.code() == error.OUT_OF_RANGE


# DECLARE_ERROR(Unimplemented, UNIMPLEMENTED)
class Unimplemented(Status):
  def __init__(self, *msg):
    super().__init__(error.UNIMPLEMENTED, strings.str_cat(*msg))

def is_unimplemented(status: Status):
  return status.code() == error.UNIMPLEMENTED


# DECLARE_ERROR(Internal, INTERNAL)
class Internal(Status):
  def __init__(self, *msg):
    super().__init__(error.INTERNAL, strings.str_cat(*msg))

def is_internal(status: Status):
  return status.code() == error.INTERNAL


# DECLARE_ERROR(Aborted, ABORTED)
class Aborted(Status):
  def __init__(self, *msg):
    super().__init__(error.ABORTED, strings.str_cat(*msg))

def is_aborted(status: Status):
  return status.code() == error.ABORTED


# DECLARE_ERROR(DeadlineExceeded, DEADLINE_EXCEEDED)
class DeadlineExceeded(Status):
  def __init__(self, *msg):
    super().__init__(error.DEADLINE_EXCEEDED, strings.str_cat(*msg))

def is_deadline_exceeded(status: Status):
  return status.code() == error.DEADLINE_EXCEEDED


# DECLARE_ERROR(DataLoss, DATA_LOSS)
class DataLoss(Status):
  def __init__(self, *msg):
    super().__init__(error.DATA_LOSS, strings.str_cat(*msg))

def is_data_loss(status: Status):
  return status.code() == error.DATA_LOSS


# DECLARE_ERROR(Unknown, UNKNOWN)
class Unknown(Status):
  def __init__(self, *msg):
    super().__init__(error.UNKNOWN, strings.str_cat(*msg))

def is_unknown(status: Status):
  return status.code() == error.UNKNOWN


# DECLARE_ERROR(PermissionDenied, PERMISSION_DENIED)
class PermissionDenied(Status):
  def __init__(self, *msg):
    super().__init__(error.PERMISSION_DENIED, strings.str_cat(*msg))

def is_permission_denied(status: Status):
  return status.code() == error.PERMISSION_DENIED


# DECLARE_ERROR(Unauthenticated, UNAUTHENTICATED)
class Unauthenticated(Status):
  def __init__(self, *msg):
    super().__init__(error.UNAUTHENTICATED, strings.str_cat(*msg))

def is_unauthenticated(status: Status):
  return status.code() == error.UNAUTHENTICATED


class IOError(Status):
  def __init__(self, context, err_number: int):
    code = errno_to_code(err_number)
    super().__init__(code, strings.str_cat(context, "; ", os.strerror(code)))


def errno_to_code(err_number: int) -> ErrorType:
  if err_number == 0:
    return error.OK

  if err_number == errno.EINVAL:        # Invalid argument
    return error.INVALID_ARGUMENT
  if err_number == errno.ENAMETOOLONG:  # Filename too long
    return error.INVALID_ARGUMENT
  if err_number == errno.E2BIG:         # Argument list too long
    return error.INVALID_ARGUMENT
  if err_number == errno.EDESTADDRREQ:  # Destination address required
    return error.INVALID_ARGUMENT
  if err_number == errno.EDOM:          # Mathematics argument out of domain of function
    return error.INVALID_ARGUMENT
  if err_number == errno.EFAULT:        # Bad address
    return error.INVALID_ARGUMENT
  if err_number == errno.EILSEQ:        # Illegal byte sequence
    return error.INVALID_ARGUMENT
  if err_number == errno.ENOPROTOOPT:   # Protocol not available
    return error.INVALID_ARGUMENT
  if err_number == errno.ENOSTR:        # Not a STREAM
    return error.INVALID_ARGUMENT
  if err_number == errno.ENOTSOCK:      # Not a socket
    return error.INVALID_ARGUMENT
  if err_number == errno.ENOTTY:        # Inappropriate I/O control operation
    return error.INVALID_ARGUMENT
  if err_number == errno.EPROTOTYPE:    # Protocol wrong type for socket
    return error.INVALID_ARGUMENT
  if err_number == errno.ESPIPE:        # Invalid seek
    return error.INVALID_ARGUMENT

  if err_number == errno.ETIMEDOUT:  # Connection timed out
    return error.DEADLINE_EXCEEDED
  if err_number == errno.ETIME:      # Timer expired
    return error.DEADLINE_EXCEEDED

  if err_number == errno.ENODEV:  # No such device
    return error.NOT_FOUND
  if err_number == errno.ENOENT:  # No such file or directory
    return error.NOT_FOUND
  if err_number == errno.ENXIO:   # No such device or address
    return error.NOT_FOUND
  if err_number == errno.ESRCH:   # No such process
    return error.NOT_FOUND

  if err_number == errno.EEXIST:         # File exists
    return error.ALREADY_EXISTS
  if err_number == errno.EADDRNOTAVAIL:  # Address not available
    return error.ALREADY_EXISTS
  if err_number == errno.EALREADY:       # Connection already in progress
    return error.ALREADY_EXISTS

  if err_number == errno.EPERM:   # Operation not permitted
    return error.PERMISSION_DENIED
  if err_number == errno.EACCES:  # Permission denied
    return error.PERMISSION_DENIED
  if err_number == errno.EROFS:   # Read only file system
    return error.PERMISSION_DENIED

  if err_number == errno.ENOTEMPTY:   # Directory not empty
    return error.FAILED_PRECONDITION
  if err_number == errno.EISDIR:      # Is a directory
    return error.FAILED_PRECONDITION
  if err_number == errno.ENOTDIR:     # Not a directory
    return error.FAILED_PRECONDITION
  if err_number == errno.EADDRINUSE:  # Address already in use
    return error.FAILED_PRECONDITION
  if err_number == errno.EBADF:       # Invalid file descriptor
    return error.FAILED_PRECONDITION
  if err_number == errno.EBUSY:       # Device or resource busy
    return error.FAILED_PRECONDITION
  if err_number == errno.ECHILD:      # No child processes
    return error.FAILED_PRECONDITION
  if err_number == errno.EISCONN:     # Socket is connected
    return error.FAILED_PRECONDITION
  if not platform.is_windows_platform() and not platform.is_haiku_platform():
    if err_number == errno.ENOTBLK:  # Block device required
      return error.FAILED_PRECONDITION
  if err_number == errno.ENOTCONN:  # The socket is not connected
    return error.FAILED_PRECONDITION
  if err_number == errno.EPIPE:     # Broken pipe
    return error.FAILED_PRECONDITION
  if not platform.is_windows_platform():
    if err_number == errno.ESHUTDOWN:  # Cannot send after transport endpoint shutdown
      return error.FAILED_PRECONDITION
  if err_number == errno.ETXTBSY:  # Text file busy
    return error.FAILED_PRECONDITION

  if err_number == errno.ENOSPC:  # No space left on device
    return error.RESOURCE_EXHAUSTED
  if not platform.is_windows_platform():
    if err_number == errno.EDQUOT:  # Disk quota exceeded
      return error.RESOURCE_EXHAUSTED
  if err_number == errno.EMFILE:   # Too many open files
    return error.RESOURCE_EXHAUSTED
  if err_number == errno.EMLINK:   # Too many links
    return error.RESOURCE_EXHAUSTED
  if err_number == errno.ENFILE:   # Too many open files in system
    return error.RESOURCE_EXHAUSTED
  if err_number == errno.ENOBUFS:  # No buffer space available
    return error.RESOURCE_EXHAUSTED
  if err_number == errno.ENODATA:  # No message is available on the STREAM read queue
    return error.RESOURCE_EXHAUSTED
  if err_number == errno.ENOMEM:   # Not enough space
    return error.RESOURCE_EXHAUSTED
  if err_number == errno.ENOSR:    # No STREAM resources
    return error.RESOURCE_EXHAUSTED
  if not platform.is_windows_platform() and not platform.is_haiku_platform():
    if err_number == errno.EUSERS:  # Too many users
      return error.RESOURCE_EXHAUSTED

  if err_number == errno.EFBIG:      # File too large
    return error.OUT_OF_RANGE
  if err_number == errno.EOVERFLOW:  # Value too large to be stored in data type
    return error.OUT_OF_RANGE
  if err_number == errno.ERANGE:     # Result too large
    return error.OUT_OF_RANGE

  if err_number == errno.ENOSYS:        # Function not implemented
    return error.UNIMPLEMENTED
  if err_number == errno.ENOTSUP:       # Operation not supported
    return error.UNIMPLEMENTED
  if err_number == errno.EAFNOSUPPORT:  # Address family not supported
    return error.UNIMPLEMENTED
  if not platform.is_windows_platform():
    if err_number == errno.EPFNOSUPPORT:  # Protocol family not supported
      return error.UNIMPLEMENTED
  if err_number == errno.EPROTONOSUPPORT:  # Protocol not supported
    return error.UNIMPLEMENTED
  if not platform.is_windows_platform() and not platform.is_haiku_platform():
    if err_number == errno.ESOCKTNOSUPPORT:  # Socket type not supported
      return error.UNIMPLEMENTED
  if err_number == errno.EXDEV:  # Improper link
    return error.UNIMPLEMENTED

  if err_number == errno.EAGAIN:        # Resource temporarily unavailable
    return error.UNAVAILABLE
  if err_number == errno.ECONNREFUSED:  # Connection refused
    return error.UNAVAILABLE
  if err_number == errno.ECONNABORTED:  # Connection aborted
    return error.UNAVAILABLE
  if err_number == errno.ECONNRESET:    # Connection reset
    return error.UNAVAILABLE
  if err_number == errno.EINTR:         # Interrupted function call
    return error.UNAVAILABLE
  if not platform.is_windows_platform():
    if err_number == errno.EHOSTDOWN:  # Host is down
      return error.UNAVAILABLE
  if err_number == errno.EHOSTUNREACH:  # Host is unreachable
    return error.UNAVAILABLE
  if err_number == errno.ENETDOWN:      # Network is down
    return error.UNAVAILABLE
  if err_number == errno.ENETRESET:     # Connection aborted by network
    return error.UNAVAILABLE
  if err_number == errno.ENETUNREACH:   # Network unreachable
    return error.UNAVAILABLE
  if err_number == errno.ENOLCK:        # No locks available
    return error.UNAVAILABLE
  if err_number == errno.ENOLINK:       # Link has been severed
    return error.UNAVAILABLE
  if not (platform.is_apple_platform() or platform.is_freebsd_platform() or platform.is_windows_platform()
          or platform.is_haiku_platform()):
    if err_number == errno.ENONET:  # Machine is not on the network
      return error.UNAVAILABLE

  if err_number == errno.EDEADLK:  # Resource deadlock avoided
    return error.ABORTED
  if not platform.is_windows_platform():
    if err_number == errno.ESTALE:  # Stale file handle
      return error.ABORTED

  if err_number == errno.ECANCELED:  # Operation cancelled
    return error.CANCELLED

  # NOTE: If you get any of the following (especially in a
  # reproducible way) and can propose a better mapping,
  # please email the owners about updating this mapping.

  if err_number == errno.EBADMSG:      # Bad message
    return error.UNKNOWN
  if err_number == errno.EIDRM:        # Identifier removed
    return error.UNKNOWN
  if err_number == errno.EINPROGRESS:  # Operation in progress
    return error.UNKNOWN
  if err_number == errno.EIO:          # I/O error
    return error.UNKNOWN
  if err_number == errno.ELOOP:        # Too many levels of symbolic links
    return error.UNKNOWN
  if err_number == errno.ENOEXEC:      # Exec format error
    return error.UNKNOWN
  if err_number == errno.ENOMSG:       # No message of the desired type
    return error.UNKNOWN
  if err_number == errno.EPROTO:       # Protocol error
    return error.UNKNOWN
  if not platform.is_windows_platform() and not platform.is_haiku_platform():
    if err_number == errno.EREMOTE:  # Object is remote
      return error.UNKNOWN

  return error.UNKNOWN

def raise_if_error(arg: Union[Status, Tuple]):
  status, *rest = (arg,) if not isinstance(arg, tuple) else arg
  if not status.ok():
    raise status
  if len(rest) > 1:
    return rest
  elif len(rest) == 1:
    return rest[0]
