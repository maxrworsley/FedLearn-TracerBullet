import tensorflow as tf
from tensorflow import keras as k


class TFHandler:
    model = ""
    model_directory = ""

    def __init__(self, path):
        self.model_directory = path

    def save_model(self):
        self.model.save(self.model_directory)

    def load_model(self):
        self.model = k.models.load_model(self.model_directory)

    def make_model(self):
        model = k.Sequential(
            [
                k.layers.Dense(4, activation="relu", input_shape=(5, )),
                k.layers.Dense(4, activation="relu")
            ]
        )

        loss_fn = tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error")

        model.compile(optimizer='adam',
                      loss=loss_fn,
                      metrics=['accuracy'])
        self.model = model
