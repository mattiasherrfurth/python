# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:54:13 2018

@author: matti
"""

import os
import glob
import csv
from xlsxwriter.workbook import Workbook

os.chdir(r'C:\Users\matti\Documents\Python Scripts\seaborn-data-master')
print(os.getcwd())
for csvfile in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()