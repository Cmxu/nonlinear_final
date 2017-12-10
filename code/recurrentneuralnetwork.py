import csv
import numpy as np
from parse import *
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn import MinMaxScaler

data = readData()
[x,y] = parseData(data)
scaler = MinMaxScaler(feature_range=(-1, 1))
scalar.fit(y)
ys = scalar.transform(y)
y_train = ys[:-1000]
y_test = ys[-1000:]

mx_train = y_train[:-1]
my_train = y_train[1:]

model = Sequential()

model.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))

model.add(Dense(1))

model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(mx_train.reshape(mx_train.size, 1, 1), my_train, batch_size = 5, epochs = 100)

model.evaluate(y_test[:-1], y_test)