# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 00:02:39 2019

@author: J20032
"""

import pandas as pd
import seaborn as sns
from datetime import timedelta as td
from math import sqrt

def get_20day_avg(df):
    dates = list(df['Date'].unique())[-20:]
    tot_insp = df[(df['Part']==pn)&(df['Date'].isin(dates))&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)].shape[0]
    tot_accept = df[(df['Part']==pn)&(df['Date'].isin(dates))&(df['WCTR_CD']!='MYVARWK')&(df['Oper']==4500)&(df['Result']=='ACCEPTED')].shape[0]
    return(tot_accept / tot_insp)

df = pd.read_excel(r'C:\Users\J20032\Documents\FTTIY_20190221.xlsx')
pn = '261K775G04'

# brute force handling for sampled parts
samps = ['261K775G03','261K775G04','255K250G07']

df = df[df['Part']==str(pn)]
#def get_yields(pn,df):
# NOTE: add handling for sample inspected parts (i.e. columns will have sample inspected values)
date_init = d = df.Date.min()
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
fttiy = [['Date','QtyInspected','QtyAccepted','Yield','Centerline','UCL','LCL']]
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
dfttiy = pd.DataFrame(data=fttiy)