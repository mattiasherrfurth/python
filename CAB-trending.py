# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:46:31 2019

@author: J20032
"""

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import datetime as dt
#from sklearn.preprocessing import 

# reading in dataframe
datas = pd.read_excel(r'C:\Users\J20032\Documents\AMEC_CAB_RAW_20190408.xlsx')

# creating integer index of QN Item Created Date column
julian = [x.to_julian_date() for x in datas['QN Item Created Date']]
datas['julian-date'] = julian

### GETTING QN COUNTS FOR PAST TWO WEEKS

# create a column for the day of the week
datas['day_of_week'] = datas['QN Item Created Date'].dt.day_name()
# filter out everything but Frodays
fridays = datas[datas['day_of_week']=='Friday']
fridays = fridays.set_index('QN Item Created Date')
days = sorted(fridays.index.unique(),reverse=True)

# get 2 week pay period beginning and ending julian time
wknd1 = round(days[2].to_julian_date())
wknd2 = round(days[0].to_julian_date())

# filter between begin and end dates
data = datas[(datas['julian-date']>wknd1) & (datas['julian-date']<wknd2)]

# pull unique part numbers
parts = data['Part Number'].unique()

# create and populate array of part number and counts of QNs
cnts = []
for p in parts:
    cnts = cnts + [[p,data[data['Part Number']==p].shape[0]]]

# creating and sorting dataframe for seaborn plotting
df = pd.DataFrame(data=cnts,columns=['Part Number','Count'])
df_sort = df.sort_values(by='Count',ascending=False)

# trimming to top10
top10 = df_sort.head(10)

plt.figure(figsize=(12,8))
# plot barh chart with index as x values
ax = sns.barplot(top10['Part Number'], top10['Count'],palette='Oranges_r')
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax.set(xlabel="Part Number", ylabel='Count')
ax.set_title('Top 10 QN Counts for Part Numbers - Past Two Weeks')
ax.set_xticklabels(top10["Part Number"])
for item in ax.get_xticklabels(): item.set_rotation(70)
for i, v in enumerate(top10["Count"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='m', va ='bottom', rotation=45)
    
### GETTING TRENDS FOR QN COUNTS OVER TWO MONTHS
pn10 = top10['Part Number']

df10 = datas[datas['Part Number'].isin(pn10)]

#trends = []
#for j in df10['julian-date'].unique():
#    date = pd.to_datetime(j)
#    nums = []
#    for r in pn10:
#        nums = 
#    trends = trends + [[date,df10[(df10['julian-date']==j) & (df10['Part Number'])].shape[0]]]

    
    
    
    
    
    
    
    
    