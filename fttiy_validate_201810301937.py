# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:37:02 2018

@author: J20032
"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

#df = pd.read_excel(r'C:\Users\J20032\FTTIY_INPUT.xlsx')
#print(os.getcwd())

jsf_pyt = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\OUT\jsf_eval_test_20181031193528.xlsx')
sabr_pyt = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\OUT\sabr_eval_test_20181031193530.xlsx')
gator_pyt = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\OUT\gator_eval_test_20181031193532.xlsx')
triton_pyt = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\OUT\triton_eval_test_20181031193533.xlsx')

jsf_pyr = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\FTTIY_10-30-2018.xlsx',sheet = 'JSF')
sabr_pyr = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\FTTIY_10-30-2018.xlsx', sheet = 'SABR')
gator_pyr = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\FTTIY_10-30-2018.xlsx', sheet = 'GATOR')
triton_pyr = pd.read_excel(r'C:\Users\J20032\FTTIY PYTHON\FTTIY_10-30-2018.xlsx', sheet = 'TRITON')

jsf_pyr = jsf_pyr[(jsf_pyr['Date'] > pd.Timestamp('2018-08-31 00:00:00'))]

t = []
for x in pd.to_datetime(jsf_pyt.Date):
    for y in jsf_pyr.Date:
        if y != x:
            t.append(x)
print(pd.Series(t).unique())


