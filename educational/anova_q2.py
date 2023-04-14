#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:29:46 2021

@author: mattias
"""

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"/home/mattias/Documents/class/hw8/hw8_q2a.xlsx",
                     engine='openpyxl')

stats.f_oneway(df['brand_a'],df['brand_b'],df['brand_c'])