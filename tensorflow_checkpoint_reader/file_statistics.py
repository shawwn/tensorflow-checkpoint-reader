from dataclasses import dataclass

@dataclass
class FileStatistics:
  # The length of the file or -1 if finding file length is not supported.
  length: int = -1
  # The last modified time in nanoseconds.
  mtime_nsec: int = 0
  # True if the file is a directory, otherwise false.
  is_directory: bool = False
