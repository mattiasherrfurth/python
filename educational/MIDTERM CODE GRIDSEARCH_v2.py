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
warnings.filterwarnings("ignore", category=DeprecationWarning)

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

#parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
#parameters = {'kernel':('linear', 'rbf', 'poly', 'sigmoid', 'precomputed'), 'C':[1,5,10], 'gamma':[0.001, 0.0001]}
parameters = {'kernel':('linear', 'rbf', 'poly', 'sigmoid'), 'C':[1,5,10], 'gamma':[0.001, 0.0001]}
#svc = svm.SVC(C=1, parameters)
#clf_log = GridSearchCV(svc, parameters, cv=5)
svc = svm.SVC(gamma="scale")
clf_log = GridSearchCV(svc, parameters, cv=5)
clf_log.fit(X_test, y_test)
print('Best score for iris dataset with a polynomial transform and a robust scaler is:', clf_log.best_score_)
#clfs_log = sorted(clf_log.cv_results_.keys())

# View the best parameters for the model found using grid search
print('Best C:',clf_log.best_estimator_.C) 
print('Best Kernel:',clf_log.best_estimator_.kernel)
print('Best Gamma:',clf_log.best_estimator_.gamma)