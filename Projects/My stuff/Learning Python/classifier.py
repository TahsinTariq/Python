import tensorflow as tf
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
print(labels)
colorTensor = tf.Variable(colors,  "int32")
labelTensor = tf.Variable(labels,  tf.strings)
# print(tf.rank(labelTensor))

oneHot = tf.one_hot(labelTensor, 9)
print(oneHot)
# labelTensor.dispose()



# indices = [0, 1, 2]
# depth = 3
# oneHot = tf.one_hot(indices, depth)
# print(oneHot)


# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(15, activation='relu'),
#     tf.keras.layers.Dense(10)
# ])


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