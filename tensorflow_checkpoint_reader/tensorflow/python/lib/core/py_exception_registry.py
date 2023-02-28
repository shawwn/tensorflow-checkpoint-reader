from __future__ import annotations

from typing import ClassVar, Dict, Any, Mapping

# /* Copyright 2018 The TensorFlow Authors. All Rights Reserved.
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
# #ifndef TENSORFLOW_PYTHON_LIB_CORE_PY_EXCEPTION_REGISTRY_H_
# #define TENSORFLOW_PYTHON_LIB_CORE_PY_EXCEPTION_REGISTRY_H_
#
# #include <Python.h>
#
# #include <map>
#
# #include "tensorflow/c/tf_status.h"
# #include "tensorflow/core/lib/core/error_codes.pb.h"
#
# namespace tensorflow {
#
# // Global registry mapping C API error codes to the corresponding custom Python
# // exception type. This is used to expose the exception types to C extension
# // code (i.e. so we can raise custom exceptions via SWIG).
# //
# // Init() must be called exactly once at the beginning of the process before
# // Lookup() can be used.
# //
# // Example usage:
# //   TF_Status* status = TF_NewStatus();
# //   TF_Foo(..., status);
# //
# //   if (TF_GetCode(status) != TF_OK) {
# //     PyObject* exc_type = PyExceptionRegistry::Lookup(TF_GetCode(status));
# //     // Arguments to OpError base class. Set `node_def` and `op` to None.
# //     PyObject* args =
# //       Py_BuildValue("sss", nullptr, nullptr, TF_Message(status));
# //     PyErr_SetObject(exc_type, args);
# //     Py_DECREF(args);
# //     TF_DeleteStatus(status);
# //     return NULL;
# //   }
# class PyExceptionRegistry {
#  public:
#   // Initializes the process-wide registry. Should be called exactly once near
#   // the beginning of the process. The arguments are the various Python
#   // exception types (e.g. `cancelled_exc` corresponds to
#   // errors.CancelledError).
#   static void Init(PyObject* code_to_exc_type_map);
#
#   // Returns the Python exception type corresponding to `code`. Init() must be
#   // called before using this function. `code` should not be TF_OK.
#   static PyObject* Lookup(TF_Code code);
#
#   static inline PyObject* Lookup(error::Code code) {
#     return Lookup(static_cast<TF_Code>(code));
#   }
#
#  private:
#   static PyExceptionRegistry* singleton_;
#   PyExceptionRegistry() = default;
#
#   // Maps error codes to the corresponding Python exception type.
#   std::map<TF_Code, PyObject*> exc_types_;
# };
#
# }  // namespace tensorflow
#
# #endif  // TENSORFLOW_PYTHON_LIB_CORE_PY_EXCEPTION_REGISTRY_H_

# /* Copyright 2018 The TensorFlow Authors. All Rights Reserved.
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
# #include "tensorflow/python/lib/core/py_exception_registry.h"
#
# #include <Python.h>
#
# #include "tensorflow/core/platform/logging.h"
# #include "tensorflow/core/protobuf/error_codes.pb.h"
#
# namespace tensorflow {
#
# PyExceptionRegistry* PyExceptionRegistry::singleton_ = nullptr;
#
# void PyExceptionRegistry::Init(PyObject* code_to_exc_type_map) {
#   CHECK(singleton_ == nullptr) << "PyExceptionRegistry::Init() already called";
#   singleton_ = new PyExceptionRegistry;
#
#   CHECK(PyDict_Check(code_to_exc_type_map));
#   PyObject* key;
#   PyObject* value;
#   Py_ssize_t pos = 0;
#   while (PyDict_Next(code_to_exc_type_map, &pos, &key, &value)) {
#     singleton_->exc_types_.emplace(static_cast<TF_Code>(PyLong_AsLong(key)),
#                                    value);
#     // The exception classes should also have the lifetime of the process, but
#     // incref just in case.
#     Py_INCREF(value);
#   }
#
#   static const TF_Code kAllCodes[] = {TF_CANCELLED,
#                                       TF_UNKNOWN,
#                                       TF_INVALID_ARGUMENT,
#                                       TF_DEADLINE_EXCEEDED,
#                                       TF_NOT_FOUND,
#                                       TF_ALREADY_EXISTS,
#                                       TF_PERMISSION_DENIED,
#                                       TF_UNAUTHENTICATED,
#                                       TF_RESOURCE_EXHAUSTED,
#                                       TF_FAILED_PRECONDITION,
#                                       TF_ABORTED,
#                                       TF_OUT_OF_RANGE,
#                                       TF_UNIMPLEMENTED,
#                                       TF_INTERNAL,
#                                       TF_UNAVAILABLE,
#                                       TF_DATA_LOSS};
#   for (TF_Code code : kAllCodes) {
#     CHECK(singleton_->exc_types_.find(code) != singleton_->exc_types_.end())
#         << error::Code_Name(static_cast<error::Code>(code))
#         << " is not registered";
#   }
# }
#
# PyObject* PyExceptionRegistry::Lookup(TF_Code code) {
#   CHECK(singleton_ != nullptr) << "Must call PyExceptionRegistry::Init() "
#                                   "before PyExceptionRegistry::Lookup()";
#   CHECK_NE(code, TF_OK);
#   auto it = singleton_->exc_types_.find(code);
#   CHECK(it != singleton_->exc_types_.end())
#       << "Unknown error code passed to PyExceptionRegistry::Lookup: " << code;
#   return it->second;
# }
#
# }  // namespace tensorflow

class PyExceptionRegistry:
  singleton_: ClassVar[PyExceptionRegistry] = None

  # std::map<TF_Code, PyObject*> exc_types_;
  exc_types_: Dict[int, Any]

  def __init__(self):
    self.exc_types_ = {}

  # static void Init(PyObject* code_to_exc_type_map);
  @classmethod
  def Init(cls, code_to_exc_type_map: Mapping):
    """Initializes the process-wide registry. Should be called exactly once near
    the beginning of the process. The arguments are the various Python
    exception types (e.g. `cancelled_exc` corresponds to
    errors.CancelledError).
    """
    # CHECK(singleton_ == nullptr) << "PyExceptionRegistry::Init() already called";
    assert cls.singleton_ is None, "PyExceptionRegistry::Init() already called"
    # singleton_ = new PyExceptionRegistry;
    cls.singleton_ = cls()
    #
    # CHECK(PyDict_Check(code_to_exc_type_map));
    # PyObject* key;
    # PyObject* value;
    # Py_ssize_t pos = 0;
    # while (PyDict_Next(code_to_exc_type_map, &pos, &key, &value)) {
    #   singleton_->exc_types_.emplace(static_cast<TF_Code>(PyLong_AsLong(key)),
    #                                  value);
    #   // The exception classes should also have the lifetime of the process, but
    #   // incref just in case.
    #   Py_INCREF(value);
    # }
    for key, value in code_to_exc_type_map.items():
      cls.singleton_.exc_types_[key] = value

    # static const TF_Code kAllCodes[] = {TF_CANCELLED,
    #                                     TF_UNKNOWN,
    #                                     TF_INVALID_ARGUMENT,
    #                                     TF_DEADLINE_EXCEEDED,
    #                                     TF_NOT_FOUND,
    #                                     TF_ALREADY_EXISTS,
    #                                     TF_PERMISSION_DENIED,
    #                                     TF_UNAUTHENTICATED,
    #                                     TF_RESOURCE_EXHAUSTED,
    #                                     TF_FAILED_PRECONDITION,
    #                                     TF_ABORTED,
    #                                     TF_OUT_OF_RANGE,
    #                                     TF_UNIMPLEMENTED,
    #                                     TF_INTERNAL,
    #                                     TF_UNAVAILABLE,
    #                                     TF_DATA_LOSS};
    # for (TF_Code code : kAllCodes) {
    #   CHECK(singleton_->exc_types_.find(code) != singleton_->exc_types_.end())
    #       << error::Code_Name(static_cast<error::Code>(code))
    #       << " is not registered";
    # }
    for code in range(1, 16):
      if code not in cls.singleton_.exc_types_:
        raise RuntimeError(f"Error code {code} is not registered")

  #   static PyObject* Lookup(TF_Code code);
  @classmethod
  def Lookup(cls, code):
    """Returns the Python exception type corresponding to `code`. Init() must be
    called before using this function. `code` should not be TF_OK.
    """
    # CHECK(singleton_ != nullptr) << "Must call PyExceptionRegistry::Init() "
    #                                 "before PyExceptionRegistry::Lookup()";
    assert cls.singleton_ is not None, "Must call PyExceptionRegistry::Init() before PyExceptionRegistry::Lookup()"
    # CHECK_NE(code, TF_OK);
    assert code != 0
    # auto it = singleton_->exc_types_.find(code);
    it = cls.singleton_.exc_types_.get(code)
    # CHECK(it != singleton_->exc_types_.end())
    #     << "Unknown error code passed to PyExceptionRegistry::Lookup: " << code;
    assert it is not None, f"Unknown error code passed to PyExceptionRegistry::Lookup: {code}"
    # return it->second;
    return it
