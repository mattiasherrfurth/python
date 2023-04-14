# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:02:44 2019

@author: J20032
"""

import pandas as pd

df_mask = pd.read_excel(r'T:\A\AMEC\Quality Engineering\Process Improvement Projects\Die Passivation\Mask_Log.xlsx')

df_mask = df_mask.sort_values('NG Mask Number')

#trim_parts = [x[2:] for x in df_mask['NG Mask Number']]
# this won't work because some of the entries do not have "NG" at the beginning of the part number

trim_parts = []

for x in df_mask['NG Mask Number']:
    while x[0].isnumeric() == False:
        x = x[1:]
    trim_parts = trim_parts + [x]
        
df_mask['Trimmed Part Number'] = trim_parts
