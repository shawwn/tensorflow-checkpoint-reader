# /* Copyright 2019 The TensorFlow Authors. All Rights Reserved.
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
# #include <memory>
# #include <string>
# #include <vector>
#
# #include "pybind11/pybind11.h"
# #include "pybind11/stl.h"
from ..... import core
# #include "tensorflow/core/lib/core/error_codes.pb.h"
# #include "tensorflow/core/lib/core/errors.h"
from ..... import errors
# #include "tensorflow/core/lib/core/status.h"
# #include "tensorflow/core/lib/io/buffered_inputstream.h"
from ....core.lib.io import buffered_inputstream
# #include "tensorflow/core/lib/io/random_inputstream.h"
from ....core.lib.io import random_inputstream
# #include "tensorflow/core/platform/env.h"
from ..... import env
# #include "tensorflow/core/platform/file_statistics.h"
# #include "tensorflow/core/platform/file_system.h"
from ..... import file_system
# #include "tensorflow/core/platform/stringpiece.h"
# #include "tensorflow/core/platform/tstring.h"
# #include "tensorflow/python/lib/core/pybind11_absl.h"
# #include "tensorflow/python/lib/core/pybind11_status.h"

from ...lib.core import py_exception_registry

def MaybeRaiseRegisteredFromStatusWithGIL(status: errors.Status):
  # TF_Code code = TF_GetCode(status);
  # if (code != TF_OK) {
  #   PyErr_SetObject(PyExceptionRegistry::Lookup(code),
  #                   pybind11::make_tuple(pybind11::none(), pybind11::none(),
  #                                        TF_Message(status))
  #                       .ptr());
  #   throw pybind11::error_already_set();
  # }
  if not status.ok():
    code = status.code()
    cls = py_exception_registry.PyExceptionRegistry.Lookup(code)
    exn = cls(None, None, status.error_message())
    raise exn

#
# namespace tensorflow {
# struct PyTransactionToken {
#   TransactionToken* token_;
# };
#
# inline TransactionToken* TokenFromPyToken(PyTransactionToken* t) {
#   return (t ? t->token_ : nullptr);
# }
# }  // namespace tensorflow
#
# namespace {
# namespace py = pybind11;
#
# PYBIND11_MODULE(_pywrap_file_io, m) {
#   using tensorflow::PyTransactionToken;
#   using tensorflow::TransactionToken;
#   py::class_<PyTransactionToken>(m, "TransactionToken")
#       .def("__repr__", [](const PyTransactionToken* t) {
#         if (t->token_) {
#           return std::string(t->token_->owner->DecodeTransaction(t->token_));
#         }
#         return std::string("Invalid token!");
#       });
#
#   m.def(
#       "FileExists",
#       [](const std::string& filename, PyTransactionToken* token) {
#         tensorflow::Status status;
#         {
#           py::gil_scoped_release release;
#           status = tensorflow::Env::Default()->FileExists(filename);
#         }
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("filename"), py::arg("token") = (PyTransactionToken*)nullptr);
def FileExists(filename: str):
  status = env.Env.default().file_exists(filename)
  MaybeRaiseRegisteredFromStatusWithGIL(status)

#   m.def(
#       "DeleteFile",
#       [](const std::string& filename, PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         tensorflow::Status status =
#             tensorflow::Env::Default()->DeleteFile(filename);
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("filename"), py::arg("token") = (PyTransactionToken*)nullptr);
def DeleteFile(filename: str):
  status = env.Env.default().delete_file(filename)
  MaybeRaiseRegisteredFromStatusWithGIL(status)
#   m.def(
#       "ReadFileToString",
#       [](const std::string& filename, PyTransactionToken* token) {
#         std::string data;
#         py::gil_scoped_release release;
#         const auto status =
#             ReadFileToString(tensorflow::Env::Default(), filename, &data);
#         pybind11::gil_scoped_acquire acquire;
#         tensorflow::MaybeRaiseRegisteredFromStatus(status);
#         return py::bytes(data);
#       },
#       py::arg("filename"), py::arg("token") = (PyTransactionToken*)nullptr);
#   m.def(
#       "WriteStringToFile",
#       [](const std::string& filename, tensorflow::StringPiece data,
#          PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         const auto status =
#             WriteStringToFile(tensorflow::Env::Default(), filename, data);
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("filename"), py::arg("data"),
#       py::arg("token") = (PyTransactionToken*)nullptr);
#   m.def(
#       "GetChildren",
#       [](const std::string& dirname, PyTransactionToken* token) {
#         std::vector<std::string> results;
#         py::gil_scoped_release release;
#         const auto status =
#             tensorflow::Env::Default()->GetChildren(dirname, &results);
#         pybind11::gil_scoped_acquire acquire;
#         tensorflow::MaybeRaiseRegisteredFromStatus(status);
#         return results;
#       },
#       py::arg("dirname"), py::arg("token") = (PyTransactionToken*)nullptr);
#   m.def(
#       "GetMatchingFiles",
#       [](const std::string& pattern, PyTransactionToken* token) {
#         std::vector<std::string> results;
#         py::gil_scoped_release release;
#         const auto status =
#             tensorflow::Env::Default()->GetMatchingPaths(pattern, &results);
#         pybind11::gil_scoped_acquire acquire;
#         tensorflow::MaybeRaiseRegisteredFromStatus(status);
#         return results;
#       },
#       py::arg("pattern"), py::arg("token") = (PyTransactionToken*)nullptr);
def GetMatchingFiles(pattern):
  status, results = env.Env.default().get_matching_paths(pattern)
  MaybeRaiseRegisteredFromStatusWithGIL(status)
  return results
#   m.def(
#       "CreateDir",
#       [](const std::string& dirname, PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         const auto status = tensorflow::Env::Default()->CreateDir(dirname);
#         if (tensorflow::errors::IsAlreadyExists(status)) {
#           return;
#         }
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("dirname"), py::arg("token") = (PyTransactionToken*)nullptr);
#   m.def(
#       "RecursivelyCreateDir",
#       [](const std::string& dirname, PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         const auto status =
#             tensorflow::Env::Default()->RecursivelyCreateDir(dirname);
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("dirname"), py::arg("token") = (PyTransactionToken*)nullptr);
#   m.def(
#       "CopyFile",
#       [](const std::string& src, const std::string& target, bool overwrite,
#          PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         auto* env = tensorflow::Env::Default();
#         tensorflow::Status status;
#         if (!overwrite && env->FileExists(target).ok()) {
#           status = tensorflow::errors::AlreadyExists("file already exists");
#         } else {
#           status = env->CopyFile(src, target);
#         }
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("src"), py::arg("target"), py::arg("overwrite"),
#       py::arg("token") = (PyTransactionToken*)nullptr);
#   m.def(
#       "RenameFile",
#       [](const std::string& src, const std::string& target, bool overwrite,
#          PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         auto* env = tensorflow::Env::Default();
#         tensorflow::Status status;
#         if (!overwrite && env->FileExists(target).ok()) {
#           status = tensorflow::errors::AlreadyExists("file already exists");
#         } else {
#           status = env->RenameFile(src, target);
#         }
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("src"), py::arg("target"), py::arg("overwrite"),
#       py::arg("token") = (PyTransactionToken*)nullptr);
def RenameFile(src, target, overwrite: bool):
  env_ = env.Env.default()
  if not overwrite and env_.file_exists(target).ok():
    status = errors.AlreadyExists("file already exists")
  else:
    status = env_.rename_file(src, target)
  MaybeRaiseRegisteredFromStatusWithGIL(status)

#   m.def(
#       "DeleteRecursively",
#       [](const std::string& dirname, PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         tensorflow::int64 undeleted_files;
#         tensorflow::int64 undeleted_dirs;
#         auto status = tensorflow::Env::Default()->DeleteRecursively(
#             dirname, &undeleted_files, &undeleted_dirs);
#         if (status.ok() && (undeleted_files > 0 || undeleted_dirs > 0)) {
#           status = tensorflow::errors::PermissionDenied(
#               "could not fully delete dir");
#         }
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#       },
#       py::arg("dirname"), py::arg("token") = (PyTransactionToken*)nullptr);

#   m.def(
#       "IsDirectory",
#       [](const std::string& dirname, PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         const auto status = tensorflow::Env::Default()->IsDirectory(dirname);
#         // FAILED_PRECONDITION response means path exists but isn't a dir.
#         if (tensorflow::errors::IsFailedPrecondition(status)) {
#           return false;
#         }
#
#         tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#         return true;
#       },
#       py::arg("dirname"), py::arg("token") = (PyTransactionToken*)nullptr);
def IsDirectory(dirname):
  status = env.Env.default().is_directory(dirname)
  # FAILED_PRECONDITION response means path exists but isn't a dir.
  if errors.is_failed_precondition(status):
    return False
  MaybeRaiseRegisteredFromStatusWithGIL(status)
  return True

#   m.def("HasAtomicMove", [](const std::string& path) {
#     py::gil_scoped_release release;
#     bool has_atomic_move;
#     const auto status =
#         tensorflow::Env::Default()->HasAtomicMove(path, &has_atomic_move);
#     tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
#     return has_atomic_move;
#   });
def HasAtomicMove(path):
  status, has_atomic_move = env.Env.default().has_atomic_move(path)
  MaybeRaiseRegisteredFromStatusWithGIL(status)
  return has_atomic_move

#   py::class_<tensorflow::FileStatistics>(m, "FileStatistics")
#       .def_readonly("length", &tensorflow::FileStatistics::length)
#       .def_readonly("mtime_nsec", &tensorflow::FileStatistics::mtime_nsec)
#       .def_readonly("is_directory", &tensorflow::FileStatistics::is_directory);
#
#   m.def(
#       "Stat",
#       [](const std::string& filename, PyTransactionToken* token) {
#         py::gil_scoped_release release;
#         std::unique_ptr<tensorflow::FileStatistics> self(
#             new tensorflow::FileStatistics);
#         const auto status =
#             tensorflow::Env::Default()->Stat(filename, self.get());
#         py::gil_scoped_acquire acquire;
#         tensorflow::MaybeRaiseRegisteredFromStatus(status);
#         return self.release();
#       },
#       py::arg("filename"), py::arg("token") = (PyTransactionToken*)nullptr);
def Stat(filename):
  status, self = env.Env.default().stat(filename)
  MaybeRaiseRegisteredFromStatusWithGIL(status)
  return self

#   using tensorflow::WritableFile;
#   py::class_<WritableFile>(m, "WritableFile")
class WritableFile:
  # .def(py::init([](const std::string& filename, const std::string& mode,
  #                  PyTransactionToken* token) {
  #        py::gil_scoped_release release;
  #        auto* env = tensorflow::Env::Default();
  #        std::unique_ptr<WritableFile> self;
  #        const auto status = mode.find('a') == std::string::npos
  #                                ? env->NewWritableFile(filename, &self)
  #                                : env->NewAppendableFile(filename, &self);
  #        py::gil_scoped_acquire acquire;
  #        tensorflow::MaybeRaiseRegisteredFromStatus(status);
  #        return self.release();
  #      }),
  #      py::arg("filename"), py::arg("mode"),
  #      py::arg("token") = (PyTransactionToken*)nullptr)
  def __init__(self, filename, mode=b"w"):
    env_ = env.Env.default()
    status, me = env_.new_writable_file(filename) if b'a' not in mode else env.new_appendable_file(filename)
    MaybeRaiseRegisteredFromStatusWithGIL(status)
    self.me_ = me

  # .def("append",
  #      [](WritableFile* self, tensorflow::StringPiece data) {
  #        const auto status = self->Append(data);
  #        tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
  #      })
  def append(self, data):
    status = self.me_.append(core.string_view(data))
    MaybeRaiseRegisteredFromStatusWithGIL(status)

  # // TODO(slebedev): Make WritableFile::Tell const and change self
  # // to be a reference.
  # .def("tell",
  #      [](WritableFile* self) {
  #        tensorflow::int64 pos = -1;
  #        py::gil_scoped_release release;
  #        const auto status = self->Tell(&pos);
  #        tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
  #        return pos;
  #      })
  def tell(self):
    status, pos = self.me_.tell()
    MaybeRaiseRegisteredFromStatusWithGIL(status)
    return pos

  # .def("flush",
  #      [](WritableFile* self) {
  #        py::gil_scoped_release release;
  #        tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(self->Flush());
  #      })
  def flush(self):
    MaybeRaiseRegisteredFromStatusWithGIL(self.me_.flush())

  # .def("close", [](WritableFile* self) {
  #   py::gil_scoped_release release;
  #   tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(self->Close());
  # });
  def close(self):
    MaybeRaiseRegisteredFromStatusWithGIL(self.me_.close())
#
#   using tensorflow::io::BufferedInputStream;
#   py::class_<BufferedInputStream>(m, "BufferedInputStream")
class BufferedInputStream:
  # .def(py::init([](const std::string& filename, size_t buffer_size,
  #                  PyTransactionToken* token) {
  def __init__(self, filename, buffer_size: int):
    # py::gil_scoped_release release;
    # std::unique_ptr<tensorflow::RandomAccessFile> file;
    # const auto status =
    #     tensorflow::Env::Default()->NewRandomAccessFile(filename,
    #                                                     &file);
    status, file = env.Env.default().new_random_access_file(filename)
    # tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
    MaybeRaiseRegisteredFromStatusWithGIL(status)
    # std::unique_ptr<tensorflow::io::RandomAccessInputStream>
    #     input_stream(new tensorflow::io::RandomAccessInputStream(
    #         file.release(),
    #         /*owns_file=*/true));
    input_stream = random_inputstream.RandomAccessInputStream(file, owns_file=True)
    # py::gil_scoped_acquire acquire;
    # return new BufferedInputStream(input_stream.release(), buffer_size,
    #                                /*owns_input_stream=*/true);
    self.me_ = buffered_inputstream.BufferedInputStream(input_stream, buffer_size, owns_input_stream=True)
  #      }),
  #      py::arg("filename"), py::arg("buffer_size"),
  #      py::arg("token") = (PyTransactionToken*)nullptr)

  #     .def("read",
  #          [](BufferedInputStream* self, tensorflow::int64 bytes_to_read) {
  def read(self, bytes_to_read: int):
    # py::gil_scoped_release release;
    # tensorflow::tstring result;
    # const auto status = self->ReadNBytes(bytes_to_read, &result);
    status, result = self.me_.read_n_bytes(bytes_to_read)
    # if (!status.ok() && !tensorflow::errors::IsOutOfRange(status)) {
    #   result.clear();
    #   tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(status);
    # }
    if not status.ok() and not errors.is_out_of_range(status):
      result.clear()
      MaybeRaiseRegisteredFromStatusWithGIL(status)
    # py::gil_scoped_acquire acquire;
    # return py::bytes(result);
    return bytes(result)
  #          })

  #     .def("readline",
  #          [](BufferedInputStream* self) {
  #            py::gil_scoped_release release;
  #            auto output = self->ReadLineAsString();
  #            py::gil_scoped_acquire acquire;
  #            return py::bytes(output);
  #          })

  #     .def("seek",
  #          [](BufferedInputStream* self, tensorflow::int64 pos) {
  #            py::gil_scoped_release release;
  #            tensorflow::MaybeRaiseRegisteredFromStatusWithGIL(self->Seek(pos));
  #          })
  def seek(self, pos: int):
    MaybeRaiseRegisteredFromStatusWithGIL(self.me_.seek(pos))

  #     .def("tell", [](BufferedInputStream* self) {
  #       py::gil_scoped_release release;
  #       return self->Tell();
  def tell(self):
    return self.me_.tell()
#       });
# }
# }  // namespace