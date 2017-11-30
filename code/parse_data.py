import csv
import numpy as np

data = list()
with open('../data/pokemon.csv', 'r') as csvfile:
    dr = csv.reader(csvfile)
    for row in dr:
        data.append(row)

print (data[0])
data = data[1:] # remove header
data = np.array(data)

# Convert Types to Classes
type1 = list(np.unique(data[:,2]))
type2 = list(np.unique(data[:,3]))
data[:,2] = [type1.index(a)+1 for a in data[:,2]]
data[:,3] = [type2.index(a)+1 for a in data[:,3]]

dt = {row[0]: list(row[2:]) for row in data[:]}