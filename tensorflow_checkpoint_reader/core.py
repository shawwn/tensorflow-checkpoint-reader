import struct

class StringPiece:
  npos = -1

  def __init__(self, data=None, size=None, offset=None):
    if data is None:
      self._ptr = bytearray()
      self._length = 0
      self._offset = 0
    elif isinstance(data, str):
      self._ptr = bytearray(data, 'utf-8')
      self._length = len(data)
      self._offset = 0
    elif isinstance(data, bytes):
      self._ptr = bytearray(data)
      self._length = len(data)
      self._offset = 0
    elif isinstance(data, bytearray):
      self._ptr = data
      self._length = len(data)
      self._offset = 0
    elif isinstance(data, StringPiece):
      self.set(data)
    if offset is not None:
      self.remove_prefix(offset)
    if size is not None:
      self.remove_suffix(len(self) - size)

  def data(self):
    return StringPiece(self._ptr, self._length, self._offset)

  def slice(self):
    return self._ptr[self._offset:self._offset + self._length]

  def set(self, other):
    self._ptr = other._ptr
    self._length = other._length
    self._offset = other._offset

  def at(self, pos: int):
    assert 0 <= pos < self._length
    return self._ptr[self._offset + pos]

  def __getitem__(self, item):
    return self.at(item)

  def length(self) -> int:
    """Returns the number of characters in the `string_view`."""
    return self._length

  def size(self) -> int:
    """Returns the number of characters in the `string_view`. Alias for `size()`."""
    return self.length()

  def empty(self) -> bool:
    """Checks if the `string_view` is empty (refers to no characters)."""
    return self._length <= 0

  def advance(self, n: int):
    if n < 0:
      if -n > self._offset:
        raise ValueError(f"Can't advance by {n}")
    elif n > 0:
      if n > self._length:
        raise ValueError(f"Can't advance by {n}")
    self._offset += n
    self._length -= n

  def remove_prefix(self, n: int):
    """Removes the first `n` characters from the `string_view`. Note that the
    underlying string is not changed, only the view."""
    if n > self._length or n < 0:
      raise ValueError(f"Can't remove {n} bytes")
    self._offset += n
    self._length -= n

  def remove_suffix(self, n: int):
    """Removes the last `n` characters from the `string_view`. Note that the
    underlying string is not changed, only the view."""
    if n > self._length or n < 0:
      raise ValueError(f"Can't remove {n} bytes")
    self._length -= n

  def find(self, target):
    return self.slice().find(string_view(target).slice())

  def rfind(self, target):
    return self.slice().rfind(string_view(target).slice())

  def substr(self, pos: int, n: int = npos):
    s = self.data()
    s.advance(pos)
    if n != StringPiece.npos:
      s.remove_suffix(len(s) - n)
    return s
    # s = self.slice()
    # if pos < 0:
    #   pos += len(s)
    # if n == StringPiece.npos:
    #   return s[pos:]
    # else:
    #   return s[pos:pos + n]

  def begin(self):
    return StringPiece(self._ptr, self._length, self._offset)

  def end(self):
    return StringPiece(self._ptr, 0, self._offset + self._length)

  def __bytes__(self):
    return bytes(self.slice())

  def __str__(self):
    return self.slice().decode('utf-8')

  def __repr__(self):
    return f"StringPiece({self.slice()!r})"

  def __len__(self):
    return self.length()

  def __add__(self, other):
    assert isinstance(other, int)
    r = StringPiece(self)
    r.advance(other)
    return r

  def __sub__(self, other):
    if isinstance(other, StringPiece):
      if other._ptr is not self._ptr:
        raise ValueError("Can only subtract pointers to same underlying data")
      return self._offset - other._offset
    r = StringPiece(self)
    r.advance(-other)
    return r


def string_view(data = None, length: int = None, offset: int = None) -> StringPiece:
  return StringPiece(data, length, offset)


class RandomAccessFile:
  def __init__(self, fp):
    self._fp = fp

  def read(self, offset, length):
    self._fp.seek(offset)
    data = self._fp.read(length)
    return StringPiece(data)


def get_varint_64(input: StringPiece):
  result = 0
  p = input.slice()
  i = 0
  for shift in range(0, 64, 7):
    byte = p[i]
    i += 1
    if byte & 128:
      # More bytes are present
      result |= ((byte & 127) << shift)
    else:
      result |= (byte << shift)
      input.remove_prefix(i)
      return True, result
  return False, None


def get_varint_32_ptr(data: bytes, p: int, limit: int):
  if p < limit:
    result = data[p]
    if (result & 128) == 0:
      value = result
      return p + 1, value
  return get_varint_32_ptr_fallback(data, p, limit)


def get_varint_32_ptr_fallback(data: bytes, p: int, limit: int):
  result = 0
  for shift in range(0, 29, 7):
    if p >= limit:
      break
    byte = data[p]
    p += 1
    if byte & 128:
      # More bytes are present
      result |= (byte & 127) << shift
    else:
      result |= byte << shift
      value = result
      return p, value
  return None, None


def decode_fixed_64(buffer, offset=0):
  return struct.unpack_from('<Q', buffer, offset=offset)[0]


def decode_fixed_32(buffer, offset=0):
  return struct.unpack_from('<L', buffer, offset=offset)[0]
