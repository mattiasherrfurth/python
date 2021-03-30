# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:24:50 2019

@author: J20032
"""

import pandas as pd

data = pd.read_csv(r'C:\Users\J20032\Documents\FTTIY PYTHON\YLD_Table_View_data.csv')

df = data[data['WCTR_CD'].str.contains('MY')]