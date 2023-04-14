# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:53:13 2019

@author: matti
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# loading the iris dataset
datas = datasets.load_iris()
X = datas.data
y = datas.target
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)

# making training and testing dataframes; then setting up X and y dataframes
#train_df, test_df = train_test_split(datas, random_state=1)

# ROBUST SCALER
from sklearn.preprocessing import RobustScaler as RS
scaleRS = RS()
fitsRS = scaleRS.fit(X)
rs = pd.DataFrame(fitsRS.transform(X))
rs['target'] = y
df = rs.dropna(subset=['target'])
df_train, df_test = train_test_split(df)
X_train = df_train.drop('target',axis=1)
y_train = df_train['target']
X_test = df_test.drop('target',axis=1)
y_test = df_test['target']

# =============================================================================
# LINEAR MODEL CLASSIFICATIONS
# =============================================================================

from sklearn.linear_model import LinearRegression as LIN
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet as ENET
from sklearn.linear_model import LogisticRegression as LOG

# LINEAR REGRESSION
#lin = LIN()
#lin.fit(X_train, y_train)
##lin_cm = confusion_matrix(lin.predict(test_df.drop('target',axis=1)), y_test)
##lin_acc = accuracy_score(lin.predict(test_df.drop('target',axis=1)), y_test)
#lin_cm = confusion_matrix(X_test, y_test)
#lin_acc = accuracy_score(X_test, y_test)
#print('The accuracy score of the Linear Regression model is: %s'%lin_acc)
#print('The confusion matrix of the Linear Regression model is: \n%s'%lin_cm)

# LOGISTIC REGRESSION
log = LOG()
log.fit(X_train, y_train)
log_cm = confusion_matrix(log.predict(X_test), y_test)
log_acc = accuracy_score(log.predict(X_test), y_test)
print('The accuracy score of the Logistic Regression model is: %s'%log_acc)
print('The confusion matrix of the Logistic Regression model is: \n%s'%log_cm)

## RIDGE CLASSIFICATION
#ridge = Ridge()
#ridge.fit(X_train, y_train)
#ridge_cm = confusion_matrix(ridge.predict(X_test), y_test)
#ridge_acc = accuracy_score(ridge.predict(X_test), y_test)
#print('The accuracy score of the Ridge model is: %s'%ridge_acc)
#print('The confusion matrix of the Ridge model is: \n%s'%ridge_cm)

## LASSO CLASSIFICATION
#lasso = Lasso()
#lasso.fit(X_train, y_train)
#lasso_cm = confusion_matrix(lasso.predict(X_test), y_test)
#lasso_acc = accuracy_score(lasso.predict(X_test), y_test)
#print('The accuracy score of the Lasso model is: %s'%lasso_acc)
#print('The confusion matrix of the Lasso model is: \n%s'%lasso_cm)

## ELASTICNET CLASSIFICATION
#enet = ENET()
#enet.fit(X_train, y_train)
#enet_cm = confusion_matrix(enet.predict(X_test), y_test)
#enet_acc = accuracy_score(enet.predict(X_test), y_test)
#print('The accuracy score of the ElasticNet model is: %s'%enet_acc)
#print('The confusion matrix of the ElasticNet model is: \n%s'%enet_cm)

# =============================================================================
# TREE CLASSIFICATIONS
# =============================================================================
from sklearn.tree import DecisionTreeRegressor as DTR
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.neighbors import KNeighborsRegressor as KNR
from sklearn.neighbors import KNeighborsClassifier as KNC

# DECISION TREE REGRESSOR
dtr = DTR()
dtr.fit(X_train, y_train)
dtr_cm = confusion_matrix(dtr.predict(X_test), y_test)
dtr_acc = accuracy_score(dtr.predict(X_test), y_test)
print('The accuracy score of the ElasticNet model is: %s'%dtr_acc)
print('The confusion matrix of the ElasticNet model is: \n%s'%dtr_cm)

# DECISION TREE CLASSIFIER
dtc = DTC()
dtc.fit(X_train, y_train)
dtc_cm = confusion_matrix(dtc.predict(X_test), y_test)
dtc_acc = accuracy_score(dtc.predict(X_test), y_test)
print('The accuracy score of the ElasticNet model is: %s'%dtc_acc)
print('The confusion matrix of the ElasticNet model is: \n%s'%dtc_cm)

# K NEAREST NEIGHBORS REGRESSOR
knr = KNR()
knr.fit(X_train, y_train)
knr_cm = confusion_matrix(knr.predict(X_test), y_test)
knr_acc = accuracy_score(knr.predict(X_test), y_test)
print('The accuracy score of the ElasticNet model is: %s'%knr_acc)
print('The confusion matrix of the ElasticNet model is: \n%s'%knr_cm)

# K NEAREST NEIGHBORS CLASSIFIER
knc = KNC()
knc.fit(X_train, y_train)
knc_cm = confusion_matrix(knc.predict(X_test), y_test)
knc_acc = accuracy_score(knc.predict(X_test), y_test)
print('The accuracy score of the ElasticNet model is: %s'%knc_acc)
print('The confusion matrix of the ElasticNet model is: \n%s'%knc_cm)

