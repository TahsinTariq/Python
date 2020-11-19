import tensorflow as tf
import numpy as np
import json

labelList = [
  'red-ish',
  'green-ish',
  'blue-ish',
  'orange-ish',
  'yellow-ish',
  'pink-ish',
  'purple-ish',
  'brown-ish',
  'grey-ish'
]

with open("colorData.json") as file:
    data = json.load(file)
    # print(len(data["entries"]))

colors = []
labels = []
for record in data['entries']:
    colors.append([record['r'] / 255, record['g'] / 255, record['b'] / 255])
    labels.append(labelList.index(record['label']))

# print(colors)
# print(labels)
colorTensor = tf.Variable(colors,  "int32").numpy()
labelTensor = tf.Variable(labels,  tf.strings)
print(colorTensor)

oneHot = tf.one_hot(labelTensor, 9)
# print(oneHot)
# labelTensor.dispose()



# indices = [0, 1, 2]
# depth = 3
# oneHot = tf.one_hot(indices, depth)
# print(oneHot)

# md = tf.sequential(
#     tf.layers.dense({
#         units: 15,
#         inputShape: [3],
#         activation: 'sigmoid'
#       })
#     tf.layers.dense({
#         units: 9,
#         activation: 'softmax'
#       })
# )

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='sigmoid'),
    tf.keras.layers.Dense(20, activation='tanh'),
    tf.keras.layers.Dense(10, activation='sigmoid'),
    tf.keras.layers.Dense(9, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])

model.fit(colorTensor, oneHot, epochs=50, shuffle=True, validation_split=0.1)

model.summary()

cols = [[10, 255, 10],
        [50, 60, 40],
        [220, 20, 10],
        [150, 50, 200],
        [90, 250, 100],
        [0, 150, 150],
        [20, 10, 250]]
# myColor = tf.Variable([10, 255, 10],  "int32")
myColor = np.array([[220, 20, 10]])
# for col in cols:
# pred = model.predict(np.array([col]))
pred = model.predict(myColor)
# print(f"prediction : {np.argmax(pred)}")
pos = int(np.argmax(pred))
# print(pred)
print(f"Prediction: \n\toneHot: {pred}\n\targMax: {pos}\n\tType: {labelList[pos]}")

# import os
# import numpy as np
# import cv2
# import tensorflow as tf
#
#
# class ModelTrain():
#     def __init__(self):
#         self.loss_object = tf.keras.losses.CategoricalCrossentropy()
#         self.optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)
#         self.train_loss = tf.keras.metrics.CategoricalCrossentropy('train_loss', dtype=tf.float32)
#         self.train_accuracy = tf.keras.metrics.CategoricalAccuracy('train_accuracy')
#         self.validation_loss = tf.keras.metrics.CategoricalCrossentropy('validation_loss', dtype=tf.float32)
#         self.validation_accuracy = tf.keras.metrics.CategoricalAccuracy('validation_accuracy')
#
#
# if __name__ == "__main__":
#     model_train = ModelTrain()