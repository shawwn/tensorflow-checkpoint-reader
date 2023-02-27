# /* Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================*/
#
# #ifndef TENSORFLOW_CORE_LIB_IO_RANDOM_INPUTSTREAM_H_
# #define TENSORFLOW_CORE_LIB_IO_RANDOM_INPUTSTREAM_H_
#
# #include "tensorflow/core/lib/io/inputstream_interface.h"
# #include "tensorflow/core/platform/cord.h"
# #include "tensorflow/core/platform/file_system.h"
#
# namespace tensorflow {
# namespace io {
#
# // Wraps a RandomAccessFile in an InputStreamInterface. A given instance of
# // RandomAccessInputStream is NOT safe for concurrent use by multiple threads.
# class RandomAccessInputStream : public InputStreamInterface {
#  public:
#   // Does not take ownership of 'file' unless owns_file is set to true. 'file'
#   // must outlive *this.
#   RandomAccessInputStream(RandomAccessFile* file, bool owns_file = false);
#
#   ~RandomAccessInputStream();
#
#   Status ReadNBytes(int64 bytes_to_read, tstring* result) override;
#
# #if defined(TF_CORD_SUPPORT)
#   Status ReadNBytes(int64 bytes_to_read, absl::Cord* result) override;
# #endif
#
#   Status SkipNBytes(int64 bytes_to_skip) override;
#
#   int64 Tell() const override;
#
#   Status Seek(int64 position) {
#     pos_ = position;
#     return Status::OK();
#   }
#
#   Status Reset() override { return Seek(0); }
#
#  private:
#   RandomAccessFile* file_;  // Not owned.
#   int64 pos_ = 0;           // Tracks where we are in the file.
#   bool owns_file_ = false;
# };
#
# }  // namespace io
# }  // namespace tensorflow
#
# #endif  // TENSORFLOW_CORE_LIB_IO_RANDOM_INPUTSTREAM_H_
from typing import Tuple

from tensorflow_checkpoint_reader import errors

# /* Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================*/
#
# #include "tensorflow/core/lib/io/random_inputstream.h"
# #include <memory>
#
# namespace tensorflow {
# namespace io {
#
# RandomAccessInputStream::RandomAccessInputStream(RandomAccessFile* file,
#                                                  bool owns_file)
#     : file_(file), owns_file_(owns_file) {}
#
# RandomAccessInputStream::~RandomAccessInputStream() {
#   if (owns_file_) {
#     delete file_;
#   }
# }
#
# Status RandomAccessInputStream::ReadNBytes(int64 bytes_to_read,
#                                            tstring* result) {
#   if (bytes_to_read < 0) {
#     return errors::InvalidArgument("Cannot read negative number of bytes");
#   }
#   result->clear();
#   result->resize_uninitialized(bytes_to_read);
#   char* result_buffer = &(*result)[0];
#   StringPiece data;
#   Status s = file_->Read(pos_, bytes_to_read, &data, result_buffer);
#   if (data.data() != result_buffer) {
#     memmove(result_buffer, data.data(), data.size());
#   }
#   result->resize(data.size());
#   if (s.ok() || errors::IsOutOfRange(s)) {
#     pos_ += data.size();
#   }
#   return s;
# }
#
# #if defined(TF_CORD_SUPPORT)
# Status RandomAccessInputStream::ReadNBytes(int64 bytes_to_read,
#                                            absl::Cord* result) {
#   if (bytes_to_read < 0) {
#     return errors::InvalidArgument("Cannot read negative number of bytes");
#   }
#   int64 current_size = result->size();
#   Status s = file_->Read(pos_, bytes_to_read, result);
#   if (s.ok() || errors::IsOutOfRange(s)) {
#     pos_ += result->size() - current_size;
#   }
#   return s;
# }
# #endif
#
# // To limit memory usage, the default implementation of SkipNBytes() only reads
# // 8MB at a time.
# static constexpr int64 kMaxSkipSize = 8 * 1024 * 1024;
#
# Status RandomAccessInputStream::SkipNBytes(int64 bytes_to_skip) {
#   if (bytes_to_skip < 0) {
#     return errors::InvalidArgument("Can't skip a negative number of bytes");
#   }
#   std::unique_ptr<char[]> scratch(new char[kMaxSkipSize]);
#   // Try to read 1 bytes first, if we could complete the read then EOF is
#   // not reached yet and we could return.
#   if (bytes_to_skip > 0) {
#     StringPiece data;
#     Status s = file_->Read(pos_ + bytes_to_skip - 1, 1, &data, scratch.get());
#     if ((s.ok() || errors::IsOutOfRange(s)) && data.size() == 1) {
#       pos_ += bytes_to_skip;
#       return Status::OK();
#     }
#   }
#   // Read kDefaultSkipSize at a time till bytes_to_skip.
#   while (bytes_to_skip > 0) {
#     int64 bytes_to_read = std::min<int64>(kMaxSkipSize, bytes_to_skip);
#     StringPiece data;
#     Status s = file_->Read(pos_, bytes_to_read, &data, scratch.get());
#     if (s.ok() || errors::IsOutOfRange(s)) {
#       pos_ += data.size();
#     } else {
#       return s;
#     }
#     if (data.size() < static_cast<size_t>(bytes_to_read)) {
#       return errors::OutOfRange("reached end of file");
#     }
#     bytes_to_skip -= bytes_to_read;
#   }
#   return Status::OK();
# }
#
# int64 RandomAccessInputStream::Tell() const { return pos_; }
#
# }  // namespace io
# }  // namespace tensorflow

from . import inputstream_interface
from ..... import file_system

from typing import Tuple, Optional


class RandomAccessInputStream(inputstream_interface.InputStreamInterface):
  """Wraps a RandomAccessFile in an InputStreamInterface. A given instance of
  RandomAccessInputStream is NOT safe for concurrent use by multiple threads."""

  #   // Does not take ownership of 'file' unless owns_file is set to true. 'file'
  #   // must outlive *this.
  #   RandomAccessInputStream(RandomAccessFile* file, bool owns_file = false);
  def __init__(self, file: file_system.RandomAccessFile, owns_file: bool = False):
    """Does not take ownership of 'file' unless owns_file is set to true. 'file'
    must outlive self."""
    self.file_ = file
    self.owns_file_ = owns_file
    self.pos_ = 0

  def read_n_bytes(self, bytes_to_read: int) -> Tuple[errors.Status, Optional[bytearray]]:
    #   if (bytes_to_read < 0) {
    #     return errors::InvalidArgument("Cannot read negative number of bytes");
    #   }
    if bytes_to_read < 0:
      return errors.InvalidArgument("Cannot read negative number of bytes"), None
    #   result->clear();
    #   result->resize_uninitialized(bytes_to_read);
    #   char* result_buffer = &(*result)[0];
    #   StringPiece data;
    #   Status s = file_->Read(pos_, bytes_to_read, &data, result_buffer);
    s, data = self.file_.read(self.pos_, bytes_to_read)
    #   if (data.data() != result_buffer) {
    #     memmove(result_buffer, data.data(), data.size());
    #   }
    #   result->resize(data.size());
    #   if (s.ok() || errors::IsOutOfRange(s)) {
    if s.ok() or errors.is_out_of_range(s):
      #   pos_ += data.size();
      self.pos_ += data.size()
    #   }
    #   return s;
    return s, data.slice()

  def skip_n_bytes(self, bytes_to_skip: int) -> errors.Status:
    raise NotImplementedError

  # int64 RandomAccessInputStream::Tell() const { return pos_; }
  def tell(self) -> int:
    return self.pos_

  def reset(self):
    raise NotImplementedError

