# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:35:38 2019

@author: J20032
"""

# IMPORTS
import pandas as pd
from datetime import datetime as dt
import time
import pyodbc
import os
import sys
import shutil





########### SCRIPT FOR RETURNING FILES TO THE CURRENT FOLDER





#
#new_data_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\write\CURRENT'
#old_data_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\write\OLD'
#new_status_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\status\CURRENT'
#old_status_path = r'T:\A\AMEC\Quality Engineering\AMEC PCAB Meetings\Data Reports\data_testing\status\OLD'
#
## making filepath string for previous status report
#filename_stat = os.listdir(new_status_path)[0]
#old_stat_file = new_status_path + '\\' + filename_stat
#
## making filepath string for previous data report
#filename_data = os.listdir(new_data_path)[0]
#old_data_file = new_data_path + '\\' + filename_data
#
## moving old status report to OLD folder
#old_path = old_status_path + '\\' + filename_stat
#os.rename(old_stat_file, old_path)
## moving old status report to OLD folder
#old_data = old_data_path + '\\' + filename_data
#os.rename(old_data_file, old_data)