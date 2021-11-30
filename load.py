from tensorflow_checkpoint_reader import bundle_reader, env

if __name__ == '__main__':
  reader = bundle_reader.BundleReader(env.Env.default(), 'models/117M/model.ckpt')
