#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
tf.config.experimental.set_memory_growth(physical_devices[0], True)

from keras import models, layers
from keras.datasets import mnist
from keras.utils import to_categorical
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras.utils import to_categorical

# Remove: PassengerId, Name, Ticket, Cabin
# CLass: label	
# Used: 
#    number: meanfreq,sd,median,Q25,Q75,IQR,skew,kurt,sp.ent,sfm,mode,centroid,meanfun,minfun,maxfun,meandom,mindom,maxdom,dfrange,modindx
#    categorical: 


file = '/home/fabiocarlesso/Downloads/RedesNeurais/atividades1_4/voice-dataset.csv'
dataset = pd.read_csv(file, sep=',')
dataset.label = pd.Categorical(dataset['label']).codes

dataclass = dataset['label']
dataset = dataset.drop(columns=['label'])


_traindata, _testdata, _trainclass, _testclass = train_test_split(dataset, dataclass, test_size=0.3)

_traindata = tf.convert_to_tensor(_traindata, dtype=tf.int64)
_testdata = tf.convert_to_tensor(_testdata, dtype=tf.int64)
_trainclass = to_categorical(_trainclass)
_testclass = to_categorical(_testclass)

network = models.Sequential()
network.add(layers.Dense(128,activation='relu', input_shape=(20,))) # input_shape  = quantidade de dados de entrada (colunas)
network.add(layers.Dense(32, activation='relu'))
# network.add(layers.Dense(, activation='relu'))
# network.add(layers.Dense(40, activation='relu'))
network.add(layers.Dense(16, activation='relu'))
network.add(layers.Dense(2, activation='softmax')) # última camada / número de classes
network.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
# network.summary()

history = network.fit(_traindata, _trainclass,  epochs=200,  batch_size=32, validation_data=(_testdata,_testclass))
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