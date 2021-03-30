# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:35:27 2018

@author: matti
"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

os.chdir(os.getcwd()+'\\fttiy_out')

#print(os.getcwd())

df1 = pd.read_excel(os.getcwd()+'\\out_test_20181028203143.xlsx',sheet_name='Sheet1')
df2 = pd.read_excel(os.getcwd()+'\\out_test_20181028203143.xlsx',sheet_name='Sheet2')

#print(df1.columns, df2.columns)

fix, axs = plt.subplots(ncols=2)
#sns.lineplot(x=df1.dates,y=df1.num, ax = axs[0])
#sns.lineplot(x=df2.dates,y=df2.num, ax = axs[1])

#date1 = input('When are we starting? (YYYY-MM-DD)')
#date2 = input('When are we ending? (YYYY-MM-DD)')
date1 = '2018-03-01'
date2 = '2018-03-01'


totyld = pd.Series()
## NEED TO INCLUDE ERROR HANDLING FOR INDEX OUT OF RANGE ##
try:
    d1 = datetime.datetime.strptime(date1,'%Y-%m-%d')
    d2 = datetime.datetime.strptime(date2,'%Y-%m-%d')
except Exception as e:
    print('Give me a real date next time...')
    raise

#while d1 != date2:
#    accept = df1[(df1.dates == d1) & (df1.eval == 'True')].shape[0]
#    inspect = df1[(df1.dates == d1)].shape[0]
#    if inspect == 0:
#        pass
#    else:
#        yld = accept/inspect
#    totyld.append
#    d1 += datetime.timedelta(days=1)