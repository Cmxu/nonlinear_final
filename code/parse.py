import csv
import numpy as np
from datetime import datetime


data = list()
with open('../data/bitstampUSD_1-min_data_2012-01-01_to_2017-10-20.csv', 'r') as csvfile:
    dr = csv.reader(csvfile)
    for row in dr:
        if(row[0] != 'Timestamp'):
            time =  datetime.fromtimestamp(int(row[0]))
            row[0] = time
            data.append(row)

print ('Bitcoin File:',data[0])
#data = data[1:] # remove header
data = np.array(data)

