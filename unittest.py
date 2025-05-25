from libraries import *
from exploredataset import *

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        # Create dummy directories and files for testing
        self.test_dir = 'test_dataset'
        self.yes_dir = os.path.join(self.test_dir, 'yes')
        self.no_dir = os.path.join(self.test_dir, 'no')
        os.makedirs(self.yes_dir)
        os.makedirs(self.no_dir)
        with open(os.path.join(self.yes_dir, 'img1.jpg'), 'w') as f:
            pass
        with open(os.path.join(self.yes_dir, 'img2.jpg'), 'w') as f:
            pass
        with open(os.path.join(self.no_dir, 'img3.jpg'), 'w') as f:
            pass

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_explore_dataset(self):
        yes_images, no_images = explore_dataset(self.yes_dir, self.no_dir)
        self.assertEqual(yes_images, 2)
        self.assertEqual(no_images, 1)

if __name__ == '__main__':
    unittest.main()