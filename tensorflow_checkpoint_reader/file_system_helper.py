from __future__ import annotations

from . import port
from . import core
from . import io
from . import platform
from . import errors

from typing import Callable, List, Tuple, Optional, TYPE_CHECKING
from multiprocessing.pool import ThreadPool
import collections
import threading

if TYPE_CHECKING:
  from . import file_system
  from . import env

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

# Status GetMatchingPaths(FileSystem* fs, Env* env, const string& pattern,
#                         std::vector<string>* results) {
def get_matching_paths(fs: file_system.FileSystem, env: env.Env, pattern) -> Tuple[errors.Status, Optional[List]]:
  # // Check that `fs`, `env` and `results` are non-null.
  # if (fs == nullptr || env == nullptr || results == nullptr) {
  #   return Status(tensorflow::error::INVALID_ARGUMENT,
  #                 "Filesystem calls GetMatchingPaths with nullptr arguments");
  # }
  if fs is None or env is None:
    return errors.InvalidArgument("Filesystem calls GetMatchingPaths with nullptr arguments"), None

  # // By design, we don't match anything on empty pattern
  # results->clear();
  results = []
  # if (pattern.empty()) {
  #   return Status::OK();
  # }
  if len(pattern) <= 0:
    return errors.Status.OK(), results

  # // The pattern can contain globbing characters at multiple levels, e.g.:
  # //
  # //   foo/ba?/baz/f*r
  # //
  # // To match the full pattern, we must match every prefix subpattern and then
  # // operate on the children for each match. Thus, we separate all subpatterns
  # // in the `dirs` vector below.
  # std::vector<std::string> dirs = AllDirectoryPrefixes(pattern);
  dirs = all_directory_prefixes(pattern)

  # // We can have patterns that have several parents where no globbing is being
  # // done, for example, `foo/bar/baz/*`. We don't need to expand the directories
  # // which don't contain the globbing characters.
  # int matching_index = GetFirstGlobbingEntry(dirs);
  matching_index = get_first_globbing_entry(dirs)

  # // If we don't have globbing characters in the pattern then it specifies a
  # // path in the filesystem. We add it to the result set if it exists.
  # if (matching_index == dirs.size()) {
  #   if (fs->FileExists(pattern).ok()) {
  #     results->emplace_back(pattern);
  #   }
  #   return Status::OK();
  # }
  if matching_index == len(dirs):
    if fs.file_exists(pattern).ok():
      results.append(pattern)
    return errors.Status.OK(), results

  # // To expand the globbing, we do a BFS from `dirs[matching_index-1]`.
  # // At every step, we work on a pair `{dir, ix}` such that `dir` is a real
  # // directory, `ix < dirs.size() - 1` and `dirs[ix+1]` is a globbing pattern.
  # // To expand the pattern, we select from all the children of `dir` only those
  # // that match against `dirs[ix+1]`.
  # // If there are more entries in `dirs` after `dirs[ix+1]` this mean we have
  # // more patterns to match. So, we add to the queue only those children that
  # // are also directories, paired with `ix+1`.
  # // If there are no more entries in `dirs`, we return all children as part of
  # // the answer.
  # // Since we can get into a combinatorial explosion issue (e.g., pattern
  # // `/*/*/*`), we process the queue in parallel. Each parallel processing takes
  # // elements from `expand_queue` and adds them to `next_expand_queue`, after
  # // which we swap these two queues (similar to double buffering algorithms).
  # // PRECONDITION: `IsGlobbingPattern(dirs[0]) == false`
  # // PRECONDITION: `matching_index > 0`
  # // INVARIANT: If `{d, ix}` is in queue, then `d` and `dirs[ix]` are at the
  # //            same level in the filesystem tree.
  # // INVARIANT: If `{d, _}` is in queue, then `IsGlobbingPattern(d) == false`.
  # // INVARIANT: If `{d, _}` is in queue, then `d` is a real directory.
  # // INVARIANT: If `{_, ix}` is in queue, then `ix < dirs.size() - 1`.
  # // INVARIANT: If `{_, ix}` is in queue, `IsGlobbingPattern(dirs[ix + 1])`.
  # std::deque<std::pair<string, int>> expand_queue;
  expand_queue = collections.deque()
  # std::deque<std::pair<string, int>> next_expand_queue;
  next_expand_queue = collections.deque()
  # expand_queue.emplace_back(dirs[matching_index - 1], matching_index - 1);
  expand_queue.append((dirs[matching_index - 1], matching_index - 1))
  #
  # // Adding to `result` or `new_expand_queue` need to be protected by mutexes
  # // since there are multiple threads writing to these.
  # mutex result_mutex;
  result_mutex = threading.RLock()
  # mutex queue_mutex;
  queue_mutex = threading.RLock()
  #
  # while (!expand_queue.empty()) {
  while len(expand_queue) > 0:
    # next_expand_queue.clear();
    next_expand_queue.clear()
    #
    # // The work item for every item in `expand_queue`.
    # // pattern, we process them in parallel.
    # auto handle_level = [&fs, &results, &dirs, &expand_queue,
    #                      &next_expand_queue, &result_mutex,
    #                      &queue_mutex](int i) {
    def handle_level(i):
      # // See invariants above, all of these are valid accesses.
      # const auto& queue_item = expand_queue.at(i);
      queue_item = expand_queue[i]
      # const std::string& parent = queue_item.first;
      parent: bytes = queue_item[0]
      # const int index = queue_item.second + 1;
      index: int = queue_item[1] + 1
      # const std::string& match_pattern = dirs[index];
      match_pattern = dirs[index]
      #
      # // Get all children of `parent`. If this fails, return early.
      # std::vector<std::string> children;
      # Status s = fs->GetChildren(parent, &children);
      s, children = fs.get_children(parent)
      # if (s.code() == tensorflow::error::PERMISSION_DENIED) {
      #   return;
      # }
      if errors.is_permission_denied(s):
        return
      #
      # // Also return early if we don't have any children
      # if (children.empty()) {
      #   return;
      # }
      if len(children) <= 0:
        return
      #
      # // Since we can get extremely many children here and on some filesystems
      # // `IsDirectory` is expensive, we process the children in parallel.
      # // We also check that children match the pattern in parallel, for speedup.
      # // We store the status of the match and `IsDirectory` in
      # // `children_status` array, one element for each children.
      # std::vector<Status> children_status(children.size());
      children_status = [errors.Status.OK() for _ in range(len(children))]
      # auto handle_children = [&fs, &match_pattern, &parent, &children,
      #                         &children_status](int j) {
      def handle_children(j: int):
        # const std::string path = io::JoinPath(parent, children[j]);
        path = io.join_path(parent, children[j])
        # if (!fs->Match(path, match_pattern)) {
        if not fs.match(path, match_pattern):
          # children_status[j] =
          #     Status(tensorflow::error::CANCELLED, "Operation not needed");
          children_status[j] = errors.Status(errors.error.CANCELLED, "Operation not needed")
        # } else {
        else:
          # children_status[j] = fs->IsDirectory(path);
          children_status[j] = fs.is_directory(path)
        # }
      # };
      # ForEach(0, children.size(), handle_children);
      for_each(0, len(children), handle_children)
      #
      # // At this point, pairing `children` with `children_status` will tell us
      # // if a children:
      # //   * does not match the pattern
      # //   * matches the pattern and is a directory
      # //   * matches the pattern and is not a directory
      # // We fully ignore the first case.
      # // If we matched the last pattern (`index == dirs.size() - 1`) then all
      # // remaining children get added to the result.
      # // Otherwise, only the directories get added to the next queue.
      # for (size_t j = 0; j < children.size(); j++) {
      for j in range(len(children)):
        # if (children_status[j].code() == tensorflow::error::CANCELLED) {
        #   continue;
        # }
        if children_status[j].code() == errors.error.CANCELLED:
          continue
        #
        # const std::string path = io::JoinPath(parent, children[j]);
        path = io.join_path(parent, children[j])
        # if (index == dirs.size() - 1) {
        if index == len(dirs) - 1:
          # mutex_lock l(result_mutex);
          with result_mutex:
            # results->emplace_back(path);
            results.append(path)
        # } else if (children_status[j].ok()) {
        elif children_status[j].ok():
          # mutex_lock l(queue_mutex);
          with queue_mutex:
            # next_expand_queue.emplace_back(path, index);
            next_expand_queue.append((path, index))
        # }
      # }
    # };
    # ForEach(0, expand_queue.size(), handle_level);
    for_each(0, len(expand_queue), handle_level)
    #
    # // After evaluating one level, swap the "buffers"
    # std::swap(expand_queue, next_expand_queue);
    expand_queue, next_expand_queue = next_expand_queue, expand_queue
  # }
  #
  # return Status::OK();
  return errors.Status.OK(), results
# }


