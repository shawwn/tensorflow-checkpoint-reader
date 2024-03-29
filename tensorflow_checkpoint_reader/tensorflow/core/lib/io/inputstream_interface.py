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
# #ifndef TENSORFLOW_CORE_LIB_IO_INPUTSTREAM_INTERFACE_H_
# #define TENSORFLOW_CORE_LIB_IO_INPUTSTREAM_INTERFACE_H_
#
# #include <string>
#
# #include "tensorflow/core/lib/core/errors.h"
# #include "tensorflow/core/lib/core/status.h"
# #include "tensorflow/core/platform/cord.h"
# #include "tensorflow/core/platform/types.h"
#
# namespace tensorflow {
# namespace io {
#
# // An interface that defines input streaming operations.
# class InputStreamInterface {
#  public:
#   InputStreamInterface() {}
#   virtual ~InputStreamInterface() {}
#
#   // Reads the next bytes_to_read from the file. Typical return codes:
#   //  * OK - in case of success.
#   //  * OUT_OF_RANGE - not enough bytes remaining before end of file.
#   virtual Status ReadNBytes(int64 bytes_to_read, tstring* result) = 0;
#
# #if defined(TF_CORD_SUPPORT)
#   // Reads the next bytes_to_read from the file. Typical return codes:
#   //  * OK - in case of success.
#   //  * OUT_OF_RANGE - not enough bytes remaining before end of file.
#   virtual Status ReadNBytes(int64 bytes_to_read, absl::Cord* cord) {
#     return errors::Unimplemented(
#         "ReadNBytes(int64, absl::Cord*) is not implemented.");
#   }
# #endif
#
#   // Skips bytes_to_skip before next ReadNBytes. bytes_to_skip should be >= 0.
#   // Typical return codes:
#   //  * OK - in case of success.
#   //  * OUT_OF_RANGE - not enough bytes remaining before end of file.
#   virtual Status SkipNBytes(int64 bytes_to_skip);
#
#   // Return the offset of the current byte relative to the beginning of the
#   // file.
#   // If we Skip / Read beyond the end of the file, this should return the length
#   // of the file.
#   // If there are any errors, this must return -1.
#   virtual int64 Tell() const = 0;
#
#   // Resets the stream to the beginning.
#   virtual Status Reset() = 0;
# };
#
# }  // namespace io
# }  // namespace tensorflow
#
# #endif  // TENSORFLOW_CORE_LIB_IO_INPUTSTREAM_INTERFACE_H_

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
# #include "tensorflow/core/lib/io/inputstream_interface.h"
#
# #include "tensorflow/core/lib/core/errors.h"
#
# namespace tensorflow {
# namespace io {
#
# // To limit memory usage, the default implementation of SkipNBytes() only reads
# // 8MB at a time.
# static constexpr int64 kMaxSkipSize = 8 * 1024 * 1024;
#
# Status InputStreamInterface::SkipNBytes(int64 bytes_to_skip) {
#   if (bytes_to_skip < 0) {
#     return errors::InvalidArgument("Can't skip a negative number of bytes");
#   }
#   tstring unused;
#   // Read kDefaultSkipSize at a time till bytes_to_skip.
#   while (bytes_to_skip > 0) {
#     int64 bytes_to_read = std::min<int64>(kMaxSkipSize, bytes_to_skip);
#     TF_RETURN_IF_ERROR(ReadNBytes(bytes_to_read, &unused));
#     bytes_to_skip -= bytes_to_read;
#   }
#   return Status::OK();
# }
#
# }  // namespace io
# }  // namespace tensorflow

from ..... import core
from ..... import errors

from abc import ABC, abstractmethod

from typing import Tuple, Optional

class InputStreamInterface(ABC):
  # // Reads the next bytes_to_read from the file. Typical return codes:
  # //  * OK - in case of success.
  # //  * OUT_OF_RANGE - not enough bytes remaining before end of file.
  # virtual Status ReadNBytes(int64 bytes_to_read, tstring* result) = 0;
  @abstractmethod
  def read_n_bytes(self, bytes_to_read: int) -> Tuple[errors.Status, Optional[bytearray]]:
    """Reads the next bytes_to_read from the file.

    Typical return codes:
     * OK - in case of success.
     * OUT_OF_RANGE - not enough bytes remaining before end of file.
    """
    ...

  # // Skips bytes_to_skip before next ReadNBytes. bytes_to_skip should be >= 0.
  # // Typical return codes:
  # //  * OK - in case of success.
  # //  * OUT_OF_RANGE - not enough bytes remaining before end of file.
  # virtual Status SkipNBytes(int64 bytes_to_skip);
  @abstractmethod
  def skip_n_bytes(self, bytes_to_skip: int) -> errors.Status:
    """Skips bytes_to_skip before next ReadNBytes. bytes_to_skip should be >= 0.

    Typical return codes:
     * OK - in case of success.
     * OUT_OF_RANGE - not enough bytes remaining before end of file.
    """
    ...

  # // Return the offset of the current byte relative to the beginning of the
  # // file.
  # // If we Skip / Read beyond the end of the file, this should return the length
  # // of the file.
  # // If there are any errors, this must return -1.
  # virtual int64 Tell() const = 0;
  @abstractmethod
  def tell(self) -> int:
    """Return the offset of the current byte relative to the beginning of the
    file.

    If we Skip / Read beyond the end of the file, this should return the length
    of the file.

    If there are any errors, this must return -1.
    """
    ...

  # // Resets the stream to the beginning.
  # virtual Status Reset() = 0;
  @abstractmethod
  def reset(self):
    """Resets the stream to the beginning."""
    ...

