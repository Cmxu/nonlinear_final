from parse import parseData

#data = parseData()

#data.head(5)
import numpy as np

import pandas as pd

from datetime import datetime

from fbprophet import Prophet

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

df = pd.read_csv('../data/bitstampUSD_1-min_data_2012-01-01_to_2017-10-20.csv')

df['Timestamp'] = df['Timestamp'].apply(lambda x: datetime.fromtimestamp(x))

df = df[df['Timestamp'] >= '2017-01-01']


#leave only two columns
df = df.drop('Open', 1)
df = df.drop('Close', 1)
df = df.drop('High', 1)
df = df.drop('Low', 1)
df = df.drop('Volume_(BTC)',1)
df = df.drop('Volume_(Currency)',1)

# ax = df.set_index('Timestamp').plot(figsize=(12, 8))
# ax.set_ylabel('Price')
# ax.set_xlabel('Date')
# plt.show()

df = df.rename(columns={'Timestamp': 'ds',
                        'Weighted_Price': 'y'})

df['y'] = np.log(df['y'])

my_model = Prophet()
my_model.fit(df)


future_dates = my_model.make_future_dataframe(periods=30)
#print(future_dates.to_string())
forecast = my_model.predict(future_dates)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
my_model.plot(forecast,
              uncertainty=True)