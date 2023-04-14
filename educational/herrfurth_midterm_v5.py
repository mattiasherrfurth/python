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

df_train, df_test = train_test_split(w, test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

X_train = df_train.drop('target',axis=1)
y_train = df_train['target']
X_test = df_test.drop('target',axis=1)
y_test = df_test['target']


knn = KNN(n_neighbors=3)
knn.fit(X_train, y_train)
knn_acc = accuracy_score(knn.predict(X_test), y_test)
knn_cm = confusion_matrix(knn.predict(X_test), y_test)
print('\nThe accuracy score of the model is: %s'%knn_acc)
print('The confusion matrix of the model is: \n%s'%knn_cm)












#from sklearn.cluster import KMeans
#from sklearn.cluster import DBSCAN
#
#X_pca = w.drop('target',axis=1)
#y_pca = w['target']
#
#kmeans = KMeans(n_clusters=2, random_state=0).fit_transform(X_pca)
#dbs = DBSCAN(eps=3, min_samples=2).fit(kmeans)











