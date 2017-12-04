#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pokemon Challenge (Random Forest Classifier)

@author: xiranliu
"""

import csv
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# Load Pokemon Data
data = list()
with open('../data/pokemon.csv', 'r') as csvfile:
    dr = csv.reader(csvfile)
    for row in dr:
        data.append(row)

print ('Pokemon File:',data[0])
data = data[1:] # remove header
data = np.array(data)

# Convert Types to Classes
type1 = list(np.unique(data[:,2]))
type2 = list(np.unique(data[:,3]))
names = list(data[:,1].astype('str'))
data[:,2] = [type1.index(a)+1 for a in data[:,2]]
data[:,3] = [type2.index(a)+1 for a in data[:,3]]
data[:,-1] = [a=='True' for a in data[:,-1]]

# Process Data
pokeman_data = data[:,4:-1]
pokeman_data = pokeman_data.astype('int')
pokeman_data = np.hstack((data[:,0:1].astype('int'),data[:,2:4].astype('int'),pokeman_data, np.expand_dims(np.array([a=='True' for a in data[:,-1]]).astype('int'),axis=-1)))

dt = {row[0]: row[1:] for row in pokeman_data} # dictionary of pokemon


# Load Combat Data
combats =list() 
with open('../data/combats.csv', 'r') as csvfile:
    dr = csv.reader(csvfile)
    for row in dr:
        combats.append(row)
        
print ('Combats File:',combats[0])
combats = combats[1:]
combats = np.array(combats).astype('int')

p1s = np.array([np.array(dt[r[0]]) for r in combats])
p2s = np.array([np.array(dt[r[1]]) for r in combats])
winners = np.array([r[0]==r[2] for r in combats]).astype('int')
X = np.hstack((p1s,p2s))
y = winners


# Normalization
X = X/np.max(X,axis=0)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# Random Forest
clf = RandomForestClassifier(n_estimators=60)
clf.fit(X, y)
print ('Classifier:',clf)
y_pred = clf.predict(X_test)  

# Performance Measures
accr = accuracy_score(y_test, y_pred)
print ('Accuracy:',accr)
cm = confusion_matrix(y_test, y_pred)
print ('Confusion Matrix:',cm)


