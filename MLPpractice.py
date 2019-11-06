#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:57:54 2019

@author: du_ds
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier as MLP
from sklearn.metrics import accuracy_score

iris = load_iris()

features = iris.data 
outcome = iris.target

train_features, test_features = train_test_split(features)
train_outcome, test_outcome = train_test_split(outcome)


centered_train_features = train_features.copy()
ncols = centered_train_features.shape[1]
col_means = centered_train_features.mean(axis=0)
for i in range(ncols):
    centered_train_features[:,i] = centered_train_features[:,i] - col_means[i]

mlp = MLP(hidden_layer_sizes = (100))
mlp.fit(centered_train_features, train_outcome)
predicted_outcome = mlp.predict(test_features)
score = accuracy_score(test_outcome, predicted_outcome)
print(score)



