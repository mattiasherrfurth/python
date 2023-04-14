# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:04:46 2019

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

# loading the iris dataset, splitting into testing and training sets
datas = datasets.load_iris()    
X = datas.data
y = datas.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)

#log = LOG()
#poly = POLY(3)
#scale = RS()

#Train a logistic regression model with a polynomilal transform and a robust scalar
pipeline = Pipeline(steps=[
        ('rs', RS()),
        ('poly', POLY(degree=2)),
        ('logistic', LOG())])

pipeline.fit(X_train, y_train)

log_msq = msq(pipeline.predict(X_test), y_test)
log_r2 = r2(pipeline.predict(X_test), y_test)
print('\nThe mean squared error of the Logistic Regression model is: \t\t%s'%log_msq)
print('The R2 score of the Logistic Regression model is: \t\t\t%s'%log_r2)




#pipe = make_pipeline(TfidfVectorizer(), LogisticRegression())
parameters = {'poly__degree': [1,2,5,10],'logistic__C': [1,2,5,10],'logistic__dual':[True,False],'rs__with_centering':[True,False]}
#param_grid = {"logisticregression_C": [0.001, 0.01, 0.1, 1, 10, 100], "tfidfvectorizer_ngram_range": [(1,1), (1,2), (1,3)]}
search = GridSearchCV(pipeline, parameters, cv=5,n_jobs=-1, verbose=1)
search.fit(X_train, y_train)
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)



