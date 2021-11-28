from tensorflow_checkpoint_reader import bundle_reader

if __name__ == '__main__':
  reader = bundle_reader.BundleReader('models/117M/model.ckpt')
