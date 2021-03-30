# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:06:12 2019

@author: J20032
"""

import pandas as pd
import math
from datetime import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

df = pd.read_excel(r'C:\Users\J20032\Documents\ME_FTTIY_20190306.xlsx')

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

#def make_pchart(df):
#    # can make a column into a numeric... not sure how it is counting though
#    dfp['Date_num'] = pd.to_numeric(dfp['Date'])
#    yld = sns.lineplot(x = 'Yield',y = 'Date_num',data = dfp)
#    cl = sns.lineplot(x = 'Center Line',y = 'Date_num',data = dfp)
#    ucl = sns.lineplot(x = 'UCL',y = 'Date_num',data = dfp)
#    lcl = sns.lineplot(x = 'LCL',y = 'Date_num',data = dfp)
#    for line in range(0,dfp.shape[0]):
#        yld.text(dfp['Date_num'][line], dfp['Yield'][line], dfp['OOC'][line], 
#                 horizontalalignment='center',verticalalignment='center', size='large', 
#                 color='red', weight='semibold')
#    plt.xticks(rotation=90)
#    plt.ylim(min([dfp['LCL'].min(),dfp['Yield'].min(),0.5]),1.0)
#    plt.ylabel('Yield')
#    plt.title('P-chart')
#    plt.show()

df = get_ptable(df)

#def make_pchart(df):
# can make a column into a numeric... not sure how it is counting though

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