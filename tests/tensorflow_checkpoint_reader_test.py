import unittest
from tensorflow_checkpoint_reader.pb.tensorflow.core.protobuf import tensor_bundle_pb2

class TensorflowCheckpointReaderTestCase(unittest.TestCase):
  def test_basic(self):
    self.assertEqual(1, 1)

if __name__ == '__main__':
  unittest.main()
