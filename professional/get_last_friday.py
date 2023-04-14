# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 22:29:05 2018

@author: J20032
"""

import datetime

current_time = datetime.datetime.now()

# get friday, one week ago, at 16 o'clock
last_friday = (current_time.date()
    - datetime.timedelta(days=current_time.weekday())
    + datetime.timedelta(days=4, weeks=-1))
#last_friday_at_16 = datetime.datetime.combine(last_friday, datetime.time(16))

# if today is also friday, and after 16 o'clock, change to the current date
#one_week = datetime.timedelta(weeks=1)
#if current_time - last_friday_at_16 >= one_week:
#    last_friday_at_16 += one_week
