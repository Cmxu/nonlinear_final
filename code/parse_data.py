import csv

with open('../data/pokemon.csv', 'r') as csvfile:
	dr = csv.reader(csvfile)
	for row in dr:
		print(row)
