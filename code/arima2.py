# Import libraries
import numpy as np
import pandas as pd
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import statsmodels.api as sm
import warnings
from itertools import product
from datetime import datetime
from sklearn.metrics import mean_squared_error



def parser(x):
	return datetime.fromtimestamp(int(x))


df = pd.read_csv('../data/data.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)

X = df.values
size = int(len(X)-1000)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(5,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()