import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import random
seed = 42
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

main_directory = 
yes_directory = os.path.join(main_directory, 'yes')
no_directory = os.path.join(main_directory, 'no')
