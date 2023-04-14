#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:56:53 2021

@author: mattias
"""

import pandas as pd 
import matplotlib.pyplot as plt
from statsmodels.graphics.factorplots import interaction_plot
pd.set_option('display.max_columns', None)

data = pd.read_excel(r"/home/mattias/Documents/class/hw8/hw8_q1.xlsx",
                     engine='openpyxl')

fig, ax = plt.subplots(figsize=(6, 6))
fig = interaction_plot(x=data['connector_type'], 
                       trace=data['battery_temp'], 
                       response=data['discharge_time_mins'],
                       colors=['red','blue'], 
                       markers=['D','^'], 
                       ms=10)
plt.show()