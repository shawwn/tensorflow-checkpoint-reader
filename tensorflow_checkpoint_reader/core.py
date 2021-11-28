import struct

class StringPiece:
  def __init__(self, data=None, size=None, offset=0):
    if data is None:
      data = b''
    self._data = data
    if size is None:
      size = len(data)
    self._size = size
    self._offset = offset

  @property
  def data(self):
    return self._data[self._offset:self._offset + self._size]

  @property
  def size(self):
    return self._size

  @property
  def offset(self):
    return self._offset

  def set(self, other):
    self._data = other._data
    self._size = other._size
    self._offset = other._offset

  def advance(self, n):
    if n > self._size:
      raise ValueError(f"Can't advance by {n} bytes")
    self._offset += n
    self._size -= n


class RandomAccessFile:
  def __init__(self, fp):
    self._fp = fp

  def read(self, offset, length):
    self._fp.seek(offset)
    data = self._fp.read(length)
    return StringPiece(data)


def get_varint_64(input: StringPiece):
  result = 0
  p = input.data
  i = 0
  for shift in range(0, 64, 7):
    byte = p[i]
    i += 1
    if byte & 128:
      # More bytes are present
      result |= ((byte & 127) << shift)
    else:
      result |= (byte << shift)
      input.advance(i)
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
