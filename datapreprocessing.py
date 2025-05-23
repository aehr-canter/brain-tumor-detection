import os
import numpy as np
import tensorflow as tf #python3 -m pip install 'tensorflow[and-cuda]'
import random

seed = 42
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

main_directory = "/Users/RheaAgrawal/Desktop/brain-tumor-detection/kaggle-brain-tumor-detection"
yes_directory = os.path.join(main_directory, 'yes')
no_directory = os.path.join(main_directory, 'no')
