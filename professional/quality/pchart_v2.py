# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:10:04 2019

@author: Mattias
"""
# immport important imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
from datetime import timedelta as td
#from sklearn.feature_extraction.text import CountVectorizer as cv

# create dataframe from pyramid FTTIY raw data
df = pd.read_excel(r'C:\path\to\excel\file.xlsx')

def get_20day_avg(df):
    dates = list(df['Date'].unique())[-20:]
    tot_insp = df[(df['Part']==pn)&(df['Date'].isin(dates))&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)].shape[0]
    tot_accept = df[(df['Part']==pn)&(df['Date'].isin(dates))&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)&(df['Result']=='ACCEPTED')].shape[0]
    return(tot_accept / tot_insp)

def get_yields(pn,df):
    # NOTE: add handling for sample inspected parts (i.e. columns will have sample inspected values)
    # brute force handling for sampled parts
    samps = ['261K775G03','261K775G04','255K250G07']
    date_end = df.Date.max()
    dates = []
    while d < date_end:
        dates = dates + [d]
        d = d + td(days=1)
    if pn in samps:
        CL = 0.98
    elif df['Date'].unique()[0] > 20:
        CL = get_20day_avg(df)
    else:
        tot_insp = df[(df['Part']==pn)&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)].shape[0]
        tot_accept = df[(df['Part']==pn)&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)&(df['Result']=='ACCEPTED')].shape[0]
        CL = tot_accept / tot_insp
    cols = ['Date','QtyInspected','QtyAccepted','Yield','Centerline','UCL','LCL']
    fttiy = []
    for n in dates:
        fttiy_cnt = df[(df['Part']==pn)&(df['Date']==n)&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)].shape[0]
        if n in set(df['Date']) and fttiy_cnt > 2:
            insp_cnt = df[(df['Part']==pn)&(df['Date']==n)&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)].shape[0]
            accept_cnt = df[(df['Part']==pn)&(df['Date']==n)&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)&(df['Result']=='ACCEPTED')].shape[0]
            cnts_yld = (accept_cnt / insp_cnt)
            sig = sqrt((CL*(1-CL))/insp_cnt)
            UCL = min([(CL + (3*sig)),1.0])
            LCL = (CL - (3*sig))
            fttiy = fttiy + [[n,insp_cnt,accept_cnt,cnts_yld,CL,UCL,LCL]]
    dfttiy = pd.DataFrame(data=fttiy,columns=cols)
    return(dfttiy)
        
        
pn = input('Please enter a part number: ')
df = df[df['Part']==str(pn)]
plot = get_yields(pn,df)
sns.lineplot(x='Date',y='Yield',data=plot)
sns.lineplot(x='Date',y='UCL',data=plot,dashes=True)
sns.lineplot(x='Date',y='LCL',data=plot,dashes=True)
