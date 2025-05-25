from libraries import *

def create_model(img_height, img_width):

    base_model = DenseNet169(
        weights = 'imagenet',
        include_top = False,
        input_shape = (img_height, img_width, 3)
    )

    for layer in base_model.layers:
        layer.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.3)(x)
    predictions = Dense(1, activation='sigmoid')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    model.compile(
        optimizer = Adam(learning_rate=0.0001),
        loss = 'binary_crossentropy',
        metrics = ['accuracy']
    )

    return model, base_model