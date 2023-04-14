# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:10:04 2019

@author: J20032
"""
# immport important imports
import pandas as pd
import seaborn as sns
#from sklearn.feature_extraction.text import CountVectorizer as cv

# create dataframe from pyramid FTTIY raw data
df = pd.read_excel(r'C:\Users\J20032\Documents\FTTIY_20190221.xlsx')

# pick out columns which look like targets
#for x in df.columns:
#    if df[x].unique().shape[0] == 2:
#        print('The column %s has only two attributes.'%x)
#        print('These unique attributes are:',df[x].unique(),'\n')
        
# out of all of the results, only column "Result" had two unique values that appeared tobe results

# lets do things with Result being our target

trgt = 'Result'

# pick out which columns are numeric
#for x in df.columns:
##    print(x,' is of data type: ',df[x].dtype)
#    if df[x].dtype == object:
#        df[x] = cv(df[x])

