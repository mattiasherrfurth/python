# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:41:50 2019

@author: matti
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd

# Perform a PCA decomposition with 30 components.
digits_data = datasets.load_digits()

X = digits_data.data
y = digits_data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)

# =============================================================================
# you have to align the clustering ot the target values
# 
# =============================================================================











from sklearn.decomposition import PCA

PCA = PCA(n_components=30)
W = PCA.fit_transform(X)
H = PCA.components_

w = pd.DataFrame(data=W)
w['target'] = y

# Attempt KMeans and DBSCAN to separate the data (using the PCA decomposition).
# Report the accuracy of the clusters of both (using the known target data).
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

X = w.drop('target',axis=1)
y = w['target']

kmeans = KMeans(n_clusters=10)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

kmeans_acc = accuracy_score(y_kmeans, y)
kmeans_cm = confusion_matrix(kmeans.predict(X), y)
print('\nThe accuracy score of the KMeans model is: %s'%kmeans_acc)
print('The confusion matrix of the KMeans model is: \n%s'%kmeans_cm)

dbs_acc = accuracy_score(dbs.fit_predict(X), y)
dbs_cm = confusion_matrix(dbs.fit_predict(X), y)
print('\nThe accuracy score of the DBSCAN model is: %s'%dbs_acc)
print('The confusion matrix of the DBSCAN model is: \n%s'%dbs_cm)