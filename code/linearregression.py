import csv
import numpy as np
from parse import *
from sklearn import linear_model

data = readData()
[x,y] = parseData(data)
x = x.reshape(x.size, 1)

x_train = x[:-1000]
y_train = y[:-1000]

x_test = x[-1000:]
y_test = y[-1000:]

def lr(x_train, y_train, x_test, all, r):
    if(all):
        reg = linear_model.LinearRegression()
        reg.fit(x_train, y_train)
        return reg.predict(x_test)
    else:
        x_train = x_train[-r:]
        y_train = y_train[-r:]
        print(x_train.shape)
        reg = linear_model.LinearRegression()
        reg.fit(x_train, y_train)
        return reg.predict(x_test)

def mrlr(x_train, y_train, x_test, mr):
    y_pred = np.zeros(x_test.size)
    for i in range(x_test.size):
        xt = np.zeros(mr)
        yt = np.zeros(mr)
        if(i < mr):
            xt = np.concatenate((x_train[-(mr-i):], x_test[:i]))
            yt = np.concatenate((y_train[-(mr-i):], y_test[:i]))
        else:
            xt = x_test[(i - mr): i]
            yt = y_test[(i - mr): i]
        reg = linear_model.LinearRegression()
        reg.fit(xt, yt)
        y_pred[i] = reg.predict(x_test[i].reshape(1,1))
    return y_pred