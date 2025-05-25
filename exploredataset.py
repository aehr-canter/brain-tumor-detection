from libraries import *
from datapreprocessing import *

def explore_dataset(yes_directory, no_directory):
    yes_images = len(os.listdir(yes_directory))
    no_images = len(os.listdir(no_directory))

    print(f"number of tumor images: {yes_images}")
    print(f"number of normal images: {no_images}")
    print(f"total: {yes_images + no_images}")

    return yes_images, no_images


explore_dataset()