# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:08:04 2019

@author: matti
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler as RS

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

digits_data = datasets.load_digits()

X = digits_data.data
y = digits_data.target

from sklearn.decomposition import PCA

PCA = PCA(n_components=30)
W = PCA.fit_transform(X)
H = PCA.components_

w = pd.DataFrame(data=W)
w['target'] = y

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

X_pca = w.drop('target',axis=1)
y_pca = w['target']

X_train, X_test, y_train, y_test = train_test_split(X_pca, y_pca, test_size=0.5, random_state=2)

kmeans = KMeans(n_clusters=10).fit(X_train)
dbs = DBSCAN(eps=3, min_samples=10).fit(X_train)

kmeans_acc = accuracy_score(kmeans.predict(X_test), y_test)
kmeans_cm = confusion_matrix(kmeans.predict(X_test), y_test)
print('\nThe accuracy score of the KMeans model is: %s'%kmeans_acc)
print('The confusion matrix of the KMeans model is: \n%s'%kmeans_cm)

dbs_acc = accuracy_score(dbs.fit_predict(X_test), y_test)
dbs_cm = confusion_matrix(dbs.fit_predict(X_test), y_test)
print('\nThe accuracy score of the KMeans model is: %s'%dbs_acc)
print('The confusion matrix of the KMeans model is: \n%s'%dbs_cm)










#knn = KNN(n_neighbors=3)
#knn.fit(X_train, y_train)
#knn_acc = accuracy_score(knn.predict(X_test), y_test)
#knn_cm = confusion_matrix(knn.predict(X_test), y_test)
#print('\nThe accuracy score of the model is: %s'%knn_acc)
#print('The confusion matrix of the model is: \n%s'%knn_cm)












#from sklearn.cluster import KMeans
#from sklearn.cluster import DBSCAN
#
#X_pca = w.drop('target',axis=1)
#y_pca = w['target']
#
#kmeans = KMeans(n_clusters=2, random_state=0).fit_transform(X_pca)
#dbs = DBSCAN(eps=3, min_samples=2).fit(kmeans)











