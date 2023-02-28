# -*- coding: utf-8 -*-
from setuptools import setup
import os

def path(to):
  return os.path.join(os.path.dirname(__file__), to)

exec(compile(open(path("setup_info.py")).read(), path("setup_info.py"), "exec"))

packages = \
['tensorflow_checkpoint_reader',
 'tensorflow_checkpoint_reader.pb',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.jit',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.mlir.lite.quantization',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.tf2tensorrt.utils',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.tf2xla',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.xla',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.xla.pjrt.distributed',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.xla.python.tpu_driver',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.xla.rpc',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.xla.service',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.xla.service.gpu',
 'tensorflow_checkpoint_reader.pb.tensorflow.compiler.xrt',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.data',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.data.service',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.debug',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.example',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.framework',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.grappler.costs',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.grappler.optimizers.inference',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.kernels.boosted_trees',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.lib.core',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.profiler',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.profiler.protobuf',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.protobuf',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.protobuf.tpu',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.tpu.kernels',
 'tensorflow_checkpoint_reader.pb.tensorflow.core.util',
 'tensorflow_checkpoint_reader.pb.tensorflow.lite.experimental.acceleration.configuration',
 'tensorflow_checkpoint_reader.pb.tensorflow.lite.python.metrics_wrapper',
 'tensorflow_checkpoint_reader.pb.tensorflow.lite.toco',
 'tensorflow_checkpoint_reader.pb.tensorflow.lite.toco.logging',
 'tensorflow_checkpoint_reader.pb.tensorflow.lite.tools.evaluation.proto',
 'tensorflow_checkpoint_reader.pb.tensorflow.python.framework',
 'tensorflow_checkpoint_reader.pb.tensorflow.python.keras.protobuf',
 'tensorflow_checkpoint_reader.pb.tensorflow.python.kernel_tests.proto',
 'tensorflow_checkpoint_reader.pb.tensorflow.python.tpu',
 'tensorflow_checkpoint_reader.pb.tensorflow.python.training',
 'tensorflow_checkpoint_reader.pb.tensorflow.python.util.protobuf',
 'tensorflow_checkpoint_reader.pb.tensorflow.stream_executor',
 'tensorflow_checkpoint_reader.pb.tensorflow.tools.api.lib',
 'tensorflow_checkpoint_reader.pb.tensorflow.tools.proto_text',
 'tensorflow_checkpoint_reader.std',
 'tensorflow_checkpoint_reader.tensorflow',
 'tensorflow_checkpoint_reader.tensorflow.core',
 'tensorflow_checkpoint_reader.tensorflow.core.lib',
 'tensorflow_checkpoint_reader.tensorflow.core.lib.io',
 'tensorflow_checkpoint_reader.tensorflow.python',
 'tensorflow_checkpoint_reader.tensorflow.python.eager',
 'tensorflow_checkpoint_reader.tensorflow.python.framework',
 'tensorflow_checkpoint_reader.tensorflow.python.lib',
 'tensorflow_checkpoint_reader.tensorflow.python.lib.core',
 'tensorflow_checkpoint_reader.tensorflow.python.lib.io',
 'tensorflow_checkpoint_reader.tensorflow.python.platform',
 'tensorflow_checkpoint_reader.tensorflow.python.training',
 'tensorflow_checkpoint_reader.tensorflow.python.util',
 'tensorflow_checkpoint_reader.tensorflow.tools',
 'tensorflow_checkpoint_reader.tensorflow.tools.docs']

package_data = \
{'': ['*']}

install_requires = \
['protobuf<3.19']


setup_kwargs = {
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
    **(globals().get('base_kwargs')),
}


setup(**setup_kwargs)
