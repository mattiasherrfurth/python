# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:16:04 2019

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

## QN CONNECTION ##

# STEP 1 - READ PREVIOUS REPORT ###

# wrap step 1 in a while loop (easy to break out of upon error)
chk = True
while chk == True:
    # setting filepaths for reports
    new_data_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\write\CURRENT'
    old_data_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\write\OLD'
    new_status_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\status\CURRENT'
    old_status_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\status\OLD'
    
    # checking that CURRENT folders exist and throwing error if they don't
    # also creating error report if the CURRENT folders don't exist
    # checking that OLD folders exist and making them if they don't
    if os.path.exists(new_data_path) == False:
        print('ERROR: Previous data report not found')
        break
    if os.path.exists(old_data_path) == False:
        os.mkdir(old_data_path)
    if os.path.exists(new_status_path) == False:
        print('ERROR: Previous status report not found')
        break
    if os.path.exists(old_status_path) == False:
        os.mkdir(old_status_path)
        
    # checking that CURRENT folders have only one status report
    curr_data_cnt = len([name for name in os.listdir(new_data_path)])
    curr_stat_cnt = len([name for name in os.listdir(new_status_path)])
    if curr_data_cnt != 1:
        print('data file count error')
        break
    if curr_stat_cnt != 1:
        print('stat file count error')
        break
    
    # making filepath string for previous status report
    filename_stat = os.listdir(new_status_path)[0]
    old_stat_file = new_status_path + '\\' + filename_stat
    
    # making filepath string for previous data report
    filename_data = os.listdir(new_data_path)[0]
    old_data_file = new_data_path + '\\' + filename_data
    
    # reading in previous status report
    with open(old_stat_file) as old_stat:
        for line in old_stat:
            if line.split(':')[0] == 'REPORT NAME':
                name = line.split(':')[1]
            if line.split(':')[0] == 'TIMESTAMP':
                time = line.split(':')[1]
            if line.split(':')[0] == 'RUN DURATION':
                run_time = line.split(':')[1]
            if line.split(':')[0] == 'NEW_DATA_SHAPE':
                old_shape = line.split(':')[1]
        old_stat.close()            
    
    # reading in previous data report
    old_df = pd.read_excel(old_data_file)
    
    # moving old status report to OLD folder
    old_path = old_status_path + '\\' + filename_stat
    os.rename(old_stat_file, old_path)
    # moving old status report to OLD folder
    old_data = old_data_path + '\\' + filename_data
    os.rename(old_data_file, old_data)
    chk = False