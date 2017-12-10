import csv
from datetime import datetime

target = open("../data/data.csv","w")
target.write("Timestamp,Weighted_Price")
target.write('\n')

with open('../data/bitstampUSD_1-min_data_2012-01-01_to_2017-10-20.csv', 'r') as csvfile:
  dr = csv.reader(csvfile)
  i = 0
  for row in dr:
    if (row[0] != 'Timestamp'):
      time = datetime.fromtimestamp(int(row[0]))
      if (time.year == 2017):
        target.write(row[0]+","+row[7])
        target.write('\n')


