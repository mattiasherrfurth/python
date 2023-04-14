#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:23:32 2021

@author: mattias
"""

import pandas as pd 
import statsmodels.api as sm
from statsmodels.formula.api import ols
pd.set_option('display.max_columns', None)

data = pd.read_excel(r"/home/mattias/Documents/class/hw8/hw8_q1.xlsx",engine='openpyxl')
model2 = ols("discharge_time_mins ~ C(battery_type,Sum) + C(connector_type,Sum) + C(battery_temp,Sum) + C(battery_type,Sum):C(connector_type,Sum) + C(battery_type,Sum):C(battery_temp,Sum) + C(connector_type,Sum):C(battery_temp,Sum)", data=data).fit()

aov_table = sm.stats.anova_lm(model2, typ=3)
print(aov_table)