# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:06:12 2019

@author: Mattias
"""

import pandas as pd
import math
from datetime import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

df = pd.read_excel(r'C:\path\to\excel\file.xlsx')

# making a function for getting a ptable for SAMPLE INSPECTION
# need to also make a function for FULL INSPECTION (i.e. moving center line)

def get_ptable(df):    
    ptable = []
    cols = ['Date','Qty Inspected','Qty Accepted','Yield','Center Line','UCL','LCL','OOC']
    for d in df.ILOR_END_DT.unique():
        cnt_insp = df[(df['ILOR_END_DT']==d)].shape[0]
        cnt_acpt = df[(df['ILOR_END_DT']==d) & (df['ILOR_EVALUATION_CD']=='ACCEPTED')].shape[0]
        yld = cnt_acpt / cnt_insp
        cl = 0.98
        ucl = min([cl+3*math.sqrt((cl*(1-cl))/cnt_insp),1.0])
        lcl = max([cl-3*math.sqrt((cl*(1-cl))/cnt_insp),0.0])
        if yld < lcl or yld > ucl:
            grp = 'o'
        else:
            grp = ''
        ptable = ptable + [[d,cnt_insp,cnt_acpt,yld,cl,ucl,lcl,grp]]
    # ADD HANDLING FOR OTHER OOC POINT CRITERIA (n points decreasing, oscillating, etc.)
    #    if yld < progyld[n]:
    #        grp = 'o'
    #    else:
    #        grp = ''
    return(pd.DataFrame(data=ptable,columns=cols))

df = get_ptable(df)

### need to make tidy data
dfp = pd.melt(df, id_vars=['Date'], value_vars=['Yield', 'CenterLine','UCL','LCL'],
              var_name='Legend', value_name='Yield')
dfp['Date_num'] = pd.to_numeric(dfp['Date'])
dfp = dfp.set_index('Date')
plt.xticks(rotation=90)
#plt.xticks(dfp['Date'])
plt.ylim(min([dfp[dfp['Legend']=='LCL'].min()[2],dfp[dfp['Legend']=='Yield'].min()[2],0.6]),1.0)
plt.ylabel('Yield')
plt.title('P-chart')
#sns.lineplot(x='index',y='Yield',hue='Legend',data=dfp)
#sns.regplot(data=dfp.reset_index(),x='index',y='Yield')
plt.show()
