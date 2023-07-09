# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:29:51 2019

@author: J20032
"""

## FTTIY CONNECTION ##

import pandas as pd
import pyodbc 
from datetime import datetime as dt
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EIM-DB-AG40.NORTHGRUM.COM;'
                      'Database=j20032_yield;'
                      'Trusted_Connection=yes;')
sql = """
SELECT * 
    FROM [j20032_yield].[dbo].[YieldPlusQNs] 
        WHERE [DATE] >= DATEADD(Month, -3, getdate()) 
            AND [OROP_PLNT_ID] = 'P001'
            AND [PCLL_SHORT_NM] = 'AMEC'
            AND [YIELDCATEGORY] = 'INSPECTION'
            """
now = dt.now().strftime('%Y%m%d')

df = pd.read_sql(sql,cnxn)

# getting rid of any trailing whitespace
for col in df.columns:
    try:
        df[col] = df[col].apply(lambda row: row.strip())
    except:
        pass
    
df.to_excel(r'T:\A\AMEC\Quality Engineering\P-charts\SQL_SERVER_QUERY\DATA\j20032_'+now+'_yieldplusQNs.xlsx')