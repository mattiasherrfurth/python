# -*- coding: utf-8 -*-
"""hw6_mtokay.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnbFx_5clds-3e_lBa6RHTyxrHJdXASt

**DATA602 - Introduction to Machine Learning - 5th Homework**

***Dr. Darin Johnson***

*Student:* Maura Tokay

*Grader:* Mattias Herrfurth
"""

import io
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests # requests is a handy http library
import seaborn as sns
import tensorflow as tf
import zipfile # a zip library

from __future__ import print_function
from google.colab import files
from matplotlib import pylab
from pydot import graph_from_dot_data
from sklearn import datasets
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression, LinearRegression, RidgeClassifier
from sklearn.metrics import confusion_matrix, mean_squared_error, accuracy_score, roc_auc_score, roc_curve, auc, f1_score, \
                            precision_score, recall_score, classification_report, r2_score, precision_recall_curve, \
                            average_precision_score
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, cross_val_predict, cross_validate
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, RobustScaler, Normalizer, MinMaxScaler, StandardScaler, Binarizer
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_graphviz
from sklearn.utils import shuffle
from sklearn.utils.fixes import signature
from time import time
from yellowbrick.features.importances import FeatureImportances

# Function to normalize data frame
def normalize(dataset):
  dataNorm=(dataset-dataset.min())/(dataset.max()-dataset.min())
  #dataNorm["diagnosis"]=dataset["diagnosis"]
  return dataNorm
  
# Function to describe the data
def describeData(dataset):
  # Show first 5 rows of data
  print("Display first 5 rows.\n")
  print(dataset.head(),"\n")
  print("--------------------------------------------------------------------")
  # Show basic data statistics
  print("Data basic statistics.\n")
  print(dataset.describe(),"\n")
  print("--------------------------------------------------------------------")
  # Show correlation among variables
  print("Data correlation.\n")
  ct = dataset.corr()
  print(ct,"\n")
  print("--------------------------------------------------------------------")
  # Show heatmap of Correlation Matrix
  plt.figure(figsize=(10,8))
  sns.heatmap(ct, cbar = True, square = True, annot=True, linewidths = .5, fmt='.2f',annot_kws={'size': 10}) 
  plt.title('Heatmap of Correlation Matrix')
  plt.show()
  print("--------------------------------------------------------------------")
  # Generate scatter plots
  #g = sns.pairplot(dataset, hue="target")
  #g._legend.remove()
  #plt.legend(bbox_to_anchor=(1.05, 10), loc=2, ncol=2, borderaxespad=0.)
  
# Function to evaluate model
def modelStatsReport(model,X,y,label=""):
  # Calculate confusion matrix
  y_pred = model.predict(X)
  confusion = confusion_matrix(y,y_pred)
  print("Confusion matrix:\n",confusion)
  print("--------------------------------------------------------------------")
  
  # Calculate score
  score = model.score(X,y)
  print("Score = {:.5f}".format(score))
  print("--------------------------------------------------------------------")
    
  # Mean squared error
  #mse = mean_squared_error(y_pred, y)
  #print("Mean squared error = {:.5f}".format(mse))

  # Coefficient of determination (Best is 1)
  #r2 = r2_score(y_pred, y)
  #print("Coefficient of determination = {:.5f}".format(r2))
  
  # Calculate accuracy score
  acc_score = accuracy_score(y,y_pred)
  print("Accuracy Score = {:.5f}".format(acc_score))
  print("--------------------------------------------------------------------")
  
  # Calculate recall score
  if label != "":
    rec_score = recall_score(y,y_pred,pos_label=label)
  else:
    rec_score = recall_score(y,y_pred,average=None)
  print("Recall Score = ",rec_score)
  print("--------------------------------------------------------------------")
  
  # Calculate precision score
  if label != "":
    prec_score = precision_score(y,y_pred,pos_label=label)
  else:
    prec_score = precision_score(y,y_pred,average=None)
  print("Precision Score = ",prec_score)
  print("--------------------------------------------------------------------")
  
  # Calculate f1 score
  if label != "":
    f1 = f1_score(y,y_pred,pos_label=label)
  else:
    f1 = f1_score(y_pred,y,average=None)
  print("F1 Score = ",f1)
  print("--------------------------------------------------------------------")
  
  # Classification report
  print("Classification report:\n", classification_report(y,y_pred)) 
  print("--------------------------------------------------------------------")
    
  # Check for feature importance
  if hasattr(model, 'feature_importances_') or hasattr(model, 'coef_'):
    # Create a new matplotlib figure
    fig = plt.figure()
    ax = fig.add_subplot()

    viz = FeatureImportances(model, ax=ax, absolute=True)
    viz.fit(X,y)
    viz.poof()
  else:
    print("Can't estimate feature importance.")

"""*Problem 1* - Feature Engineering Homework

- Sklearn has sklearn.preprocessing.OneHotEncoder, try to implement it on the adult.csv dtaset instead of using the above using get_dummies. Also, try get_dummies without the columns argument, how did it go?
- Train a logistic regression model with a robust scalar.
- Train a logistic regression model with a polynomilal transform and a robust scalar
"""

# Uploaded a file to Colab (I'll share this via drive with the class).
uploaded = files.upload()

# Normally, you could just use filename.
data = pd.read_csv(io.StringIO(uploaded['adult.csv'].decode('utf-8')))

data.head()

data_transformed = pd.get_dummies(data, columns=['workclass', 'education', 'educational-num', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country'])

data_transformed.head()

train_df, test_df = train_test_split(data_transformed)

lr = LogisticRegression()
lr.fit(train_df.drop('income', axis=1), train_df['income'])

print("Performance summary for Logistic Regression using get_dummies.\n")
modelStatsReport(lr,test_df.drop('income',axis=1),test_df['income'],label='<=50K')

# Now going through the same process using get_dummies without column argument
data_transformed_nc = pd.get_dummies(data)

data_transformed_nc.head()

train_nc_df, test_nc_df = train_test_split(data_transformed_nc)

lr_nc = LogisticRegression()
lr_nc.fit(train_nc_df.drop('income_<=50K', axis=1), train_nc_df['income_<=50K'])

print("Performance summary for Logistic Regression using get_dummies (no columns income <= 50K).\n")
modelStatsReport(lr_nc,test_nc_df.drop('income_<=50K',axis=1),test_nc_df['income_<=50K'])

lr_nc = LogisticRegression()
lr_nc.fit(train_nc_df.drop('income_>50K', axis=1), train_nc_df['income_>50K'])

print("Performance summary for Logistic Regression using get_dummies (no columns income > 50K).\n")
modelStatsReport(lr_nc,test_nc_df.drop('income_>50K',axis=1),test_nc_df['income_>50K'])

"""The accuracy didn't change much when using get_dummies with and without column specification."""

# Test now logistic regression with onehotencoder
# OneHotEncoder should only apply to categorical features

# Select the numeric columns
numeric_subset = data.select_dtypes('number')

# Select categorical columns
categorical_subset = data.select_dtypes('object')

# Apply OneHotEncode to categorical columns
ohe = OneHotEncoder(categories='auto')
cat_data_transformed_ohe = pd.DataFrame(ohe.fit_transform(categorical_subset).toarray())

# Put data back together
data_transformed_ohe = pd.concat([numeric_subset, cat_data_transformed_ohe], axis = 1)

data_transformed_ohe.head()

# Splitting data set
data_ohe_train_X, data_ohe_test_X = train_test_split(data_transformed_ohe.drop(103, axis=1), random_state=1)
data_ohe_train_y, data_ohe_test_y = train_test_split(data_transformed_ohe[103], random_state=1)

# Fitting logistic regression
lr = LogisticRegression()
lr.fit(data_ohe_train_X, data_ohe_train_y)

# fitting random forest model using the encoded features
rf = RandomForestClassifier(n_estimators=10, oob_score=True)
rf.fit(data_ohe_train_X, data_ohe_train_y)

print("Performance summary for Logistic Regression with OneHotEncoder.\n")
modelStatsReport(lr,data_ohe_test_X,data_ohe_test_y)

print("Performance summary for Random Forest with OneHotEncoder.\n")
modelStatsReport(rf,data_ohe_test_X,data_ohe_test_y)

# Train a logistic regression model with a robust scalar on iris dataset.
iris_data = datasets.load_iris()
iris_df = pd.DataFrame(np.c_[iris_data.data, iris_data.target], columns=iris_data.feature_names + ['target'])

# Describe data
describeData(iris_df)

# Splitting data set
data_train_X, data_test_X = train_test_split(iris_df.drop('target', axis=1), random_state=1)
data_train_y, data_test_y = train_test_split(iris_df['target'], random_state=1)

# Preprocess the data using Robust Scaler technique
rs = RobustScaler()
rs.fit_transform(data_train_X)

rslr = LogisticRegression()
rslr.fit(rs.fit_transform(data_train_X),data_train_y)

print("Performance summary for Logistic Regression with Robust Scaler.\n")
modelStatsReport(rslr,rs.transform(data_test_X),data_test_y)

#Train a logistic regression model with a polynomilal transform and a robust scalar
pipeline = Pipeline(steps=[('rs', RobustScaler()),
                          ('poly', PolynomialFeatures(degree=2)),
                          ('logistic', LogisticRegression())])
pipeline.fit(data_train_X, data_train_y)

print("Performance summary for Logistic Regression with Polynomilal Features and Robust Scaler.\n")
modelStatsReport(pipeline,data_test_X,data_test_y)

"""*Problem 2* - Performance and Optimization Homework

- Try to use sklearn's precision_recall_curve function
- Train a Random Forest, how does this effect each metric?

Setup a pipeline for the Faces data set, try to optimize the parameters using GridSearch.
"""

data = pd.read_csv(io.StringIO(uploaded['adult.csv'].decode('utf-8')))
data_transformed = pd.get_dummies(data, columns=['workclass', 'education', 'educational-num', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country'])

# Splitting data set
data_train_X, data_test_X = train_test_split(data_transformed.drop('income', axis=1), random_state=1)
data_train_y, data_test_y = train_test_split(data_transformed['income'], random_state=1)

lr = LogisticRegression()
lr.fit(data_train_X,data_train_y)

print("Performance summary for Logistic Regression.\n")
modelStatsReport(lr,data_test_X,data_test_y)

scores = lr.predict_proba(data_test_X)[:,0]
fpr, tpr, thresholds = roc_curve(data_test_y, scores, pos_label='<=50K')

plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve ')
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

print("Area under the curve (AUC): ", auc(fpr, tpr))

# Calculate precision recall curve
y_score = lr.decision_function(data_test_X)

# Calculate average precision
average_precision = average_precision_score(data_test_y, y_score, pos_label='<=50K')
print('Average precision-recall score: {0:0.2f}'.format(average_precision))

precision, recall, _ = precision_recall_curve(data_test_y, y_score, pos_label='<=50K')

# In matplotlib < 1.5, plt.fill_between does not have a 'step' argument
step_kwargs = ({'step': 'post'}
               if 'step' in signature(plt.fill_between).parameters
               else {})
plt.step(recall, precision, color='b', alpha=0.2, where='post')
plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(average_precision))

# Train Random Forest
# fitting random forest model using the encoded features
rf = RandomForestClassifier(n_estimators=50)
rf.fit(data_train_X, data_train_y)

print("Performance summary for Random Forest.\n")
modelStatsReport(rf,data_test_X,data_test_y)

scores = rf.predict_proba(data_test_X)[:,0]
fpr_rf, tpr_rf, thresholds_rf = roc_curve(data_test_y, scores, pos_label='<=50K')

plt.figure()
lw = 2
plt.plot(fpr_rf, tpr_rf, color='darkorange',
         lw=lw, label='ROC curve ')
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

print("Area under the curve (AUC): ", auc(fpr_rf, tpr_rf))

# Calculate precision recall curve
y_score = rf.oob_decision_function(data_test_X)

# Calculate average precision
average_precision = average_precision_score(data_test_y, y_score, pos_label='<=50K')
print('Average precision-recall score: {0:0.2f}'.format(average_precision))

precision_rf, recall_rf, _ = precision_recall_curve(data_test_y, y_score, pos_label='<=50K')

# In matplotlib < 1.5, plt.fill_between does not have a 'step' argument
step_kwargs = ({'step': 'post'}
               if 'step' in signature(plt.fill_between).parameters
               else {})
plt.step(recall_rf, precision_rf, color='b', alpha=0.2, where='post')
plt.fill_between(recall_rf, precision_rf, alpha=0.2, color='b', **step_kwargs)

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(average_precision))

#Setup a pipeline for the Faces data set, try to optimize the parameters using GridSearch.

# Load faces dataset
#lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
lfw_people = fetch_lfw_people(min_faces_per_person=30)

for name in lfw_people.target_names:
  print(name)

"""I didn't know how to do this problem, so on my search I found the script below on https://scikit-learn.org/stable/tutorial/statistical_inference/putting_together.html. Because of lack of time I will not be able to tinker with the script before this homework submission deadline."""

print(__doc__)

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape

# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)


# #############################################################################
# Split into a training set and a test set using a stratified k fold
# split into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# #############################################################################
# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
# dataset): unsupervised feature extraction / dimensionality reduction
n_components = 150

print("Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0]))
t0 = time()
pca = PCA(n_components=n_components, svd_solver='randomized',whiten=True).fit(X_train)
print("done in %0.3fs" % (time() - t0))

eigenfaces = pca.components_.reshape((n_components, h, w))

print("Projecting the input data on the eigenfaces orthonormal basis")
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" % (time() - t0))


# #############################################################################
# Train a SVM classification model

print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'),param_grid, cv=5)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)


# #############################################################################
# Quantitative evaluation of the model quality on the test set

print("Predicting people's names on the test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))

print(classification_report(y_test, y_pred, target_names=target_names))
print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))


# #############################################################################
# Qualitative evaluation of the predictions using matplotlib

def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


# plot the result of the prediction on a portion of the test set

def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
    return 'predicted: %s\ntrue:      %s' % (pred_name, true_name)

prediction_titles = [title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])]

plot_gallery(X_test, prediction_titles, h, w)

# plot the gallery of the most significative eigenfaces

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()