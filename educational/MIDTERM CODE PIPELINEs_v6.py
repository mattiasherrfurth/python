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
from sklearn.preprocessing import PolynomialFeatures as POLY
from sklearn.preprocessing import RobustScaler as RS
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)




from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
log = LOG()
poly = POLY(3)
scale = RS()

#logistic = SGDClassifier(loss='log', penalty='l2', early_stopping=True,max_iter=10000, tol=1e-5, random_state=0)
#pca = PCA()
#pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])
pipe = Pipeline(steps=[('poly', poly), ('log', log)])


digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

parameters = {'kernel':('linear', 'rbf', 'poly', 'sigmoid'), 'C':[5,10], 'gamma':[0.001, 0.0001]}

# Parameters of pipelines can be set using ‘__’ separated parameter names:
#param_grid = {'pca__n_components': [5, 20, 30, 40, 50, 64],'logistic__alpha': np.logspace(-4, 4, 5),}
#param_grid = {'poly__n_components': [5, 20, 30, 40, 50, 64],'log__alpha': np.logspace(-4, 4, 5),}
search = GridSearchCV(pipe, iid=False, cv=5,return_train_score=False)
search.fit(X_digits, y_digits)
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)












# =============================================================================
# parameters = {'kernel':('linear', 'rbf', 'poly', 'sigmoid'), 'C':[5,10], 'gamma':[0.001, 0.0001]}
# svc = svm.SVC(gamma="scale")
# GSCV = GridSearchCV(svc, parameters, cv=5)
# 
# # basically a pipeline via a function
# def tran_scale(d):
# #    from sklearn.preprocessing import PolynomialFeatures as POLY
# #    from sklearn.preprocessing import RobustScaler as RS
#     poly = POLY(3)
#     scale = RS()
#     poly_d = poly.fit_transform(d)
#     return(scale.fit_transform(poly_d))
# 
# # loading the iris dataset, splitting into testing and training sets
# datas = datasets.load_iris()    
# X = datas.data
# y = datas.target
# #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)
# 
# digits = datasets.load_digits()
# X_digits = digits.data
# y_digits = digits.target
# 
# #scaleX = tran_scale(X_train)
# #
# #logX = LOG()
# #logX.fit(scaleX, y_train)
# poly = POLY(3)
# scale = RS()
# clf_log = GSCV
# =============================================================================




















##vX = poly.fit_transform(X_train)
##scaleX = scale.fit_transform(vX)
##predicted = log.fit(scaleX, y_train)
#
## Now evaluate all steps on test set
##vX = poly.fit_transform(X_test)
##scaleX = scale.fit_transform(vX)
##predicted = log.fit(scaleX, y_train)
##pipeline = Pipeline(steps=[('poly', POLY(3)),('scale', RS()),('clf_log', GSCV)])
#pipeline = Pipeline(steps=[('poly', poly),('scale', scale),('clf_log', clf_log)])
##predicted = pipeline.fit(X_train).predict(y_train)
#predicted = pipeline.fit(X_train,y_train)
#
#search = GridSearchCV(pipeline, parameters, iid=False, cv=5)
#search.fit(X_train, y_train)
#
##parameters = {'kernel':('linear', 'rbf', 'poly', 'sigmoid'), 'C':[1,5,10], 'gamma':[0.001, 0.0001]}
#param_grid = {'pca__n_components': [5, 20, 30, 40, 50, 64],'logistic__alpha': np.logspace(-4, 4, 5),}
#svc = svm.SVC(gamma="scale")
#earch = GridSearchCV(pipe, param_grid, iid=False, cv=5,return_train_score=False)
#clf_log.fit(X_test, y_test)
#
#
## LOGISTIC REGRESSION
#log = LOG()
#log.fit(X_train, y_train)
#log_msq = msq(log.predict(X_test), y_test)
#log_r2 = r2(log.predict(X_test), y_test)
#print('\nThe mean squared error of the Logistic Regression model is: \t\t%s'%log_msq)
#print('The R2 score of the Logistic Regression model is: \t\t\t%s'%log_r2)
#
## View the best parameters for the model found using grid search
#print('Best C:',search.best_estimator_.C) 
#print('Best Kernel:',search.best_estimator_.kernel)
#print('Best Gamma:',search.best_estimator_.gamma)