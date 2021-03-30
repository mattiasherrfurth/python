# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:53:13 2019

@author: matti
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error as msq
from sklearn.metrics import r2_score as r2
from sklearn.linear_model import LogisticRegression as LOG

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# loading the iris dataset
datas = datasets.load_iris()
X = datas.data
y = datas.target
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)

# making training and testing dataframes; then setting up X and y dataframes
#train_df, test_df = train_test_split(datas, random_state=1)

# POLYNOMIAL TRANSFORM and ROBUST SCALER
from sklearn.preprocessing import PolynomialFeatures as POLY
from sklearn.preprocessing import RobustScaler as RS
poly = POLY(3)
X = poly.fit_transform(X)
scale = RS()
fits = scale.fit(X)
rs = pd.DataFrame(fits.transform(X))
rs['target'] = y
robust = rs.dropna(subset=['target'])
train_df, test_df = train_test_split(robust)
X_train = train_df.drop('target',axis=1)
y_train = train_df['target']
X_test = test_df.drop('target',axis=1)
y_test = test_df['target']

# LOGISTIC REGRESSION
log = LOG()
log.fit(X_train, y_train)
log_msq = msq(log.predict(X_test), y_test)
log_r2 = r2(log.predict(X_test), y_test)
print('\nThe mean squared error of the Logistic Regression model is: \t\t%s'%log_msq)
print('The R2 score of the Logistic Regression model is: \t\t\t%s'%log_r2)

parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc = svm.SVC(gamma="scale")
clf = GridSearchCV(svc, parameters, cv=5)
clf.fit(datas.data, datas.target)
clfs = sorted(clf.cv_results_.keys())

clf_log = GridSearchCV(svc, parameters, cv=5)
clf_log.fit(X_test, y_test)
clfs_log = sorted(clf_log.cv_results_.keys())












## =============================================================================
## LINEAR MODEL CLASSIFICATIONS
## =============================================================================
#
#from sklearn.linear_model import LinearRegression as LIN
#from sklearn.linear_model import Ridge
#from sklearn.linear_model import Lasso
#from sklearn.linear_model import ElasticNet as ENET
#from sklearn.linear_model import LogisticRegression as LOG
#
## LINEAR REGRESSION
#lin = LIN()
#lin.fit(X_train, y_train)
#lin_msq = msq(lin.predict(X_test), y_test)
#lin_r2 = r2(lin.predict(X_test), y_test)
#print('\nThe mean squared error of the Linear Regression model is: \t\t%s'%lin_msq)
#print('The R2 score of the Linear Regression model is: \t\t\t%s'%lin_r2)
#
## LOGISTIC REGRESSION
#log = LOG()
#log.fit(X_train, y_train)
#log_msq = msq(log.predict(X_test), y_test)
#log_r2 = r2(log.predict(X_test), y_test)
#print('\nThe mean squared error of the Logistic Regression model is: \t\t%s'%log_msq)
#print('The R2 score of the Logistic Regression model is: \t\t\t%s'%log_r2)
#
## RIDGE CLASSIFICATION
#ridge = Ridge()
#ridge.fit(X_train, y_train)
#ridge_msq = msq(ridge.predict(X_test), y_test)
#ridge_r2 = r2(ridge.predict(X_test), y_test)
#print('\nThe mean squared error of the Ridge model is: \t\t\t\t%s'%ridge_msq)
#print('The R2 score of the Ridge model is: \t\t\t\t\t%s'%ridge_r2)
#
## LASSO CLASSIFICATION
#lasso = Lasso()
#lasso.fit(X_train, y_train)
#lasso_msq = msq(lasso.predict(X_test), y_test)
#lasso_r2 = r2(lasso.predict(X_test), y_test)
#print('\nThe mean squared error of the Lasso model is: \t\t\t\t%s'%lasso_msq)
#print('The R2 score of the Lasso model is: \t\t\t\t\t%s'%lasso_r2)
#
## ELASTICNET CLASSIFICATION
#enet = ENET()
#enet.fit(X_train, y_train)
#enet_msq = msq(enet.predict(X_test), y_test)
#enet_r2 = r2(enet.predict(X_test), y_test)
#print('\nThe mean squared error of the ElasticNet model is: \t\t\t%s'%enet_msq)
#print('The R2 score of the ElasticNet model is: \t\t\t\t%s'%enet_r2)
#
## =============================================================================
## TREE CLASSIFICATIONS
## =============================================================================
#from sklearn.tree import DecisionTreeRegressor as DTR
#from sklearn.tree import DecisionTreeClassifier as DTC
#from sklearn.neighbors import KNeighborsRegressor as KNR
#from sklearn.neighbors import KNeighborsClassifier as KNC
#
## DECISION TREE REGRESSOR
#dtr = DTR()
#dtr.fit(X_train, y_train)
#dtr_msq = msq(dtr.predict(X_test), y_test)
#dtr_r2 = r2(dtr.predict(X_test), y_test)
#print('\nThe mean squared error of the Decision Tree Regressor model is: \t%s'%dtr_msq)
#print('The R2 score of the Decision Tree Regressor model is: \t\t\t%s'%dtr_r2)
#
## DECISION TREE CLASSIFIER
#dtc = DTC()
#dtc.fit(X_train, y_train)
#dtc_msq = msq(dtc.predict(X_test), y_test)
#dtc_r2 = r2(dtc.predict(X_test), y_test)
#print('\nThe mean squared error of the Decision Tree Classifier model is: \t%s'%dtc_msq)
#print('The R2 score of the Decision Tree Classifier model is: \t\t\t%s'%dtc_r2)
#
## K NEAREST NEIGHBORS REGRESSOR
#knr = KNR()
#knr.fit(X_train, y_train)
#knr_msq = msq(knr.predict(X_test), y_test)
#knr_r2 = r2(knr.predict(X_test), y_test)
#print('\nThe mean squared error of the K Nearest Neighbors Regressor model is: \t%s'%knr_msq)
#print('The R2 score of the K Nearest Neighbors Regressor model is: \t\t%s'%knr_r2)
#
## K NEAREST NEIGHBORS CLASSIFIER
#knc = KNC()
#knc.fit(X_train, y_train)
#knc_msq = msq(knc.predict(X_test), y_test)
#knc_r2 = r2(knc.predict(X_test), y_test)
#print('\nThe mean squared error of the K Nearest Neighbors Classifier model is: \t%s'%knc_msq)
#print('The R2 score of the K Nearest Neighbors Classifier model is: \t\t%s'%knc_r2)
#
