from tensorflow_checkpoint_reader import bundle_reader, env
import sys

if __name__ == '__main__':
  args = sys.argv[1:]
  model = '117M' if len(args) < 1 else args[0]
  reader = bundle_reader.BundleReader(env.Env.default(), f'models/{model}/model.ckpt')
