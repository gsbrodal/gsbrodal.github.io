# Some accuracy values:

# No hidden layers / linear classifier
#   Linear + mean-square: 83.6% accuracy
#   Softmax + categorical_crossentropy: 92.7% accuracy

# 1 hidden layer
#   layer size 16 + ReLU + Softmax + categorical_crossentropy: 94.5% accuracy

# 2 hidden layers
#   layer sizes 256 + ReLU + Softmax + categorical_crossentropy: 98.0% accuracy


from tensorflow import keras

(images_train, labels_train), (images_test, labels_test) = keras.datasets.mnist.load_data()

images_train = images_train.reshape((60000, 28 * 28)).astype('float32') / 255
images_test  = images_test .reshape((10000, 28 * 28)).astype('float32') / 255

labels_train, labels_test = map(keras.utils.to_categorical, (labels_train, labels_test))

network = keras.models.Sequential()

# 0 hidden layer network (linear classifier)

#network.add(keras.layers.Dense(10, activation='linear', input_shape=(28 * 28,)))
network.add(keras.layers.Dense(10, activation='softmax', input_shape=(28 * 28,)))

# 1 layer network (linear classifier)
#network.add(keras.layers.Dense(16, activation='relu', input_shape=(28 * 28,)))
#network.add(keras.layers.Dense(10, activation='softmax'))

# 2 hidden layers
#network.add(keras.layers.Dense(256, activation='relu', input_shape=(28 * 28,)))
#network.add(keras.layers.Dense(256, activation='relu'))
#network.add(keras.layers.Dense(10, activation='softmax'))

network.compile(
#    optimizer='adam',
    optimizer='rmsprop',
#    loss='mean_squared_error',
    loss='categorical_crossentropy',  # for small loss
    metrics=['accuracy']
)

network.fit(images_train, labels_train, epochs=10, batch_size=100)

results = network.evaluate(images_test, labels_test)
print('loss, accuracy:', *results)

with open('mnist_linear.weights', 'w') as f:
    print([a.tolist() for a in network.get_weights()], file=f)
