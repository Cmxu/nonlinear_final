import csv


data = list()
with open('../data/pokemon.csv', 'r') as csvfile:
    dr = csv.reader(csvfile)
    for row in dr:
        print(row)
        data.append(row)

dt = {row[0]: row[1:] for row in data}