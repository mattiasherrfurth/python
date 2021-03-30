# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import seaborn as sns
import pandas as pd
import numpy as np
import os


#def shuffle(df, n=1, axis=0):
#    df = df.copy()
#    for x in range(n):
#        df.apply(np.random.shuffle,axis=axis)
#    return df

def make_fttiy():
    serial = []
    first = 50784500
    x = 0
    while x < 2000:
        serial.append(first)
        first+=1
        x+=1
    np.random.shuffle(serial)
    serial = pd.Series(serial)
    
    deez = pd.date_range(start='2018-03-01', end='2018-08-31',periods=2000)
    dates=[]
    for x in deez:
        dates.append(str(x).split(' ')[0])
    
    nums = np.random.randint(0,2000,size=(2000,))
    
    evals=[]
    for x in np.random.randint(0,2000,size=(2000,)):
        if x%6 == 0:
            evals.append(False)
        else:
            evals.append(True)
    
    df = pd.DataFrame({'dates':dates,'num':nums,'eval':evals,'sn':serial})
    return df

os.chdir(os.getcwd()+'\\fttiy_out')

df1 = make_fttiy()
df2 = make_fttiy()

writer = pd.ExcelWriter('out_test_%s.xlsx'%datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
df1.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2')
writer.save()

sns.lineplot(x=df1.dates,y=df1.num)