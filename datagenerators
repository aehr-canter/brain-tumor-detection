from libraries import *

logging.basicConfig(level=logging.INFO) #added later to help in debugging

img_height = 224
img_width = 224
batch_size = 32
val_split = 0.2

def setup_data(main_directory, img_height, img_width, batch_size):
    if not os.path.exists(main_directory):
        raise FileNotFoundError(f"Base directory not found: {main_directory}")

    logging.info(f"Setting up generators using data from: {main_directory}")

    datagen = ImageDataGenerator(
        rescale = 1./255,
        rotation_range = 10,
        width_shift_range = 0.05,
        height_shift_range = 0.05,
        zoom_range = 0.1,
        horizontal_flip = True,
        fill_mode='nearest',
        validation_split = val_split
    )

    train_gen = datagen.flow_from_directory(
        main_directory,
        target_size = (img_height, img_width),
        batch_size = batch_size,
        class_mode = 'binary',
        subset = 'training',
        shuffle = True
    )

    val_gen = datagen.flow_from_directory(
        main_directory,
        target_size = (img_height, img_width),
        batch_size = batch_size,
        class_mode = 'binary',
        subset = 'validation',
        shuffle = False
    )

    test_datagen = ImageDataGenerator(rescale=1./255)
    test_gen = test_datagen.flow_from_directory(
        main_directory,
        target_size = (img_height, img_width),
        batch_size = batch_size,
        class_mode = 'binary',
        shuffle = False
    )

    logging.info(f"Data generators created. Classes found: {train_gen.class_indices}")
    return train_gen, val_gen, test_gen