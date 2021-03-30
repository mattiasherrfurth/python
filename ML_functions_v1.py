import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
# import tensorflow as tf
import random
import sys
import seaborn as sns

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

### VECTORIZATION FUNCTIONS ###

# let's make functions that return the applied transforms / preprocessing / etc.

# TEXT HANDLING
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer

# ENCODINGS
from sklearn.preprocessing import Binarizer, FunctionTransformer, LabelBinarizer, PolynomialFeatures, RobustScaler

# this function takes in a pandas dataframe and the string representation of the column which will be targeted
def CntVec(df,target):
  # split into X and y datasets
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  # extract numerical and object columns from X dataset
  numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
  X_num = X_init.select_dtypes(include=numerics)
  X_obj = X_init.select_dtypes(include='object')
  # fill an empty dataframe with all the vectorizations of the object columns
  X_vect = pd.DataFrame()
  print('Count vectorizing...')
  for col in X_obj.columns:
    vect = CountVectorizer(binary=True)
    arr = vect.fit_transform(X_obj[col]).toarray()
    dfv = pd.DataFrame(arr)
    X_vect = pd.concat([X_vect, dfv], axis=1, join_axes=[dfv.index])
  # concat the vectorized data and the numeric data
  X_prime = pd.concat([X_vect, X_num], axis=1, join_axes=[X_num.index])
  # drop any NaNs that may have been made (there were few in the landslides vectorization)
  nadrop = pd.concat([X_prime, y_init], axis=1, join_axes=[y_init.index]).dropna()
  print('The vectorized data has shape:',nadrop.shape,'\n')
  return nadrop

def TfdVec(df,target):
  # split into X and y datasets
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  # extract numerical and object columns from X dataset
  numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
  X_num = df.select_dtypes(include=numerics)
  X_obj = df.select_dtypes(include='object')
  # fill an empty dataframe with all the vectorizations of the object columns
  X_vect = pd.DataFrame()
  print('Tfidf vectorizing...')
  for col in X_obj.columns:
    vect = TfidfVectorizer()
    arr = vect.fit_transform(X_obj[col].values.astype('U')).toarray()
    df = pd.DataFrame(arr)
    X_vect = pd.concat([X_vect, df], axis=1, join_axes=[df.index]).dropna()
  # concat the vectorized data and the numeric data
  X_prime = pd.concat([X_vect, X_num], axis=1, join_axes=[X_num.index])
  # drop any NaNs that may have been made (there were few in the landslides vectorization)
  nadrop = pd.concat([X_prime, y_init], axis=1, join_axes=[y_init.index]).dropna()
  print('The vectorized data has shape:',nadrop.shape,'\n')
  return nadrop


### ENCODING FUNCTIONS ###
  
# let's make functions that return the applied transforms / preprocessing / etc.

# ENCODINGS
from sklearn.preprocessing import Binarizer, FunctionTransformer, LabelBinarizer, PolynomialFeatures, RobustScaler

def RobScale(df):
  dum = RobustScaler(with_centering=False)
  print('Robust fitting...')
  fit = dum.fit(df)
  print('Robust scaling...')
  df2 = fit.transform(df)
#   print('Pandas filling...')
  dfit = pd.DataFrame(df2).dropna()
  print('The scaled data has shape:',dfit.shape,'\n')
  return dfit

def Binz(df, target):
  # split into X and y datasets
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  dum = Binarizer()
  scaled = RobScale(df)
  print('Binarizer fitting...')
  fit = dum.fit(scaled)
  print('Binarizer transforming...')
  dfit = pd.DataFrame(fit.transform(scaled))
  # drop any NaNs that may have been made (there were few in the landslides vectorization)
  dfity = pd.concat([dfit, y_init], axis=1, join_axes=[y_init.index]).dropna()
  print('The encoded data has shape:',dfity.shape,'\n\n')
  return dfity
  
def FncTran(df, target):
  # split into X and y datasets
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  dum = FunctionTransformer()
  scaled = RobScale(X_init)
  print('Function transformer fitting...')
  fit = dum.fit(scaled)
  print('Function transforming...')
  dfit = pd.DataFrame(fit.transform(scaled))
  # drop any NaNs that may have been made (there were few in the landslides vectorization)
  dfity = pd.concat([dfit, y_init], axis=1, join_axes=[y_init.index]).dropna()
  print('The encoded data has shape:',dfity.shape,'\n\n')
  return dfity



### CLASSIFICATION FUNCTIONS ###
  
# CLASSIFICATIONS
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

### BACKUP LINES FOR ACCURACY SCORE AND CONFUSION
#   acc_score = accuracy_score(y_test, pred.predict(X_test))  
#   conf_matrix = confusion_matrix(y_test, pred.predict(X_test))
#   print('The accuracy score is: \t\t%s'%acc_score)
#   print('The confusion matrix is:',conf_matrix)

# LINEAR REGRESSION
def LinReg(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = LinearRegression()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred
  
# LOGISTIC REGRESSION
def LogReg(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = LogisticRegression()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred

# RIDGE CLASSIFICATION
def RidgeClass(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = Ridge()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred
  
# LASSO CLASSIFICATION
def LassoClass(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = Lasso()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred
  
# ELASTICNET CLASSIFICATION
def ElastNet(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = ElasticNet()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred
  
# DECISION TREE REGRESSOR
def TreeReg(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = DecisionTreeRegressor()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred
  
# DECISION TREE CLASSIFIER
def TreeClass(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = DecisionTreeClassifier()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred

# K NEAREST NEIGHBORS REGRESSOR
def KNNReg(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = KNeighborsRegressor()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred

# K NEAREST NEIGHBORS CLASSIFIER
def KNNClass(df,target):
  X_init = df.drop(target, axis=1)
  y_init = df[target]
  X_train, X_test, y_train, y_test = train_test_split(X_init,y_init,train_size=0.7,random_state=42)
  pred = KNeighborsClassifier()
  pred.fit(X_train, y_train)
  msq = mean_squared_error(y_test, pred.predict(X_test))
  r2= r2_score(y_test, pred.predict(X_test))
  print('The mean squared error is: \t\t%s'%msq)
  print('The R2 score is: \t\t\t%s'%r2)
  return pred