import struct
import numpy as np
from . import strings

# namespace tensorflow {
# namespace core {

# void EncodeFixed16(char* buf, uint16 value) {
#   if (port::kLittleEndian) {
#     memcpy(buf, &value, sizeof(value));
#   } else {
#     buf[0] = value & 0xff;
#     buf[1] = (value >> 8) & 0xff;
#   }
# }
def encode_fixed16(value):
  value = int(np.uint16(value))
  return struct.pack("=H", value)

# void EncodeFixed32(char* buf, uint32 value) {
#   if (port::kLittleEndian) {
#     memcpy(buf, &value, sizeof(value));
#   } else {
#     buf[0] = value & 0xff;
#     buf[1] = (value >> 8) & 0xff;
#     buf[2] = (value >> 16) & 0xff;
#     buf[3] = (value >> 24) & 0xff;
#   }
# }
def encode_fixed32(value):
  value = int(np.uint32(value))
  return struct.pack("=L", value)

# void EncodeFixed64(char* buf, uint64 value) {
#   if (port::kLittleEndian) {
#     memcpy(buf, &value, sizeof(value));
#   } else {
#     buf[0] = value & 0xff;
#     buf[1] = (value >> 8) & 0xff;
#     buf[2] = (value >> 16) & 0xff;
#     buf[3] = (value >> 24) & 0xff;
#     buf[4] = (value >> 32) & 0xff;
#     buf[5] = (value >> 40) & 0xff;
#     buf[6] = (value >> 48) & 0xff;
#     buf[7] = (value >> 56) & 0xff;
#   }
# }
def encode_fixed64(value):
  value = int(np.uint64(value))
  return struct.pack("=Q", value)

# void PutFixed16(string* dst, uint16 value) {
#   char buf[sizeof(value)];
#   EncodeFixed16(buf, value);
#   dst->append(buf, sizeof(buf));
# }
def put_fixed16(dst: bytearray, value):
  buf = encode_fixed16(value)
  dst.extend(buf)

# void PutFixed32(string* dst, uint32 value) {
#   char buf[sizeof(value)];
#   EncodeFixed32(buf, value);
#   dst->append(buf, sizeof(buf));
# }
def put_fixed32(dst: bytearray, value):
  buf = encode_fixed32(value)
  dst.extend(buf)

# void PutFixed64(string* dst, uint64 value) {
#   char buf[sizeof(value)];
#   EncodeFixed64(buf, value);
#   dst->append(buf, sizeof(buf));
# }
def put_fixed64(dst: bytearray, value):
  buf = encode_fixed64(value)
  dst.extend(buf)

# char* EncodeVarint32(char* dst, uint32 v) {
#   // Operate on characters as unsigneds
#   unsigned char* ptr = reinterpret_cast<unsigned char*>(dst);
#   static const int B = 128;
#   if (v < (1 << 7)) {
#     *(ptr++) = v;
#   } else if (v < (1 << 14)) {
#     *(ptr++) = v | B;
#     *(ptr++) = v >> 7;
#   } else if (v < (1 << 21)) {
#     *(ptr++) = v | B;
#     *(ptr++) = (v >> 7) | B;
#     *(ptr++) = v >> 14;
#   } else if (v < (1 << 28)) {
#     *(ptr++) = v | B;
#     *(ptr++) = (v >> 7) | B;
#     *(ptr++) = (v >> 14) | B;
#     *(ptr++) = v >> 21;
#   } else {
#     *(ptr++) = v | B;
#     *(ptr++) = (v >> 7) | B;
#     *(ptr++) = (v >> 14) | B;
#     *(ptr++) = (v >> 21) | B;
#     *(ptr++) = v >> 28;
#   }
#   return reinterpret_cast<char*>(ptr);
# }
def encode_varint32(v):
  v = int(np.uint32(v))
  ptr = bytearray()
  def add(i):
    ptr.append(int(i) & 0xFF)
  B = 128
  # if (v < (1 << 7)) {
  #   *(ptr++) = v;
  if v < (1 << 7):
    ptr.append(v)
  # } else if (v < (1 << 14)) {
  #   *(ptr++) = v | B;
  #   *(ptr++) = v >> 7;
  elif v < (1 << 14):
    add(v | B)
    add(v >> 7)
  # } else if (v < (1 << 21)) {
  #   *(ptr++) = v | B;
  #   *(ptr++) = (v >> 7) | B;
  #   *(ptr++) = v >> 14;
  elif v < (1 << 21):
    add(v | B)
    add((v >> 7) | B)
    add(v >> 14)
  # } else if (v < (1 << 28)) {
  #   *(ptr++) = v | B;
  #   *(ptr++) = (v >> 7) | B;
  #   *(ptr++) = (v >> 14) | B;
  #   *(ptr++) = v >> 21;
  elif v < (1 << 28):
    add(v | B)
    add((v >> 7) | B)
    add((v >> 14) | B)
    add(v >> 21)
  # } else {
  #   *(ptr++) = v | B;
  #   *(ptr++) = (v >> 7) | B;
  #   *(ptr++) = (v >> 14) | B;
  #   *(ptr++) = (v >> 21) | B;
  #   *(ptr++) = v >> 28;
  # }
  else:
    add(v | B)
    add((v >> 7) | B)
    add((v >> 14) | B)
    add((v >> 21) | B)
    add(v >> 28)
  return ptr

# void PutVarint32(string* dst, uint32 v) {
#   char buf[5];
#   char* ptr = EncodeVarint32(buf, v);
#   dst->append(buf, ptr - buf);
# }
def put_varint32(dst: bytearray, v):
  buf = encode_varint32(v)
  dst.extend(buf)

# char* EncodeVarint64(char* dst, uint64 v) {
#   static const int B = 128;
#   unsigned char* ptr = reinterpret_cast<unsigned char*>(dst);
#   while (v >= B) {
#     *(ptr++) = (v & (B - 1)) | B;
#     v >>= 7;
#   }
#   *(ptr++) = static_cast<unsigned char>(v);
#   return reinterpret_cast<char*>(ptr);
# }
def encode_varint64(v):
  v = int(np.uint64(v))
  B = 128
  ptr = bytearray()
  def add(i):
    ptr.append(int(i) & 0xFF)
  while v >= B:
    add((v & (B - 1)) | B)
    v >>= 7
  add(v)
  return ptr

# void PutVarint64(string* dst, uint64 v) {
#   char buf[10];
#   char* ptr = EncodeVarint64(buf, v);
#   dst->append(buf, ptr - buf);
# }
def put_varint64(dst: bytearray, v):
  buf = encode_varint64(v)
  dst.extend(buf)

# void PutVarint64(tstring* dst, uint64 v) {
#   char buf[10];
#   char* ptr = EncodeVarint64(buf, v);
#   dst->append(buf, ptr - buf);
# }

# int VarintLength(uint64_t v) {
#   int len = 1;
#   while (v >= 128) {
#     v >>= 7;
#     len++;
#   }
#   return len;
# }
def varint_length(v):
  v = int(np.uint64(v))
  length = 1
  while v >= 128:
    v >>= 7
    length += 1
  return length

# const char* GetVarint32Ptr(const char* p, const char* limit, uint32* value) {
#   if (p < limit) {
#     uint32 result = *(reinterpret_cast<const unsigned char*>(p));
#     if ((result & 128) == 0) {
#       *value = result;
#       return p + 1;
#     }
#   }
#   return GetVarint32PtrFallback(p, limit, value);
# }
#
# const char* GetVarint32PtrFallback(const char* p, const char* limit,
#                                    uint32* value) {
#   uint32 result = 0;
#   for (uint32 shift = 0; shift <= 28 && p < limit; shift += 7) {
#     uint32 byte = *(reinterpret_cast<const unsigned char*>(p));
#     p++;
#     if (byte & 128) {
#       // More bytes are present
#       result |= ((byte & 127) << shift);
#     } else {
#       result |= (byte << shift);
#       *value = result;
#       return reinterpret_cast<const char*>(p);
#     }
#   }
#   return nullptr;
# }
#
# bool GetVarint32(StringPiece* input, uint32* value) {
#   const char* p = input->data();
#   const char* limit = p + input->size();
#   const char* q = GetVarint32Ptr(p, limit, value);
#   if (q == nullptr) {
#     return false;
#   } else {
#     *input = StringPiece(q, limit - q);
#     return true;
#   }
# }
#
# const char* GetVarint64Ptr(const char* p, const char* limit, uint64* value) {
#   uint64 result = 0;
#   for (uint32 shift = 0; shift <= 63 && p < limit; shift += 7) {
#     uint64 byte = *(reinterpret_cast<const unsigned char*>(p));
#     p++;
#     if (byte & 128) {
#       // More bytes are present
#       result |= ((byte & 127) << shift);
#     } else {
#       result |= (byte << shift);
#       *value = result;
#       return reinterpret_cast<const char*>(p);
#     }
#   }
#   return nullptr;
# }
#
# bool GetVarint64(StringPiece* input, uint64* value) {
#   const char* p = input->data();
#   const char* limit = p + input->size();
#   const char* q = GetVarint64Ptr(p, limit, value);
#   if (q == nullptr) {
#     return false;
#   } else {
#     *input = StringPiece(q, limit - q);
#     return true;
#   }
# }
#
# }  // namespace core
# }  // namespace tensorflow