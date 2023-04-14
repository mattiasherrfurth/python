# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:53:13 2019

@author: matti
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# =============================================================================
# TRANSFORMATIONS on ADULT.CSV
# =============================================================================
# load the dataframe
data = pd.read_csv(r'C:\Users\matti\Downloads\adult.csv')
df = data.sample(frac=0.25, random_state=1)
X = df.drop('income', axis=1)
y = df['income']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

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

# =============================================================================
# TRANSFORMATIONS on IRIS
# =============================================================================
# loading the iris dataset
datas = datasets.load_iris()
X = datas.data
y = datas.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)

from sklearn.preprocessing import RobustScaler as RS
from sklearn.preprocessing import PolynomialFeatures as POLY
from sklearn.preprocessing import OneHotEncoder as ONEHOT

# ROBUST SCALER
scaleRS = RS()
fitsRS = scaleRS.fit(X)
rs = pd.DataFrame(fitsRS.transform(X))
rs['income'] = y
robust = rs.dropna(subset=['income'])
robust_train, robust_test = train_test_split(robust)
robust_train_X = robust_train.drop('income',axis=1)
robust_train_y = robust_train['income']

# POLYNOMIAL TRANSFORM
tranPOLY = POLY()
fitsPOLY = tranPOLY.fit(X)
poly = pd.DataFrame(fitsPOLY.transform(X))
poly['income'] = y
polys = poly.dropna(subset=['income'])
polys_train, polys_test = train_test_split(polys)
polys_train_X = polys_train.drop('income',axis=1)
polys_train_y = polys_train['income']

# ONE HOT ENCODER
enc = ONEHOT()
encONE = enc.fit(X)
ohe = pd.DataFrame(encONE.transform(X).toarray())
ohe['income'] = y
hot = ohe.dropna(subset=['income'])
train_df, test_df = train_test_split(hot)

