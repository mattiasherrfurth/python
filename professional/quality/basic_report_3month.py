# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:13:11 2019

@author: Mattias
"""

# IMPORTS
import pandas as pd
from datetime import datetime as dt
import time
import pyodbc
import os
import sys
import shutil

# FILEPATH FOR REPORTS
datapath = r'T:\path\to\folder'

###############################################################################

## FTTIY CONNECTION - Past 3 Months for AMEC Inspection ##

# connecting to the database
cnxn_fttiy = pyodbc.connect('Driver={SQL Server};'
                      'Server=server.hostname.domain.com;'
                      'Database=db_name;'
                      'Trusted_Connection=yes;')

# defining the sql query string
# NOTE: string is surrounded by three double-quotes ("""<text>"""), must exclude """ from query
sql_fttiy = """
SELECT * 
    FROM [db_name].[dbo].[PyramidYieldData] 
        WHERE [DATE] >= DATEADD(Month, -3, getdate()) 
            AND [OROP_PLNT_ID] = 'P001'
            AND [PCLL_SHORT_NM] = 'AMEC'
            AND [YIELDCATEGORY] = 'INSPECTION'
            """
now_fttiy = dt.now().strftime('%Y%m%d%H%M')

df_fttiy = pd.read_sql(sql_fttiy,cnxn_fttiy)

# getting rid of any trailing whitespace
for col in df_fttiy.columns:
    try:
        df_fttiy[col] = df_fttiy[col].apply(lambda row: row.strip())
    except:
        pass

df_fttiy.to_excel(datapath+'\\sql_'+now_fttiy+'_3month-yield.xlsx')

###############################################################################

## QN CONNECTION - Past 3 Months for AMEC ##

# connecting to the database
cnxn_qns = pyodbc.connect('Driver={SQL Server};'
                      'Server=server.hostname.domain.com;'
                      'Database=db2_name;'
                      'Trusted_Connection=yes;')

# defining the sql query string
# NOTE: string is surrounded by three double-quotes, must exclude these from query
sql_qns = """
SELECT * 
    FROM [db2_name].[dbo].[QNs_YTD_table] 
        WHERE [QNDF_CREATED_DT] >= DATEADD(Month, -3, getdate()) 
            AND [ORDR_PLNT_ID] = 'P001'
            AND [PCLL_CELL_NM] = 'ADVANCED MICROELECTRONICS CENTER'
            """
now_qns = dt.now().strftime('%Y%m%d%H%M')

df_qns = pd.read_sql(sql_qns,cnxn_qns)

# getting rid of any trailing whitespace
for col in df_qns.columns:
    try:
        df_qns[col] = df_qns[col].apply(lambda row: row.strip())
    except:
        pass

df_qns.to_excel(datapath+'\\sql_'+now_qns+'_3month-QNs.xlsx')

###############################################################################

## SRR CONNECTION - Past 3 Months for AMEC ##

# connecting to the database

cnxn_srr = pyodbc.connect('Driver={SQL Server};'
                      'Server=server.hostname.domain.com;'
                      'Database=db3_name;'
                      'Trusted_Connection=yes;')

# defining the sql query string
# NOTE: string is surrounded by three double-quotes, must exclude these from query
sql_srr = """
SELECT * 
    FROM [db3_name].[dbo].[SRR_YTD_table_test] 
        WHERE [MONTH] >= DATEADD(Month, -3, getdate()) 
            AND [PLANT] = 'P001'
            AND [CHARGED_AREA] = 'AMEC'
            """
now_srr = dt.now().strftime('%Y%m%d%H%M')

df_srr = pd.read_sql(sql_srr,cnxn_srr)

# getting rid of any trailing whitespace
for col in df_srr.columns:
    try:
        df_srr[col] = df_srr[col].apply(lambda row: row.strip())
    except:
        pass

df_srr.to_excel(datapath+'\\sql_'+now_srr+'_3month-srr.xlsx')
