import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def export_data(train_images, train_labels, class_names):
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()


def manipulate_data(train_images, test_images):
    train_images = train_images / 255.0
    test_images = test_images / 255.0


def train_model(train_images, train_labels):
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(
                      from_logits=True),
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=10)
    return model


if __name__ == "__main__":
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images,
                                   test_labels) = fashion_mnist.load_data()
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    manipulate_data(train_images, test_images)
    export_data(train_images, train_labels, class_names)
    model = train_model(train_images, train_labels)

    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print('\nTest Accuracy: ', test_acc)
