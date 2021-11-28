from . import core

class Iterator:
  def valid(self) -> bool:
    """An iterator is either positioned at a key/value pair, or
    not valid.  This method returns true iff the iterator is valid."""
    raise NotImplementedError()

  def seek_to_first(self):
    """Position at the first key in the source.The iterator is Valid()
    after this call iff the source is not empty."""
    raise NotImplementedError()

  def seek(self, target: core.StringPiece):
    """Position at the first key in the source that is at or past target.
    The iterator is Valid() after this call iff the source contains
    an entry that comes at or past target."""
    raise NotImplementedError()

  def next(self):
    """Moves to the next entry in the source.  After this call, Valid() is
    true iff the iterator was not positioned at the last entry in the source.
    REQUIRES: Valid()"""
    raise NotImplementedError()

  def key(self) -> core.StringPiece:
    """Return the key for the current entry.  The underlying storage for
    the returned slice is valid only until the next modification of
    the iterator.
    REQUIRES: Valid()"""
    raise NotImplementedError()

  def value(self) -> core.StringPiece:
    """Return the value for the current entry.  The underlying storage for
    the returned slice is valid only until the next modification of
    the iterator.
    REQUIRES: Valid()"""
    raise NotImplementedError()

  def status(self):
    """If an error has occurred, raise it"""


class EmptyIterator(Iterator):
  def __init__(self, status = None):
    self._status = status

  def valid(self):
    return False

  def seek(self, target: core.StringPiece):
    pass

  def seek_to_first(self):
    pass

  def next(self):
    assert False

  def key(self) -> core.StringPiece:
    assert False
    return core.StringPiece()

  def value(self) -> core.StringPiece:
    assert False
    return core.StringPiece()

def status(self):
  if self._status is not None:
    raise self._status

def new_empty_iterator() -> Iterator:
  return EmptyIterator()

def new_error_iterator(status) -> Iterator:
  return EmptyIterator(status)