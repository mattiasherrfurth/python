#!/usr/bin/env python
# coding: utf-8

# # IMPORTS
# 
# - importing standard modules for data manipulation
# - importing sklearn tools

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
# import tensorflow as tf
import random
import sys
import seaborn as sns

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[2]:


# GRIDSEARCH
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# SCORING
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, r2_score


# # FUNCTIONS
# - creating functions to take in data and produce vectorizations / scaling / encodings of the data

# # VECTORIZATIONS

# In[3]:


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


# # ENCODINGS

# In[4]:


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


# # CLASSIFICATIONS

# In[5]:


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


# # SETTING UP THE GPU
# - want this to run faster
# - use GPU for rapid simple calculations

# In[6]:


## THIS CODE IS ONLY FOR WORKING IN GOOGLE COLAB ##

# import tensorflow as tf
# device_name = tf.test.gpu_device_name()
# if device_name != '/device:GPU:0':
#   raise SystemError('GPU device not found')
# print('Found GPU at: {}'.format(device_name))


# # GETTING THE DATA
# - We are going to look at a dataset of landslides
# - This could be interesting, or boring. Not sure yet...

# In[7]:


import urllib.request, json 
with urllib.request.urlopen("https://data.nasa.gov/resource/tfkf-kniw.json") as url:
    df = pd.DataFrame(json.loads(url.read().decode()))


# In[8]:


df.head()


# In[9]:


df.shape


# In[10]:


df.dtypes


# In[ ]:


# need to handle for converting all possibly numeric data from their original dtype

for x in df.columns:
  try:
    df[x] = df[x].astype('float')
  except ValueError:
    pass


# In[ ]:


df.dtypes


# In[ ]:


# there are a number of columns that will not help us
#   - source_link
#   - created_date
#   - submitted_date
#   - photo_link
#   - event_description
#   - event_id
#   - event_import_id
#   - event_import_source

cols = ['source_link','created_date','submitted_date','photo_link','event_description','event_id','event_import_id','event_import_source','last_edited_date']

df = df.drop(columns=cols)


# In[ ]:


df.dtypes


# # REVIEWING THE DATA
# - want to see what distributions we have in the dataset for the various fields
# - different data visualizations and characteristics

# In[ ]:


df.describe()


# In[ ]:


import matplotlib.pyplot as plt

# want to see countplots that mean something to us
# get countplots for all columns that have less than 50 unique values

for col in df.columns:
  if df[col].unique().shape[0] < 50:
    sns.countplot(data=df, y=col, palette='Blues_r', order=df[col].value_counts().index)
    plt.show()


# In[ ]:


# there is only one numeric column with less than 20 unique values

# let's see what a scatterplot of the latitude and longitude look like
# and add a hue for the gazeteer distance

fig, ax = plt.subplots(figsize=(14, 8))

sns.scatterplot(x='longitude',y='latitude',hue='gazeteer_distance',data=df)


# In[ ]:


# looks vaguely like a world map, as to be expected
# why are so many gazeteer_distances == 0.0??

# let's use population as a hue

fig, ax = plt.subplots(figsize=(14, 8))

sns.scatterplot(x='longitude',y='latitude',hue='admin_division_population',data=df)


# In[ ]:


# another numeric with many zeroes
# i don't know if modeling will work out well...

# let's try with fatality count

fig, ax = plt.subplots(figsize=(14, 8))

sns.scatterplot(x='longitude',y='latitude',hue='fatality_count',data=df)


# In[ ]:


# more zeroes, but that's to be expected. most recorded landslides are not fatal.

# do fatalities and injuries correlate to size?

# going to get means for counts of fatalities/injuries by landslide_size
# going to reindex to sort plots by size

sizes = ['small','medium','large','very_large','catastrophic']

fatal_means = df[df['landslide_size']!='unknown'].groupby('landslide_size')['fatality_count'].mean().reindex(sizes)

injure_means = df[df['landslide_size']!='unknown'].groupby('landslide_size')['injury_count'].mean().reindex(sizes)


# In[ ]:


fig, ax = plt.subplots(figsize=(14, 8))

fatal_means.plot.bar()


# In[ ]:


fig, ax = plt.subplots(figsize=(14, 8))

injure_means.plot.bar()


# In[ ]:


# looks like fatalities correlate except for catastrophic
# looks like injuries correlate for all sizes

# this would help the modeling

# alright, enough exploration. let's actually get into it.


# In[ ]:


# brk


# # LOOKING FOR A TARGET
# - want to see how many unique values are in columns
# - the ones with the fewest unique values will be best to use for a target

# In[ ]:


# getting a list of dictionaries for unique counts of all columns
# we want to find something to target

unq_cnts = []

for x in df.columns:
  unq_cnts = unq_cnts + [{'cols':x,'cnts':df[x].unique().shape[0]}]


# In[ ]:


unq_cnts


# In[ ]:


# sorting the list, to see if there are targets i can use

col_unqs = sorted(unq_cnts, key = lambda i: i['cnts'])


# In[ ]:


# filtering to only columns with <10 unique elements

targ_cols = col_unqs[0:5]


# In[ ]:


targ_cols


# In[ ]:


# looks like we'll have to use landslide_size and landslide_category

# lets start with landslide_size

print(df.landslide_size.unique())


# 

# # DATA PREPARATION
# - gotta lose all the NaNs in the target
# - want to remove "unknown" from the target, as well (these aren't helpful)
# - need to have something to replace the NaNs in data columns
# - depending on dtype, should use either median for numerics and 'NA' string for objects
# - need to numerize the target (values 1-5)
#   - this is good, less unique values is easier for training

# In[ ]:


# we'll have to fill nans, remove unknowns in all data columns

df = df.dropna(axis=0, subset=['landslide_size'])[df['landslide_size'] != 'unknown']

# creating dictonary of what to fill nans with in each column

values = {'admin_division_name': 'unknown', 'admin_division_population': df.admin_division_population.median(), 'country_code': 'UNK', 
          'country_name': 'NA', 'created_date':'2017-11-20T15:17:00.000', 'event_description':'NA', 
          'fatality_count':df.fatality_count.median(),'gazeteer_closest_point':'NA', 
          'gazeteer_distance':df.gazeteer_distance.median(), 'injury_count':df.injury_count.median(), 'landslide_setting':'NA', 'landslide_trigger':'NA',
          'location_accuracy':'unknown', 'location_description':'NA', 'notes':'NA', 'photo_link':'NA', 'source_link':'NA', 'storm_name':'NA', 'submitted_date':'NA'}

df = df.fillna(value=values)


# In[ ]:


df.dtypes


# In[ ]:


# we have to numerize the target

mapping = {'small':1, 'medium':2, 'large':3, 'very_large':4, 'catastrophic':5}
df = df.replace({'landslide_size':mapping})


# In[ ]:


df.head()


# # TESTING FUNCTIONS ON DIFFERENT DATASETS
# - want to see if the functions that I created would work on multiple datasets
# - this would prove they can be portable

# In[ ]:


from seaborn import load_dataset

data1 = load_dataset('dots')
data2 = load_dataset('fmri')
data3 = load_dataset('exercise')
data4 = load_dataset('planets')


# In[ ]:


data1_CntVec = CntVec(data1, 'time')
data2_CntVec = CntVec(data2, 'timepoint')
data3_CntVec = CntVec(data3, 'kind')
data4_CntVec = CntVec(data4, 'method')


# In[ ]:


data2_CntVec.dtypes


# In[ ]:


# looks like the count vectorization function works for these datasets!

# now let's try the binarizing function

targ = 'timepoint'

data2_Binz = Binz(data2_CntVec, targ)


# In[ ]:


# looks like the binarizing function works for these vectorizations!

# now let's try training a logistic regression via the function

logreg = LogReg(data2_Binz,targ)


# In[ ]:


# all the ML functions look like they are performing well


# # BEGIN ANALYZING THE DATA
# - the functions for ML tools have been tested and are ready for use
# - need to define target before anything

# In[ ]:


# now that we have the data, we can apply the ML functions to it
# we have 2 vectorizations, 2 encodings, and 9 classifications
# the order of application for these functions means there are:
#    - 4 combinations of vectorizers and encoders
#    - 36 total possible combinations of vects/encs/models (4 x 9 = 36)

# i tried using vectorizing functions as the input to the transforming functions, but the tuple from the vectorization was read as one input?...

target = 'landslide_size'


# In[ ]:


# vectorizations

C_vect = CntVec(df, target)
T_vect = TfdVec(df, target)


# In[ ]:


# encodings

CntFnc = FncTran(C_vect, target)
TfdFnc = FncTran(T_vect, target)
CntBin = Binz(C_vect, target)
TfdBin = Binz(T_vect, target)


# In[ ]:


# # classifications

print('\n\n**** MODEL = LINEAR REGRESSION *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncLin = LinReg(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncLin = LinReg(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinLin = LinReg(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinLin = LinReg(TfdBin,target)

print('\n\n**** MODEL = LOGISTIC REGRESSION *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncLog = LogReg(CntFnc,target)
#print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
#TfdFncLog = LogReg(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinLog = LogReg(CntBin,target)
#print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
#TfdBinLog = LogReg(TfdBin,target)

print('\n\n**** MODEL = RIDGE CLASSIFIER *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncRidge = RidgeClass(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncRidge = RidgeClass(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinRidge = RidgeClass(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinRidge = RidgeClass(TfdBin,target)

print('\n\n**** MODEL = LASSO CLASSIFIER *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncLasso = LassoClass(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncLasso = LassoClass(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinLasso = LassoClass(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinLasso = LassoClass(TfdBin,target)

print('\n\n**** MODEL = ELASTIC NET *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncElast = ElastNet(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncElast = ElastNet(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinElast = ElastNet(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinElast = ElastNet(TfdBin,target)

print('\n\n**** MODEL = DECISION TREE REGRESSOR *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncTreeReg = TreeReg(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncTreeReg = TreeReg(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinTreeReg = TreeReg(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinTreeReg = TreeReg(TfdBin,target)

print('\n\n**** MODEL = DECISION TREE CLASSIFIER *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncTreeClass = TreeClass(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncTreeClass = TreeClass(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinTreeClass = TreeClass(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinTreeClass = TreeClass(TfdBin,target)

print('\n\n**** MODEL = KNN REGRESSOR *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncKNNReg = KNNReg(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncKNNReg = KNNReg(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinKNNReg = KNNReg(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinKNNReg = KNNReg(TfdBin,target)

print('\n\n**** MODEL = KNN CLASSIFIER *********************')
print('\n\tFEATURE ENGINEERING = CountVectorizer + FunctionTransformer')
CntFncKNNClass = KNNClass(CntFnc,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + FunctionTransformer')
TfdFncKNNClass = KNNClass(TfdFnc,target)
print('\n\n\tFEATURE ENGINEERING = CountVectorizer + Binarizer')
CntBinKNNClass = KNNClass(CntBin,target)
print('\n\n\tFEATURE ENGINEERING = TfidfVectorizer + Binarizer')
TfdBinKNNClass = KNNClass(TfdBin,target)


# # Notes on Classifications
# - the r2 score doesn't help us much unless we are talking about linear/logistic regression
# - the mean squared error is always helpful, identifying how far our samples are on average from the model
# 
# # RESULTS
# - based on the mean squared error we can see that:
#   - Lasso and ElasticNet models predict with highest accuracy
#   - the two vectorizations for these two classifications produce Lasso/ENet models with similar accuracy
#   - the Binarizer produces a slightly more accurate Lasso/ENet model than the FunctionTransformer

# # GRID SEARCHING
# - picking the following combination of methods to include in the pipeline:
#   - CountVectorizer
#   - Binarizer
#   - RobustScaler
#   - ElasticNet

# In[ ]:


# REFRESHING THE DATA SOURCE

import urllib.request, json 
with urllib.request.urlopen("https://data.nasa.gov/resource/tfkf-kniw.json") as url:
    df = pd.DataFrame(json.loads(url.read().decode()))

# what if we implemented the vectorization here?...
for x in df.columns:
  try:
    df[x] = df[x].astype('float')
  except ValueError:
    pass
    
# we'll have to fill nans, remove unknowns in all data columns
df = df.dropna(axis=0, subset=['landslide_size'])[df['landslide_size'] != 'unknown']

# creating dictonary of what to fill nans with in each column
values = {'admin_division_name': 'unknown', 'admin_division_population': df.admin_division_population.median(), 'country_code': 'UNK', 
          'country_name': 'NA', 'created_date':'2017-11-20T15:17:00.000', 'event_description':'NA', 'event_import_id': df.event_import_id.mean(), 
          'event_import_source': 'NA', 'fatality_count':df.fatality_count.median(),'gazeteer_closest_point':'NA', 
          'gazeteer_distance':df.gazeteer_distance.median(), 'injury_count':df.injury_count.median(), 'landslide_setting':'NA', 'landslide_trigger':'NA',
          'location_accuracy':'unknown', 'location_description':'NA', 'notes':'NA', 'photo_link':'NA', 'source_link':'NA', 'storm_name':'NA', 'submitted_date':'NA'}
df = df.fillna(value=values)

# we have to numerize the target
mapping = {'small':1, 'medium':2, 'large':3, 'very_large':4, 'catastrophic':5}
df = df.replace({'landslide_size':mapping})

# dropping unnecessary columns
cols = ['source_link','created_date','submitted_date','photo_link','event_description']
df = df.drop(columns=cols)

# vectorizing the data
df = CntVec(df, 'landslide_size')


# In[ ]:


target = 'landslide_size'

X = df.drop(target, axis=1).as_matrix()
y = df[target].as_matrix()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)


# In[ ]:


pipeline = Pipeline(steps=[
    ('rs', RobustScaler()),
    ('binz', Binarizer()),
    ('en', ElasticNet())])

pipeline.fit(X_train, y_train)


# In[ ]:


# LITTLE SEARCH

parameters = {'rs__with_centering':[True],
              'rs__with_scaling':[True],
#               'rs__copy':[True,False],
#               'binz__copy':[True,False],
              'binz__threshold':[3.15,3.2,3.25,3.3],
              'en__alpha':[0.0,0.5],
#               'en__l1_ratio':[0.0,0.25],
              'en__fit_intercept':[True,False],
              'en__normalize':[True,False],
#               'en__precompute':[True,False],
#               'en__warm_start':[True,False],
#               'en__positive':[True,False]
             }

search = GridSearchCV(pipeline, parameters, cv=5,n_jobs=-1, verbose=3)
search.fit(X_train, y_train)
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)


# In[ ]:


# # BIG SEARCH

# parameters = {'rs__with_centering':[True],
#               'rs__with_scaling':[True],
#               'rs__copy':[True,False],
#               'binz__copy':[True,False],
#               'binz__threshold':[3.15,3.2,3.25,3.3],
#               'en__alpha':[0.0,0.5],
#               'en__l1_ratio':[0.0,0.25],
#               'en__fit_intercept':[True,False],
#               'en__normalize':[True,False],
#               'en__precompute':[True,False],
#               'en__warm_start':[True,False],
#               'en__positive':[True,False]
#              }

# search = GridSearchCV(pipeline, parameters, cv=5,n_jobs=-1, verbose=3)
# search.fit(X_train, y_train)
# print("Best parameter (CV score=%0.3f):" % search.best_score_)
# print(search.best_params_)

