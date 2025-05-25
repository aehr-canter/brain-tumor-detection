from libraries import *

seed = 42
random.seed(seed)
np.random.seed(seed)
keras.utils.set_random_seed(seed)

main_directory = "/Users/RheaAgrawal/Desktop/brain-tumor-detection/kaggle-brain-tumor-detection"
yes_directory = os.path.join(main_directory, 'yes')
no_directory = os.path.join(main_directory, 'no')
