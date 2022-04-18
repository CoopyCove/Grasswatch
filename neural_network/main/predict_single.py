import argparse
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.python.data.ops.dataset_ops import AUTOTUNE;


def main() -> None:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Predict image class using trained model"
    )
    parser.add_argument("file")
    args = parser.parse_args()

    if not args.file:
        print("Please provide a valid image path")
    
    model = tf.keras.models.load_model("./neural_network/models/saved_models/greenwatch_model_2022_03_28-10_25_34_AM.h5");
    img = tf.keras.utils.load_img(
        args.file,
        target_size=(256,256)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_names = ["Healthy", "Unhealthy"]
    print(
        "\nThis image most likely belongs to {} with a {:.2f} percent confidance.\n"
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

if __name__ == "__main__":
    main()