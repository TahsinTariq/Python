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
    labels.append(record['label'])

# print(colors)
# print(labels)
colorTensor = tf.Variable(colors,  "int32")
labelTensor = tf.Variable(labels,  tf.strings)
print(tf.rank(labelTensor))