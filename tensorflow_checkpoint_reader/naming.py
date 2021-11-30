from . import strings
from . import core

def meta_filename(prefix) -> bytes:
  prefix = core.string_view(prefix)
  return strings.printf(b"%.*s.index", prefix.size(), prefix.bytes())

def data_filename(prefix, shard_id: int, num_shards: int) -> bytes:
  assert num_shards > 0
  assert 0 <= shard_id < num_shards
  prefix = core.string_view(prefix)
  return strings.printf(b"%.*s.data-%05d-of-%05d", prefix.size(), prefix.bytes(), shard_id, num_shards)