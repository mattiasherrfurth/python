# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:46:31 2019

@author: J20032
"""

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import datetime as dt

import pyodbc 
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EIM-DB-AG40.NORTHGRUM.COM;'
                      'Database=j20032_yield;'
                      'Trusted_Connection=yes;')
sql = "SELECT * FROM [j20032_yield].[dbo].[YieldQNs] WHERE [QNOT_CREATED_DT] >= DATEADD(Month, -3, getdate()) AND [QNOT_PLNT_ID] = 'P001'"
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


### creating integer index of QN Item Created Date column
##julian = [x.to_julian_date() for x in datas['QN Item Created Date']]
##datas['julian-date'] = julian
##
##### GETTING QN COUNTS FOR PAST TWO WEEKS
##datas['day_of_week'] = datas['QN Item Created Date'].dt.day_name()
##fridays = datas[datas['day_of_week']=='Friday']
##fridays = fridays.set_index('QN Item Created Date')
##days = sorted(fridays.index.unique(),reverse=True)
##
##wknd1 = round(days[2].to_julian_date())
##wknd2 = round(days[0].to_julian_date())
##
##data = datas[(datas['julian-date']>wknd1) & (datas['julian-date']<wknd2)]
##
##parts = data['Part Number'].unique()
#
##cnts = []
##for p in parts:
##    cnts = cnts + [[p,data[data['Part Number']==p].shape[0]]]
##
##df = pd.DataFrame(data=cnts,columns=['Part Number','Count'])
##df_sort = df.sort_values(by='Count',ascending=False)
#
#top10 = df_sort.head(10)
#
#plt.figure(figsize=(12,8))
## plot barh chart with index as x values
#ax = sns.barplot(top10['Part Number'], top10['Count'],palette='Oranges_r')
#ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
#ax.set(xlabel="Part Number", ylabel='Count')
#ax.set_title('Top 10 QN Counts for Part Numbers - Past Two Weeks')
#ax.set_xticklabels(top10["Part Number"])
#for item in ax.get_xticklabels(): item.set_rotation(70)
#for i, v in enumerate(top10["Count"].iteritems()):        
#    ax.text(i ,v[1], "{:,}".format(v[1]), color='m', va ='bottom', rotation=45)