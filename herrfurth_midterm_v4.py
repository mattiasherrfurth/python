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

X_pca = w.drop('target',axis=1)
y_pca = w['target']

kmeans = KMeans(n_clusters=2, random_state=0).fit_transform(X_pca)
dbs = DBSCAN(eps=3, min_samples=2).fit(kmeans)






#from sklearn.neighbors import KNeighborsClassifier as KNN
#from sklearn.metrics import r2_score as r2
#
#X_pca = w.drop('target',axis=1)
#y_pca = w['target']
#
#X_pca_train, X_pca_test, y_pca_train, y_pca_test = train_test_split(X, y, test_size=0.5, random_state=2)




