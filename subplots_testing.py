# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 10:28:56 2018

@author: J20032
"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#import datetime as dt
#from matplotlib import rc

x = np.linspace(0, 2 * np.pi, 400)
df = pd.DataFrame({'x': x, 'y': np.sin(x ** 2)})
df.index.names = ['obs']
df.columns.names = ['vars']

idx = np.array(df.index.tolist(), dtype='float')  # make an array of x-values

# call regplot on each axes
fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
sns.regplot(x=idx, y=df['x'], ax=ax1)
sns.regplot(x=idx, y=df['y'], ax=ax2)
