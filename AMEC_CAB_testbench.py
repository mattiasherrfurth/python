# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 00:33:39 2018

@author: J20032
"""

## INITIALIZATIONS ##

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from matplotlib import rc
from matplotlib.colors import ListedColormap

df = pd.read_excel(os.getcwd()+'\\AMEC CAB QN Data.xlsx')

## TESTING ##

amec_desc = ["AMEC Active Feed","AMEC IMA's and others","AMEC Modules"]
disp = ['MRBE','RWK','SCRP','SRP','UDEF']
m = dt.datetime.now().month
m = [m-2,m-1,m]
dfrwk = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['Month'].isin(m))]
counts = []
for y in amec_desc:
    m1 = dfrwk[(dfrwk['Scheduler Description']==y) & (dfrwk['Month']==(m[0]))].shape[0]
    m2 = dfrwk[(dfrwk['Scheduler Description']==y) & (dfrwk['Month']==(m[1]))].shape[0]
    m3 = dfrwk[(dfrwk['Scheduler Description']==y) & (dfrwk['Month']==(m[2]))].shape[0]
    total = m1+m2+m3
    counts.append([y,m1,m2,m3,total])
dfrwk = pd.DataFrame(counts,columns=["Scheduler Desc.",m[0],m[1],m[2],'Total']).sort_values(by=['Total'],ascending=False)

dfrwk_trim = dfrwk.drop(labels=['Total'], axis=1)
dfrwk = pd.melt(dfrwk_trim, ['Scheduler Desc.'], var_name='Month', value_name='Count').sort_values(by = ['Count'],ascending=False)
sns.barplot(x='Scheduler Desc.', y='Count', hue='Month',data=dfrwk)
plt.xticks(rotation=90)
plt.ylabel('QN Count')
plt.title('AMEC QNs Created')