# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:53:13 2019

@author: matti
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# load the dataframe
#data = pd.read_csv(io.StringIO(uploaded['adult.csv'].decode('utf-8')))
data = pd.read_csv(r'C:\Users\matti\Downloads\adult.csv')

# getting a random sample of the dataset
# the full dataset was causing the kernel to crash
# this sample will be 1/4 the original dataset
df = data.sample(frac=0.25, random_state=1)

# splitting dataset into features and targets
X = df.drop('income', axis=1)
y = df['income']

# splitting into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)

# =============================================================================
# TRANSFORMATIONS
# =============================================================================
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import RobustScaler as RS
from sklearn.preprocessing import PolynomialFeatures as POLY
from sklearn.preprocessing import OneHotEncoder as ONEHOT
from sklearn.preprocessing import LabelBinarizer as LB

# vectorizer = CountVectorizer(binary=True)
vectC = CountVectorizer(binary=True)
vectC_train = vectC.fit_transform(X_train)
vectC_test = vectC.transform(X_test)

# vectorizer = HashingVectorizer()
vectH = HashingVectorizer()
vectH_train = vectH.fit_transform(X_train)
vectH_test = vectH.transform(X_test)

# vectorizer = HashingVectorizer()
vectTfid = TfidfVectorizer()
vectTfid_train = vectTfid.fit_transform(X_train)
vectTfid_test = vectTfid.transform(X_test)

# using a robust scaler
scale = RS()
fits = scale.fit(X)
rs = pd.DataFrame(fits.transform(X))
rs['income'] = y
robust = rs.dropna(subset=['income'])

# making testing and training sets
robust_train, robust_test = train_test_split(robust)
robust_train_X = robust_train.drop('income',axis=1)
robust_train_y = robust_train['income']

# =============================================================================
# CLASSIFICATIONS
# =============================================================================

#from sklearn.linear_model import LinearRegression as LIN
#from sklearn.linear_model import Ridge
#from sklearn.linear_model import Lasso
#from sklearn.linear_model import ElasticNet as ENET
#from sklearn.linear_model import LogisticRegression as LOG
#
## fitting models using the encoded features
#log = LOG()
##log.fit(train_df.drop('income',axis=1), train_df['income'])
#log.fit(X_train, y_train)
#rf = RF()
#rf.fit(X_train, y_train)