from . import core
from . import strings
from . import port

Char = strings.Scanner.CharClass

kPathSep = b"/"

def join_path(*paths: core.StringPiece):
  result = b''
  for path in paths:
    path = core.string_view(path)
    if path.empty():
      continue

    if len(result) <= 0:
      result = path.slice()
      continue
    
    if is_absolute_path(path):
      path = path.substr(1)

    if result[-1] == kPathSep[0]:
      result += path.slice()
    else:
      result += kPathSep
      result += path.slice()
  return result

def split_path(uri: core.StringPiece):
  """Return the parts of the URI, split on the final "/" in the path. If there is
  no "/" in the path, the first part of the output is the scheme and host, and
  the second is the path. If the only "/" in the path is the first character,
  it is included in the first part of the output."""
  uri = core.string_view(uri)
  scheme, host, path = parse_uri(uri)
  pos = path.rfind('/')
  if port.is_windows_platform():
    if pos == core.StringPiece.npos:
      pos = path.rfind('\\')
  # Handle the case with no '/' in 'path'.
  if pos == core.StringPiece.npos:
    return (core.StringPiece(uri.begin(), host.end() - uri.begin()),
            path)
  # Handle the case with a single leading '/' in 'path'.
  if pos == 0:
    return (core.StringPiece(uri.begin(), path.begin() + 1 - uri.begin()),
            core.StringPiece(path.data() + 1, path.size() - 1))

  return (core.StringPiece(uri.begin(), path.begin() + pos - uri.begin()),
          core.StringPiece(path.data() + pos + 1, path.size() - (pos + 1)))


def split_basename(path: core.StringPiece):
  """Return the parts of the basename of path, split on the final ".".
  If there is no "." in the basename or "." is the final character in the
  basename, the second value will be empty."""
  path = basename(path)
  pos = path.rfind('.')
  if pos == core.StringPiece.npos:
    return (path,
            core.StringPiece(path.data() + path.size(), 0))
  return (core.StringPiece(path.data(), pos),
          core.StringPiece(path.data() + pos + 1, path.size() - (pos + 1)))

def is_absolute_path(path: core.StringPiece):
  path = core.string_view(path)
  return not path.empty() and path[0] == strings.Ascii.SLASH

def dirname(path: core.StringPiece):
  return split_path(path)[0]

def basename(path: core.StringPiece):
  return split_path(path)[1]

def extension(path: core.StringPiece):
  return split_basename(path)[1]

def clean_path(path: core.StringPiece):
  raise NotImplementedError()

def parse_uri(remaining: core.StringPiece):
  remaining = core.string_view(remaining)
  scheme = core.string_view()
  host = core.string_view()
  path = core.string_view()
  # 0. Parse scheme
  # Make sure scheme matches [a-zA-Z][0-9a-zA-Z.]*
  # TODO(keveman): Allow "+" and "-" in the scheme.
  # Keep URI pattern in TensorBoard's `_parse_event_files_spec` updated
  # accordingly
  if not strings.Scanner(remaining) \
          .one(Char.LETTER) \
          .many(Char.LETTER_DIGIT_DOT) \
          .stop_capture() \
          .one_literal("://") \
          .get_result(remaining, scheme):
    # If there's no scheme, assume the entire string is a path.
    scheme.set(core.StringPiece(remaining.begin(), 0))
    host.set(core.StringPiece(remaining.begin(), 0))
    path.set(remaining)
    return scheme, host, path

  # 1. Parse host
  if not strings.Scanner(remaining) \
    .scan_until(strings.Ascii.SLASH) \
    .get_result(remaining, host):
    # No path, so the rest of the URI is the host
    host.set(remaining)
    path.set(core.StringPiece(remaining.begin(), 0))
    return scheme, host, path

  # 2. The rest is the path
  path.set(remaining)
  return scheme, host, path


def create_uri(scheme: core.StringPiece, host: core.StringPiece, path: core.StringPiece):
  scheme = core.string_view(scheme)
  if scheme.empty():
    return str(path)
  return strings.str_cat(scheme, "://", host, path)