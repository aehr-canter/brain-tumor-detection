from libraries import *

def callbacks():
    checkpoint = ModelCheckpoint(
        'densenet169_brain_tumor.h5',
        monitor = 'val_accuracy',
        save_best_only = True,
        verbose = 1
    )

    earlystopping = EarlyStopping(
        monitor = 'val_loss',
        patience = 10,
        verbose = 1,
        restore_best_weights = True
    )

    reducelr = ReduceLROnPlateau(
        monitor = 'val_loss',
        factor = 0.2,
        patience = 5,
        min_lr = 1e-6,
        verbose = 1
    )

    return [checkpoint, earlystopping, reducelr]