# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tensorflow_checkpoint_reader',
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
 'tensorflow_checkpoint_reader.std']

package_data = \
{'': ['*']}

install_requires = \
['protobuf<3.19']

setup_kwargs = {
    'name': 'tensorflow-checkpoint-reader',
    'version': '0.1.3',
    'description': "Tensorflow's CheckpointReader in pure python",
    'description_content_type': "text/markdown",
    'long_description': "# tensorflow-checkpoint-reader\n\n> Tensorflow's CheckpointReader in pure python\n\nWARNING: This repo is in development. It was automatically generated with [mkpylib](https://github.com/shawwn/scrap/blob/master/mkpylib). If you're reading this message, it means that I use this repo for my own purposes right now. It might not do anything at all; the default functionality is `print('TODO')`.\n\nIf you really want to try it out, feel free. I recommend reading through the code and commit history to see if it does what you need, or [ask me](#contact) for status updates.\n\nStay tuned!\n\n## Install\n\n```\npython3 -m pip install -U tensorflow-checkpoint-reader\n```\n\n## Usage\n\n```py\nimport tensorflow_checkpoint_reader\n\nprint('TODO')\n```\n\n## License\n\nMIT\n\n## Contact\n\nA library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!\n\nMy Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.\n\n- Twitter: [@theshawwn](https://twitter.com/theshawwn)\n- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)\n- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)\n- Website: [shawwn.com](https://www.shawwn.com)\n\n",
    'long_description_content_type': "text/markdown",
    'author': 'Shawn Presser',
    'author_email': 'shawnpresser@gmail.com',
    'maintainer': 'Shawn Presser',
    'maintainer_email': 'shawnpresser@gmail.com',
    'url': 'https://github.com/shawwn/tensorflow-checkpoint-reader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
