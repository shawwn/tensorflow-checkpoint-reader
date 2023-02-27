from . import table_options
import numpy as np

from typing import List

#import tensorflow_checkpoint_reader.core as core
from . import core
from . import coding
from . import strings

class BlockBuilder:
  #  // Reset the contents as if the BlockBuilder was just constructed.
  #  void Reset();
  #
  #  // REQUIRES: Finish() has not been called since the last call to Reset().
  #  // REQUIRES: key is larger than any previously added key
  #  void Add(const StringPiece& key, const StringPiece& value);
  #
  #  // Finish building the block and return a slice that refers to the
  #  // block contents.  The returned slice will remain valid for the
  #  // lifetime of this builder or until Reset() is called.
  #  StringPiece Finish();
  #
  #  // Returns an estimate of the current (uncompressed) size of the block
  #  // we are building.
  #  size_t CurrentSizeEstimate() const;
  #
  #  // Return true iff no entries have been added since the last Reset()
  #  bool empty() const { return buffer_.empty(); }
  #
  # private:
  #  const Options* options_;
  #  string buffer_;                 // Destination buffer
  #  std::vector<uint32> restarts_;  // Restart points
  #  int counter_;                   // Number of entries emitted since restart
  #  bool finished_;                 // Has Finish() been called?
  #  string last_key_;
  #
  #  // No copying allowed
  #  BlockBuilder(const BlockBuilder&);
  #  void operator=(const BlockBuilder&);


  # namespace tensorflow {
  # namespace table {
  #
  # BlockBuilder::BlockBuilder(const Options* options)
  #     : options_(options), restarts_(), counter_(0), finished_(false) {
  #   assert(options->block_restart_interval >= 1);
  #   restarts_.push_back(0);  // First restart point is at offset 0
  # }

  restarts_: List[int]

  def __init__(self, options: table_options.Options):
    self.options_ = options
    self.buffer_ = bytearray() # Destination buffer
    self.restarts_ = []
    self.counter_ = 0
    self.finished_ = False
    self.last_key_ = bytearray()
    assert options.block_restart_interval >= 1
    self.restarts_.append(0) # First restart point is at offset 0

  # void BlockBuilder::Reset() {
  #   buffer_.clear();
  #   restarts_.clear();
  #   restarts_.push_back(0);  // First restart point is at offset 0
  #   counter_ = 0;
  #   finished_ = false;
  #   last_key_.clear();
  # }
  def reset(self):
    """Reset the contents as if the BlockBuilder was just constructed."""
    self.buffer_.clear()
    self.restarts_.clear()
    self.restarts_.append(0) # First restart point is at offset 0
    self.counter_ = 0
    self.finished_ = False
    self.last_key_.clear()

  # size_t BlockBuilder::CurrentSizeEstimate() const {
  #   return (buffer_.size() +                     // Raw data buffer
  #           restarts_.size() * sizeof(uint32) +  // Restart array
  #           sizeof(uint32));                     // Restart array length
  # }
  def current_size_estimate(self):
    return (len(self.buffer_) +        # Raw data buffer
            len(self.restarts_) * 4 +  # Restart array
            4                          # Restart array length
            )


  def empty(self):
    """Return true iff no entries have been added since the last Reset()"""
    return len(self.buffer_) <= 0

  # StringPiece BlockBuilder::Finish() {
  #   // Append restart array
  #   CHECK_LE(restarts_.size(), std::numeric_limits<uint32_t>::max());
  #   for (const auto r : restarts_) {
  #     core::PutFixed32(&buffer_, r);
  #   }
  #   // Downcast safe because of the CHECK.
  #   core::PutFixed32(&buffer_, static_cast<uint32_t>(restarts_.size()));
  #   finished_ = true;
  #   return StringPiece(buffer_);
  # }
  def finish(self):
    """Finish building the block and return a slice that refers to the
    block contents.  The returned slice will remain valid for the
    lifetime of this builder or until Reset() is called.
    """
    # Append restart array
    # CHECK_LE(restarts_.size(), std::numeric_limits<uint32_t>::max());
    assert len(self.restarts_) <= np.iinfo(np.uint32).max
    # for (const auto r : restarts_) {
    #   core::PutFixed32(&buffer_, r);
    # }
    for r in self.restarts_:
      coding.put_fixed32(self.buffer_, r)
    # // Downcast safe because of the CHECK.
    # core::PutFixed32(&buffer_, static_cast<uint32_t>(restarts_.size()));
    coding.put_fixed32(self.buffer_, np.uint32(len(self.restarts_)))
    # finished_ = true;
    self.finished_ = True
    # return StringPiece(buffer_);
    return core.StringPiece(self.buffer_)

  # void BlockBuilder::Add(const StringPiece& key, const StringPiece& value) {
  #   StringPiece last_key_piece(last_key_);
  #   assert(!finished_);
  #   assert(counter_ <= options_->block_restart_interval);
  #   assert(buffer_.empty()  // No values yet?
  #          || key.compare(last_key_piece) > 0);
  #   size_t shared = 0;
  #   if (counter_ < options_->block_restart_interval) {
  #     // See how much sharing to do with previous string
  #     const size_t min_length = std::min(last_key_piece.size(), key.size());
  #     while ((shared < min_length) && (last_key_piece[shared] == key[shared])) {
  #       shared++;
  #     }
  #   } else {
  #     // Restart compression
  #     CHECK_LE(buffer_.size(), std::numeric_limits<uint32_t>::max());
  #     restarts_.push_back(static_cast<uint32_t>(buffer_.size()));
  #     counter_ = 0;
  #   }
  #   const size_t non_shared = key.size() - shared;
  #
  #   CHECK_LE(shared, std::numeric_limits<uint32_t>::max());
  #   CHECK_LE(non_shared, std::numeric_limits<uint32_t>::max());
  #   CHECK_LE(value.size(), std::numeric_limits<uint32_t>::max());
  #
  #   // Add "<shared><non_shared><value_size>" to buffer_
  #   core::PutVarint32(&buffer_, static_cast<uint32_t>(shared));
  #   core::PutVarint32(&buffer_, static_cast<uint32_t>(non_shared));
  #   core::PutVarint32(&buffer_, static_cast<uint32_t>(value.size()));
  #
  #   // Add string delta to buffer_ followed by value
  #   buffer_.append(key.data() + shared, non_shared);
  #   buffer_.append(value.data(), static_cast<uint32_t>(value.size()));
  #
  #   // Update state
  #   last_key_.resize(shared);
  #   last_key_.append(key.data() + shared, non_shared);
  #   assert(StringPiece(last_key_) == key);
  #   counter_++;
  # }
  def add(self, key, value):
    """
    REQUIRES: Finish() has not been called since the last call to Reset().
    REQUIRES: key is larger than any previously added key
    """
    key = core.string_view(key)
    value = core.string_view(value)
    # StringPiece last_key_piece(last_key_);
    last_key_piece = core.StringPiece(self.last_key_)
    # assert(!finished_);
    assert not self.finished_
    # assert(counter_ <= options_->block_restart_interval);
    assert self.counter_ <= self.options_.block_restart_interval
    # assert(buffer_.empty()  // No values yet?
    #        || key.compare(last_key_piece) > 0);
    assert (len(self.buffer_) <= 0  # No values yet?
            or key.compare(last_key_piece) > 0)

    # size_t shared = 0;
    shared = 0
    # if (counter_ < options_->block_restart_interval) {
    if self.counter_ < self.options_.block_restart_interval:
      # // See how much sharing to do with previous string
      # const size_t min_length = std::min(last_key_piece.size(), key.size());
      min_length = min(last_key_piece.size(), key.size())
      # while ((shared < min_length) && (last_key_piece[shared] == key[shared])) {
      #   shared++;
      # }
      while (shared < min_length) and (last_key_piece[shared] == key[shared]):
        shared += 1
    # } else {
    else:
      # // Restart compression
      # CHECK_LE(buffer_.size(), std::numeric_limits<uint32_t>::max());
      assert len(self.buffer_) <= np.iinfo(np.uint32).max
      # restarts_.push_back(static_cast<uint32_t>(buffer_.size()));
      self.restarts_.append(np.uint32(len(self.buffer_)))
      # counter_ = 0;
      self.counter_ = 0
    # }
    # const size_t non_shared = key.size() - shared;
    non_shared = key.size() - shared

    # CHECK_LE(shared, std::numeric_limits<uint32_t>::max());
    # CHECK_LE(non_shared, std::numeric_limits<uint32_t>::max());
    # CHECK_LE(value.size(), std::numeric_limits<uint32_t>::max());
    assert shared <= np.iinfo(np.uint32).max
    assert non_shared <= np.iinfo(np.uint32).max
    assert value.size() <= np.iinfo(np.uint32).max

    # // Add "<shared><non_shared><value_size>" to buffer_
    # core::PutVarint32(&buffer_, static_cast<uint32_t>(shared));
    # core::PutVarint32(&buffer_, static_cast<uint32_t>(non_shared));
    # core::PutVarint32(&buffer_, static_cast<uint32_t>(value.size()));
    coding.put_varint32(self.buffer_, shared)
    coding.put_varint32(self.buffer_, non_shared)
    coding.put_varint32(self.buffer_, value.size())

    # // Add string delta to buffer_ followed by value
    # buffer_.append(key.data() + shared, non_shared);
    # buffer_.append(value.data(), static_cast<uint32_t>(value.size()));
    self.buffer_.extend(key[shared:][:non_shared])
    self.buffer_.extend(value.bytes())

    # // Update state
    # last_key_.resize(shared);
    # last_key_.append(key.data() + shared, non_shared);
    # assert(StringPiece(last_key_) == key);
    # counter_++;
    strings.resize(self.last_key_, shared)
    self.last_key_.extend(key[shared:][:non_shared])
    assert core.StringPiece(self.last_key_) == key
    self.counter_ += 1

  # }  // namespace table
  # }  // namespace tensorflow
