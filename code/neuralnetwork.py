import csv
import numpy as np
from parse import *
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from sklearn.metrics import mean_squared_error

data = readData()
[x,y] = parseData(data)


y_train = y[:-1000]
y_test = y[-1000:]

model = Sequential()
model.add(Dense(100, input_dim = 100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(1))

model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])

mx_train = np.asarray([y_train[i:(i+100)] for i in range(y_train.size - 101)])
my_train = np.asarray([y_train[i+100] for i in range(y_train.size - 101)])
mx_test = np.asarray([y[i:(i+100)] for i in range(y.size - y_test.size - 100, y.size -100)])

model.fit(mx_train, my_train, epochs = 25, batch_size = 32)

print(mean_squared_error(model.predict(mx_test).flatten(), y_test))

model = Sequential()
model.add(Dense(100, input_dim = 100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(1))

model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])

mx_train = np.asarray([y_train[i:(i+100)] for i in range(y_train.size - 101)])
my_train = np.asarray([y_train[i+100] for i in range(y_train.size - 101)])
mx_test = np.asarray([y[i:(i+100)] for i in range(y.size - y_test.size - 100, y.size -100)])

model.fit(mx_train[:-10000], my_train[:-10000], epochs = 25, batch_size = 32)

print(mean_squared_error(model.predict(mx_test).flatten(), y_test))

model = Sequential()
model.add(Dense(100, input_dim = 100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(1))

model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])

mx_train = np.asarray([y_train[i:(i+100)] for i in range(y_train.size - 101)])
my_train = np.asarray([y_train[i+100] for i in range(y_train.size - 101)])
mx_test = np.asarray([y[i:(i+100)] for i in range(y.size - y_test.size - 100, y.size -100)])

model.fit(mx_train, my_train, epochs = 25, batch_size = 32)

print(mean_squared_error(model.predict(mx_test).flatten(), y_test))

model = Sequential()
model.add(Dense(100, input_dim = 100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(1))

model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])

mx_train = np.asarray([y_train[i:(i+100)] for i in range(y_train.size - 101)])
my_train = np.asarray([y_train[i+100] for i in range(y_train.size - 101)])
mx_test = np.asarray([y[i:(i+100)] for i in range(y.size - y_test.size - 100, y.size -100)])

model.fit(mx_train[:-10000], my_train[:-10000], epochs = 25, batch_size = 32)

print(mean_squared_error(model.predict(mx_test).flatten(), y_test))


