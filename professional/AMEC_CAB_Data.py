# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:01:52 2018

@author: Mattias Herrfurth
"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from matplotlib import rc

df = pd.read_excel(os.getcwd()+'\\AMEC CAB QN Data.xlsx')
plt.style.use('seaborn-white')
#plt.subplots(1,3,sharey='row')

def QN_RWK_Analysis(df):
    amec_desc = ["AMEC Active Feed","AMEC IMA's and others","AMEC Modules"]
    disp = ['MRBE','RWK','SCRP','SRP','UDEF']
    d = dt.datetime.now().month
    month = [d-2,d-1,d]
    dfrwk = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['Month'].isin(month))]
    counts = []
    for x in month:
        mods = dfrwk[(dfrwk['Scheduler Description'] == "AMEC Modules") & (dfrwk['Month'] == x)].shape[0]
        afs = dfrwk[(dfrwk['Scheduler Description'] == "AMEC Active Feed") & (dfrwk['Month'] == x)].shape[0]
        imas = dfrwk[(dfrwk['Scheduler Description'] == "AMEC IMA's and others") & (dfrwk['Month'] == x)].shape[0]
        counts.append([mods,afs,imas])
    cnt = pd.DataFrame(counts,columns=month).transpose()
    return cnt

def Top5Drivers(df):
    amec_desc = ['AMEC Modules',]
    disp = ['MRBE','RWK','SCRP','SRP','UDEF']
    m = dt.datetime.now().month
    counts = []
    month = [m-2,m-1,m]
    dftop5 = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['Month'].isin(month))]
    for y in dftop5['Part Number'].unique():
        m1 = dftop5[(dftop5['Part Number']==y) & (dftop5['Month']==(m-2))].shape[0]
        m2 = dftop5[(dftop5['Part Number']==y) & (dftop5['Month']==(m-1))].shape[0]
        m3 = dftop5[(dftop5['Part Number']==y) & (dftop5['Month']==(m))].shape[0]
        total = m1+m2+m3
        counts.append([y,m1,m2,m3,total])
    return(pd.DataFrame(counts,columns=['Part Number',month[0],month[1],month[2],'Total']).sort_values(by=['Total'],ascending=False).head(5))
    
    
def Top5Modules(df):
    amec_desc = ["AMEC Modules","AMEC IMA's and others"]
    disp = ['MRBE','RWK','SCRP','SRP','UDEF']
    now = dt.datetime.now()
    endweek1 = (now.date() - dt.timedelta(days=now.weekday()) + dt.timedelta(days=4, weeks=-1))
    endweek3 = endweek1 - dt.timedelta(days = 14)
    d = endweek3
    days = []
    while d < endweek1:
        d = d + dt.timedelta(days=1)
        days.append(pd.to_datetime(d.strftime('%Y%m%d'), format='%Y%m%d'))
    counts = []
    dfmods = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['QN Item Number'] == 1) & (df['Week Ending'].isin(days))]
    for y in dfmods['Part Number'].unique():
        insp = dfmods[(dfmods['Work Center Category']=='Inspection Labor') & (dfmods['Part Number']==y)].shape[0]
        mfg = dfmods[(dfmods['Work Center Category']=='Mfg Labor') & (dfmods['Part Number']==y)].shape[0]
        test = dfmods[(dfmods['Work Center Category']=='Test Labor') & (dfmods['Part Number']==y)].shape[0]
        qual = dfmods[(dfmods['Work Center Category']=='QE Labor') & (dfmods['Part Number']==y)].shape[0]
        total = insp+mfg+test+qual
        counts.append([y,insp,mfg,test,qual,total])
    return(pd.DataFrame(counts,columns=['Part Number','Inspection Labor','Mfg Labor','Test Labor','QE Labor','Total']).sort_values(by=['Total'],ascending=False).head(5))
    
## this function should be altered to report the past 4 weeks, not a single month
def SABR10(df):
    amec_desc = ["AMEC Modules"]
    disp = ['MRBE','RWK','SCRP','SRP','UDEF']
    sabrpn = ['partnumber1','partnumber2']
    m = dt.datetime.now().month - 1
    counts = []
    sabr = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['QN Item Number'] == 1) & (df['Month']==m) & (df['Part Number'].isin(sabrpn))]
    for y in sabr['Defect Code'].unique():
        cnt = sabr[sabr['Defect Code']==y].shape[0]
        counts.append([y,cnt])
    return(pd.DataFrame(counts,columns=['Defect Code','QN Count']).sort_values(by=['QN Count'],ascending=False).head(10))
    
## this function should be altered to report the past 4 weeks, not a single month
def jsf10_mfg(df):
    amec_desc = ["AMEC Modules"]
    disp = ['MRBE','RWK','SCRP','SRP','UDEF']
    jsfpn = ['partnumber3','partnumber4','partnumber5']
    m = dt.datetime.now().month - 1
    counts = []
    jsf = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['QN Item Number'] == 1) & (df['Month']==m) & (df['Part Number'].isin(jsfpn)) & (df['Work Center Category']=='Mfg Labor')]
    for y in jsf['Defect Code'].unique():
        cnt = jsf[jsf['Defect Code']==y].shape[0]
        counts.append([y,cnt])
    return(pd.DataFrame(counts,columns=['Defect Code','QN Count']).sort_values(by=['QN Count'],ascending=False).head(10))

def jsf10_test(df):
    amec_desc = ["AMEC Modules"]
    disp = ['MRBE','RWK','SCRP','SRP','UDEF']
    jsfpn = ['partnumber3','partnumber4','partnumber5']
    m = dt.datetime.now().month - 1
    counts = []
    jsf = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['QN Item Number'] == 1) & (df['Month']==m) & (df['Part Number'].isin(jsfpn)) & (df['Work Center Category']=='Test Labor')]
    for y in jsf['Defect Code'].unique():
        cnt = jsf[jsf['Defect Code']==y].shape[0]
        counts.append([y,cnt])
    return(pd.DataFrame(counts,columns=['Defect Code','QN Count']).sort_values(by=['QN Count'],ascending=False).head(10))
 
def jsf10_insp(df):
    amec_desc = ["AMEC Modules"]
    disp = ['MRBE','RWK','SCRP','SRP','UDEF']
    jsfpn = ['partnumber3','partnumber4','partnumber5']
    m = dt.datetime.now().month - 1
    counts = []
    jsf = df[(df['Scheduler Description'].isin(amec_desc)) & (df['Disposition'].isin(disp)) & (df['QN Item Number'] == 1) & (df['Month']==m) & (df['Part Number'].isin(jsfpn)) & (df['Work Center Category']=='Inspection Labor')]
    for y in jsf['Defect Code'].unique():
        cnt = jsf[jsf['Defect Code']==y].shape[0]
        counts.append([y,cnt])
    return(pd.DataFrame(counts,columns=['Defect Code','QN Count']).sort_values(by=['QN Count'],ascending=False).head(10))
    

#jsf10insp = jsf10_insp(df)
#jsf10test = jsf10_test(df)
#jsf10mfg = jsf10_mfg(df)
#mod5 = Top5Modules(df)
#df5 = Top5Drivers(df)
#dfrwk = QN_RWK_Analysis(df)



    