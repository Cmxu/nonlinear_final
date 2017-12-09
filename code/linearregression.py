import csv
import numpy as np
from parse import *
from sklearn import linear_model

data = readData()
[x,y] = parseData(data)