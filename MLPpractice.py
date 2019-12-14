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
from sklearn.decomposition import PCA
from sklearn.naive_bayes import MultinomialNB as multi
from sklearn.naive_bayes import GaussianNB as gauss

iris = load_iris()

features = iris.data 
outcome = iris.target

train_features, test_features, train_outcome, test_outcome = train_test_split(features, outcome, train_size = .70, random_state = 43234)

centered_train_features = train_features.copy()
ncols = features.shape[1]
train_col_means = centered_train_features.mean(axis=0)
for i in range(ncols):
    centered_train_features[:,i] = centered_train_features[:,i] - train_col_means[i]

centered_test_features = test_features.copy()
test_col_means = centered_test_features.mean(axis=0)
for i in range(ncols):
    centered_test_features[:,i] = centered_test_features[:,i] - test_col_means[i]

mlp = MLP(hidden_layer_sizes = (2*len(centered_train_features)))
mlp.fit(centered_train_features, train_outcome)
predicted_outcome = mlp.predict(centered_test_features) #don't forget to center the test features
score = accuracy_score(test_outcome, predicted_outcome)
print(score)
# about 82 % accuracy

pca = PCA(train_features.shape[1])
transformed_train_features = pca.fit_transform(train_features)
transformed_test_features = pca.transform(test_features)

mlp = MLP(hidden_layer_sizes = (2*len(transformed_train_features)))
mlp.fit(transformed_train_features, train_outcome)
predicted_outcome = mlp.predict(transformed_test_features)
score = accuracy_score(test_outcome, predicted_outcome)
print(score)
# about 95% accuracy


nb = multi()
nb.fit(train_features, train_outcome)
predicted_outcome = nb.predict(test_features)
multi_score = accuracy_score(predicted_outcome, test_outcome)
print(multi_score)
# about 91% accuracy

nb = gauss()
nb.fit(train_features, train_outcome)
predicted_outcome = nb.predict(test_features)
gauss_score = accuracy_score(predicted_outcome, test_outcome)
print(gauss_score)
#about 95% accuracy

nb = gauss()
nb.fit(transformed_train_features, train_outcome)
predicted_outcome = nb.predict(transformed_test_features)
gauss_score = accuracy_score(test_outcome, predicted_outcome)
print(gauss_score)
# about 91% accuracy
# makes sense that pca doesn't help with naive bayes
# naive bayes assumes that the features are independent condtioned on the outcome
# pca will make the features independent (not conditionally)
# so pca wouldn't be help with fitting these models

