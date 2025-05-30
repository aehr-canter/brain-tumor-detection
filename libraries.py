import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import logging
import unittest
import shutil
import random

import tensorflow as tf
import keras as keras
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import set_random_seed
from keras.applications import DenseNet169
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.layers import Dense, GlobalAveragePooling2D, Dropout