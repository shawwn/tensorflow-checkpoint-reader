from . import core

def consume_prefix(s: core.StringPiece, expected) -> bool:
  ex = core.string_view(expected)
  if not s.slice().startswith(ex.slice()):
    return False
  s.remove_prefix(ex.size())
  return True
