# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 23:07:16 2018

@author: J20032
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:01:52 2018

@author: J20032
"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from matplotlib import rc

df = pd.read_excel(os.getcwd()+'\\AMEC CAB QN Data.xlsx')

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






    