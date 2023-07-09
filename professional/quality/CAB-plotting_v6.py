# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:46:31 2019

@author: Mattias
"""

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import datetime as dt

import pyodbc 
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server.hostname.domain.com;'
                      'Database=db_name;'
                      'Trusted_Connection=yes;')
sql = "SELECT * FROM [db_name].[dbo].[YieldQNs] WHERE [QNOT_CREATED_DT] >= DATEADD(Month, -3, getdate()) AND [QNOT_PLNT_ID] = 'P001'"
df = pd.read_sql(sql,cnxn)

cnts = []

for x in df['QNOT_PART_NO'].unique():
    cnt = df[df['QNOT_PART_NO'] == x].shape[0]
    cnts = cnts + [{'PN':x, 'cnt':cnt}]

# cnts = sorted(cnts, key = lambda i: i['cnt'], reverse = True)
top10 = sorted(cnts, key = lambda i: i['cnt'], reverse = True)[0:10]

df['pyDate'] = df['QNOT_CREATED_DT'].apply(lambda row: pd.to_datetime(str(row)).strftime('%Y-%m-%d'))

plt.figure(figsize=(12,8))
# plot barh chart with index as x values
ax = sns.barplot(top10['QNOT_PART_NO'], top10['Count'],palette='Oranges_r')
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax.set(xlabel="QNOT_PART_NO", ylabel='Count')
ax.set_title('Top 10 QN Counts for Part Numbers - Past Two Weeks')
ax.set_xticklabels(top10["Part Number"])
for item in ax.get_xticklabels(): item.set_rotation(70)
for i, v in enumerate(top10["Count"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='m', va ='bottom', rotation=45)
