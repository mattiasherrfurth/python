# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:31:16 2019

@author: J20032
"""

# =============================================================================
# NOTE: at any time, you can type 'help(x)' into a console to get help with
# a module, method, etc.

# for example, if I wanted to know more about pandas I would enter:
#   >>> import pandas as pd
#   >>> help(pd)

# this would then give me some resources to help understand the module

# alternatively, Google exists


# for comments I have written that have "quotation marks" around them, 
# those are pulled directly from the help() function
# =============================================================================



# =============================================================================
# IMPORT PANDAS AND TRAIN-TEST-SPLIT
# =============================================================================

# pandas is a module used for working with dataframes / datasets
# pandas dataframes are supported by many other modules, as well
# this means I can use a pandas dataframe to teach an sklearn model
import pandas as pd

# sklearn is a module that has many tools for machine learning
# sklearn has preprocessing, encoding, modeling, scoring, and much more
from sklearn.model_selection import train_test_split


# =============================================================================
# LOAD THE DATA
# =============================================================================

# read data from a csv, excel, or other
# pandas is reading in csv or excel files
data = pd.read_csv(r'[your filepath here]')
data = pd.read_excel(r'[your filepath here]')

# this is an example line from code I wrote
#data = pd.read_csv(r'C:\Users\matti\Downloads\adult.csv')

# split the data into inputs and output (i.e. features and target
# pandas is taking the dataframe and doing the following:
#   - removing the target column to leave just the features for inputs (X)
#   - taking only the target column to make the output (y)
X = df.drop('target', axis=1)
y = df['target']

# split the data into training and testing sets
# sklearn.train_test_split is taking the data, randomizing it, and pulling out 
# dataframes to use for training the model, and then testing the model
# for this case, we are making the training data to be 80% of the initial dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# =============================================================================
# TRANSFORM THE DATA
# =============================================================================

# depending on the type of data you have, you may need to transform it
# for example, categorical data will need to be converted to numeric data
# for example, numeric data may have columns that are different orders of 
#   magnitude than other columns (need to scale the data)

# these are all the options that I know of for transforming
# recommend use one at a time to see which one produces a more robust model

# importing some transformation tools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import OneHotEncoder

# "Convert a collection of text documents to a matrix of token counts"
# this will convert categorical arrays to numeric arrays
#   right now, I am converting the features for the training and testing inputs
X_vectC = CountVectorizer(binary=True)
X_vectC_train = X_vectC.fit_transform(X_train)
X_vectC_test = X_vectC.transform(X_test)

# "Convert a collection of text documents to a matrix of token occurrences"
# this will also convert categorical arrays to numeric arrays
#   right now, I am converting the features for the training and testing inputs
X_vectH = HashingVectorizer()
X_vectH_train = X_vectH.fit_transform(X_train)
X_vectH_test = X_vectH.transform(X_test)

# "Convert a collection of raw documents to a matrix of TF-IDF features."
# "Equivalent to CountX_vectorizer followed by TfidfTransformer."
# this will both convert categorical data to numeric, then transform it
X_vectTfid = TfidfVectorizer()
X_vectTfid_train = X_vectTfid.fit_transform(X_train)
X_vectTfid_test = X_vectTfid.transform(X_test)

# "Scale features using statistics that are robust to outliers."
# this will improve the training of a model
# it will scale the data based on the interquartile range
#   right now, I am scaling the features in the full dataset, 
#   then splitting them into training and testing sets
scaleRS = RobustScaler()
fitsRS = scaleRS.fit(X)
rs = pd.DataFrame(fitsRS.transform(X))
rs['target'] = y
robust = rs.dropna(subset=['target'])
robust_train, robust_test = train_test_split(robust)
robust_X_train = robust_train.drop('target',axis=1)
robust_y_train = robust_train['target']
robust_X_test = robust_test.drop('target',axis=1)
robust_y_test = robust_test['target']

# "Generate polynomial and interaction features."
# this will improve the information extracted from features
# new features will be added which are based on current features
#   right now, I am converting the features in the full dataset, 
#   then splitting them into training and testing sets
tranPOLY = PolynomialFeatures()
fitsPOLY = tranPOLY.fit(X)
poly = pd.DataFrame(fitsPOLY.transform(X))
poly['target'] = y
polys = poly.dropna(subset=['target'])
polys_train, polys_test = train_test_split(polys)
polys_X_train = polys_train.drop('target',axis=1)
polys_y_train = polys_train['target']
polys_X_test = polys_test.drop('target',axis=1)
polys_y_test = polys_test['target']

# "Encode categorical integer features using a one-hot aka one-of-K scheme."
# this will convert any array of features into a binary array
# the resulting array will indicate the counts for feature values in each entry
#   right now, I am encoding the features in the full dataset, 
#   then splitting them into training and testing sets
enc = OneHotEncoder()
encONE = enc.fit(X)
ohe = pd.DataFrame(encONE.transform(X).toarray())
ohe['target'] = y
hot = ohe.dropna(subset=['target'])
ohe_train, ohe_test = train_test_split(hot)
ohe_X_train = ohe_train.drop('target',axis=1)
ohe_y_train = ohe_train['target']
ohe_X_test = ohe_test.drop('target',axis=1)
ohe_y_test = ohe_test['target']

# =============================================================================
# MODEL THE DATA (LINEAR)
# =============================================================================

# these are mathematical models based on regression analysis
# there are many ways to score models based on their accuracy
# here I have used the mean squared error and R2 score, since these
# are metrics for linear models


# importing model tools
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LogisticRegression

# importing scoring tools
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# LINEAR REGRESSION
# "Ordinary least squares Linear Regression."
#   this will use linear regression to model the relationship
lin = LinearRegression()
lin.fit(X_train, y_train)
lin_msq = mean_squared_error(lin.predict(X_test), y_test)
lin_r2 = r2_score(lin.predict(X_test), y_test)
print('\nThe mean squared error of the Linear Regression model is: \t\t%s'%lin_msq)
print('The R2 score of the Linear Regression model is: \t\t\t%s'%lin_r2)

# LOGISTIC REGRESSION
log = LogisticRegression()
log.fit(X_train, y_train)
log_msq = mean_squared_error(log.predict(X_test), y_test)
log_r2 = r2_score(log.predict(X_test), y_test)
print('\nThe mean squared error of the Logistic Regression model is: \t\t%s'%log_msq)
print('The R2 score of the Logistic Regression model is: \t\t\t%s'%log_r2)

# RIDGE CLASSIFICATION
# "Linear least squares with l2 regularization."
ridge = Ridge()
ridge.fit(X_train, y_train)
ridge_msq = mean_squared_error(ridge.predict(X_test), y_test)
ridge_r2 = r2_score(ridge.predict(X_test), y_test)
print('\nThe mean squared error of the Ridge model is: \t\t\t\t%s'%ridge_msq)
print('The R2 score of the Ridge model is: \t\t\t\t\t%s'%ridge_r2)

# LASSO CLASSIFICATION
# "Linear Model trained with L1 prior as regularizer"
lasso = Lasso()
lasso.fit(X_train, y_train)
lasso_msq = mean_squared_error(lasso.predict(X_test), y_test)
lasso_r2 = r2_score(lasso.predict(X_test), y_test)
print('\nThe mean squared error of the Lasso model is: \t\t\t\t%s'%lasso_msq)
print('The R2 score of the Lasso model is: \t\t\t\t\t%s'%lasso_r2)

# ELASTICNET CLASSIFICATION
# "Linear regression with combined L1 and L2 priors as regularizer."
enet = ElasticNet()
enet.fit(X_train, y_train)
enet_msq = mean_squared_error(enet.predict(X_test), y_test)
enet_r2 = r2_score(enet.predict(X_test), y_test)
print('\nThe mean squared error of the ElasticNet model is: \t\t\t%s'%enet_msq)
print('The R2 score of the ElasticNet model is: \t\t\t\t%s'%enet_r2)

# =============================================================================
# MODEL THE DATA (TREE)
# =============================================================================
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier

# DECISION TREE REGRESSOR
# this is a decision tree model that uses regression to predict
dtr = DecisionTreeRegressor()
dtr.fit(X_train, y_train)
dtr_msq = mean_squared_error(dtr.predict(X_test), y_test)
dtr_r2 = r2_score(dtr.predict(X_test), y_test)
print('\nThe mean squared error of the Decision Tree Regressor model is: \t%s'%dtr_msq)
print('The R2 score of the Decision Tree Regressor model is: \t\t\t%s'%dtr_r2)

# DECISION TREE CLASSIFIER
# this is a decision tree model that goes by a flowchart structure
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
dtc_msq = mean_squared_error(dtc.predict(X_test), y_test)
dtc_r2 = r2_score(dtc.predict(X_test), y_test)
print('\nThe mean squared error of the Decision Tree Classifier model is: \t%s'%dtc_msq)
print('The R2 score of the Decision Tree Classifier model is: \t\t\t%s'%dtc_r2)

# K NEAREST NEIGHBORS REGRESSOR
# similar to tree, this is a model that uses regression to characterize
# based on nearest neighbors
knr = KNeighborsRegressor()
knr.fit(X_train, y_train)
knr_msq = mean_squared_error(knr.predict(X_test), y_test)
knr_r2 = r2_score(knr.predict(X_test), y_test)
print('\nThe mean squared error of the K Nearest Neighbors Regressor model is: \t%s'%knr_msq)
print('The R2 score of the K Nearest Neighbors Regressor model is: \t\t%s'%knr_r2)

# K NEAREST NEIGHBORS CLASSIFIER
# similar to tree, this is a model that uses classification to characterize
# based on nearest neighbors
knc = KNeighborsClassifier()
knc.fit(X_train, y_train)
knc_msq = mean_squared_error(knc.predict(X_test), y_test)
knc_r2 = r2_score(knc.predict(X_test), y_test)
print('\nThe mean squared error of the K Nearest Neighbors Classifier model is: \t%s'%knc_msq)
print('The R2 score of the K Nearest Neighbors Classifier model is: \t\t%s'%knc_r2)