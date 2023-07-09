# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:29:51 2019

@author: Mattias
"""

## FTTIY CONNECTION ##

import pandas as pd
import pyodbc 
from datetime import datetime as dt
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server.hostname.domain.com;'
                      'Database=db_name;'
                      'Trusted_Connection=yes;')
sql = """
SELECT * 
    FROM [db_name].[dbo].[YieldPlusQNs] 
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
    
df.to_excel(r'C:\path\to\excel\file_'+now+'_yield.xlsx')
