#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import tensorflow as tf
from keras import models, layers
from keras.datasets import mnist
from keras.utils import to_categorical
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras.utils import to_categorical

# Remove: 
# CLass: quality
# Used: 
#    number: fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol
#    categorical: 


file = '/home/fabiocarlesso/Downloads/RedesNeurais/atividades1_4/wine-dataset.csv'
dataset = pd.read_csv(file, sep=',')


dataclass = dataset['quality']
dataset = dataset.drop(columns=['quality'])


_traindata, _testdata, _trainclass, _testclass = train_test_split(dataset, dataclass, test_size=0.3)

_traindata = tf.convert_to_tensor(_traindata, dtype=tf.int64)
_testdata = tf.convert_to_tensor(_testdata, dtype=tf.int64)
_trainclass = to_categorical(_trainclass)
_testclass = to_categorical(_testclass)

network = models.Sequential()
network.add(layers.Dense(121, activation='relu', input_shape=(11,))) # input_shape  = quantidade de dados de entrada (colunas)
network.add(layers.Dense(99, activation='relu'))
network.add(layers.Dense(18, activation='relu'))
network.add(layers.Dense(9, activation='softmax')) # última camada / número de classes
network.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
# network.summary()

history = network.fit(_traindata, _trainclass,  epochs=200,  batch_size=16, validation_data=(_testdata,_testclass))
test_loss, test_acc = network.evaluate(_testdata, _testclass)
print('test_acc: ', test_acc)


import matplotlib.pyplot as plt
history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len( history_dict['loss']) + 1)

plt.plot(epochs, loss_values, 'bo', label='Training Loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation Loss')
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

#plt.clf()
acc_values = history_dict['accuracy']
val_acc_values = history_dict['val_accuracy']

plt.plot(epochs, acc_values, 'bo', label='Training Acc')
plt.plot(epochs, val_acc_values, 'b', label='Validation Acc')
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()