from .pb.tensorflow.core.protobuf import error_codes_pb2 as error
from . import core, strings
from typing import Union, NamedTuple, Tuple, Any

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


def raise_if_error(arg: Union[Status, Tuple]):
  status, *rest = (arg,) if not isinstance(arg, tuple) else arg
  if not status.ok():
    raise status
  if len(rest) > 1:
    return rest
  elif len(rest) == 1:
    return rest[0]
