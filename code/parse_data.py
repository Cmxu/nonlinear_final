import csv
import numpy as np

data = list()
with open('../data/pokemon.csv', 'r') as csvfile:
    dr = csv.reader(csvfile)
    for row in dr:
        data.append(row)

print (data[0])
data = data[1:]
dt = {row[0]: row[1:] for row in data}
data = np.array(data)

# Types
type1 = list(np.unique(data[:,2]))
type2 = list(np.unique(data[:,3]))

type1class = [type1.index(a)+1 for a in data[:,2]]
type2class = [type2.index(a)+1 for a in data[:,3]]