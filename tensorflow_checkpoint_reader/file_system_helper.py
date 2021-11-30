from . import port
from . import core
from . import io
from . import platform

from typing import Callable, List
from multiprocessing.pool import ThreadPool

kNumThreads = port.num_schedulable_cpus()

def for_each(first: int, last: int, f: Callable[[int], None]):
  """Run a function in parallel using a ThreadPool, but skip the ThreadPool
  on the iOS platform due to its problems with more than a few threads."""
  if platform.is_iphone_platform():
    for i in range(first, last):
      f(i)
  else:
    num_threads: int = min(kNumThreads, last - first)
    with ThreadPool(num_threads) as threads:
      for i in range(first, last):
        threads.apply(f, args=(i,))


# A globbing pattern can only start with these characters:
kGlobbingChars = "*?[\\"

def is_globbing_pattern(pattern: bytes) -> bool:
  return core.string_view(pattern).find_first_of(kGlobbingChars) != core.StringPiece.npos

def patch_pattern(pattern) -> bytes:
  """Make sure that the first entry in `dirs` during glob expansion does not
  contain a glob pattern. This is to prevent a corner-case bug where
  `<pattern>` would be treated differently than `./<pattern>`."""
  pat = core.string_view(pattern)
  fixed_prefix = pat.substr(0, pat.find_first_of(kGlobbingChars))
  # Patching is needed when there is no directory part in `prefix`
  if io.dirname(fixed_prefix).empty():
    return io.join_path(".", pat)
  # No patching needed
  return pat.bytes()

def all_directory_prefixes(d) -> List[bytes]:
  d = core.string_view(d)
  dirs = []
  patched = patch_pattern(d)
  dir = core.StringPiece(patched)
  # If the pattern ends with a `/` (or `\\` on Windows), we need to strip it
  # otherwise we would have one additional matching step and the result set
  # would be empty.
  is_directory = d[d.size() - 1] == b'/'[0]
  if platform.is_windows_platform():
    is_directory = is_directory or (d[d.size() - 1] == b'\\'[0])
  if is_directory:
    dir = io.dirname(dir)
  while not dir.empty():
    dirs.append(dir.bytes())
    new_dir = io.dirname(dir)
    # io::Dirname("/") returns "/" so we need to break the loop.
    # On Windows, io::Dirname("C:\\") would return "C:\\", so we check for
    # identity of the result instead of checking for dir[0] == `/`.
    if dir.slice() == new_dir.slice():
      break
    dir = new_dir
  # Order the array from parent to ancestor (reverse order).
  dirs = list(reversed(dirs))
  return dirs

def get_first_globbing_entry(dirs: List[bytes]) -> int:
  i = 0
  for d in dirs:
    if is_globbing_pattern(d):
      break
    i += 1
  return i



