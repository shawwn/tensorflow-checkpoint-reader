import time as _time

class EnvTime:
  """An interface used by the implementation to
  access timer related operations."""
  kMicrosToPicos: int = 1000 * 1000
  kMicrosToNanos: int = 1000
  kMillisToMicros: int = 1000
  kMillisToNanos: int = 1000 * 1000
  kNanosToPicos: int = 1000
  kSecondsToMillis: int = 1000
  kSecondsToMicros: int = 1000 * 1000
  kSecondsToNanos: int = 1000 * 1000 * 1000

  @classmethod
  def now_nanos(cls) -> int:
    """Returns the number of nano-seconds since the Unix epoch."""
    return _time.time_ns()

  @classmethod
  def now_micros(cls) -> int:
    """Returns the number of micro-seconds since the Unix epoch."""
    return cls.now_nanos() // cls.kMicrosToNanos

  @classmethod
  def now_seconds(cls) -> int:
    """Returns the number of seconds since the Unix epoch."""
    return cls.now_nanos() // cls.kSecondsToNanos
