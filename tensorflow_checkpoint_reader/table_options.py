import enum
import dataclasses

class Cache:
  def __init__(self):
    raise NotImplementedError

# // DB contents are stored in a set of blocks, each of which holds a
# // sequence of key,value pairs.  Each block may be compressed before
# // being stored in a file.  The following enum describes which
# // compression method (if any) is used to compress a block.
# enum CompressionType {
#   // NOTE: do not change the values of existing entries, as these are
#   // part of the persistent format on disk.
#   kNoCompression = 0x0,
#   kSnappyCompression = 0x1
# };
class CompressionType(enum.IntEnum):
  kNoCompression = 0x0
  kSnappyCompression = 0x1
kNoCompression = CompressionType.kNoCompression
kSnappyCompression = CompressionType.kSnappyCompression

# // Options to control the behavior of a table (passed to Table::Open)
# struct Options {
#   // Approximate size of user data packed per block.  Note that the
#   // block size specified here corresponds to uncompressed data.  The
#   // actual size of the unit read from disk may be smaller if
#   // compression is enabled.  This parameter can be changed dynamically.
#   size_t block_size = 262144;
#
#   // Number of keys between restart points for delta encoding of keys.
#   // This parameter can be changed dynamically.  Most clients should
#   // leave this parameter alone.
#   int block_restart_interval = 16;
#
#   // Compress blocks using the specified compression algorithm.  This
#   // parameter can be changed dynamically.
#   //
#   // Default: kSnappyCompression, which gives lightweight but fast
#   // compression.
#   //
#   // Typical speeds of kSnappyCompression on an Intel(R) Core(TM)2 2.4GHz:
#   //    ~200-500MB/s compression
#   //    ~400-800MB/s decompression
#   // Note that these speeds are significantly faster than most
#   // persistent storage speeds, and therefore it is typically never
#   // worth switching to kNoCompression.  Even if the input data is
#   // incompressible, the kSnappyCompression implementation will
#   // efficiently detect that and will switch to uncompressed mode.
#   CompressionType compression = kSnappyCompression;
#
#   // Control over blocks (user data is stored in a set of blocks, and
#   // a block is the unit of reading from disk).
#
#   // If non-null, use the specified cache for blocks.
#   Cache* block_cache = nullptr;
# };

@dataclasses.dataclass
class Options:
  # Approximate size of user data packed per block.  Note that the
  # block size specified here corresponds to uncompressed data.  The
  # actual size of the unit read from disk may be smaller if
  # compression is enabled.  This parameter can be changed dynamically.
  block_size: int = 262144

  # Number of keys between restart points for delta encoding of keys.
  # This parameter can be changed dynamically.  Most clients should
  # leave this parameter alone.
  block_restart_interval: int = 16

  # Compress blocks using the specified compression algorithm.  This
  # parameter can be changed dynamically.
  #
  # Default: kSnappyCompression, which gives lightweight but fast
  # compression.
  #
  # Typical speeds of kSnappyCompression on an Intel(R) Core(TM)2 2.4GHz:
  #    ~200-500MB/s compression
  #    ~400-800MB/s decompression
  # Note that these speeds are significantly faster than most
  # persistent storage speeds, and therefore it is typically never
  # worth switching to kNoCompression.  Even if the input data is
  # incompressible, the kSnappyCompression implementation will
  # efficiently detect that and will switch to uncompressed mode.
  compression: CompressionType = kSnappyCompression

  # Control over blocks (user data is stored in a set of blocks, and
  # a block is the unit of reading from disk).
  #
  # If non-null, use the specified cache for blocks.
  block_cache: Cache = None
