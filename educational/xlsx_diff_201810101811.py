#Purpose: import two xlsx workbooks, compare the values in the tables
#Response: move two original files into another directyory.
#          create a third xlsx file that returns the value different for either
#          column, and statistical differences both on the metadata and data
#Author: Mattias Herrfurth

import os, pandas as pd, seaborn as sb

dir_path = os.getcwd()

def dir_check():
    if '\\' in os.getcwd():
        print('this is windows')
        if os.path.isdir(dir_path + '\\_INPUT_') == True:
            indir = dir_path + '\\_INPUT_'
        else:
            indir = os.mkdir(dir_path + '\\_INPUT_')
            print('let me make you an inbox')
        if os.path.isdir(dir_path + '\\_OUTPUT_') == True:
            outdir = dir_path + '\\_OUTPUT_'
        else:
            outdir = os.mkdir(dir_path + '\\_OUTPUT_')
            print('let me make you an outbox')
        if os.path.isdir(dir_path + '\\_COPY_') == True:
            copdir = dir_path + '\\_COPY_'
        else:
            copdir = os.mkdir(dir_path + '\\_COPY_')
            print('let me make you an copybox')
    else:
        print('this is linux')
        if os.path.isdir(dir_path + '//_INPUT_') == True:
            indir = dir_path + '//_INPUT_'
        else:
            indir = os.mkdir(dir_path + '//_INPUT_')
            print('let me make you an inbox')
        if os.path.isdir(dir_path + '//_OUTPUT_') == True:
            outdir = dir_path + '//_OUTPUT_'
        else:
            outdir = os.mkdir(dir_path + '//_OUTPUT_')
            print('let me make you an outbox')
        if os.path.isdir(dir_path + '//_COPY_') == True:
            copdir = dir_path + '//_COPY_'
        else:
            copdir = os.mkdir(dir_path + '//_COPY_')
            print('let me make you an copybox')

#LINUX DIRECTORY HANDLING

dir_check()

##PURPOSE: compare two pandas series containing continuous information and 
##         return indexing/metadata differences
##  continuous information = strings, text, etc idk
# def contcoldiff(c1,c2):
#     c1 = 


##PURPOSE: compare two pandas dataframes and return a table with differences
##differences include: 
##  rows missing/present in either table
##  statistical differences between rows?
##  stat diff between metadata of the tables
def tabdiff(t1,t2):
    col1_unique=[]
    col2_unique=[]
    row1_unique=[]
    row2_unique=[]
    ##checking tables for differences in columns
    if t1.shape != t2.shape or sorted(t1.columns) != sorted(t1.columns):
        if t1.shape[1] != t2.shape[1]:
            for x in t1.columns:
                if x not in t2.columns:
                    col1_unique.append(x)
            for x in t2.columns:
                if x not in t1.columns:
                    col2_unique.append(x)
        elif t1.shape[1] == t2.shape[1] and sorted(t1.columns) != sorted(t2.columns):
            for x in t1.columns:
                if x not in t2.columns:
                    col1_unique.append(x)
            for x in t2.columns:
                if x not in t1.columns:
                    col2_unique.append(x)
        else:
            print('Both tables have the same columns')
    else:
        print('Both tables have the same columns')
        
    ##checking tables for differences in rows
    for x in t1.columns:
        colrow1_unique = []
        for y in t1[x]:
            if t2.columns.contains(x) and str(y).split(' ')[0] not in str(t2[x]):
                colrow1_unique.append(y)
        row1_unique.append(colrow1_unique)
    for x in t2.columns:
        colrow2_unique = []
        for y in t2[x]:
            if t1.columns.contains(x) and str(y).split(' ')[0] not in str(t1[x]):
                colrow2_unique.append(y)
        row2_unique.append(colrow2_unique)
        
    else:
        print('Both tables have the same rows')
    col1 = pd.Series(col1_unique)
    col2 = pd.Series(col2_unique)
    row1 = pd.Series(row1_unique)
    row2 = pd.Series(row2_unique)

    return col1, col2, row1, row2

t1 = pd.read_excel(dir_path+'\\_INPUT_\\jsf_testing.xlsx', encoding='utf-8') 
t2 = pd.read_excel(dir_path+ '\\_INPUT_\\sabr_testing.xlsx', encoding='utf-8') 
col1, col2, row1, row2 = tabdiff(t1, t2)

c1 = [x for x in col1]
c2 = [x for x in col2]
print('Table 1 has %s columns'%t1.shape[1],'and %s rows.'%t1.shape[0])
print('Table 2 has %s columns'%t2.shape[1], 'and %s rows.'%t2.shape[0])

line1 = "Table 1 contains columns %s which do not exist in table 2"%c1
line2 = "Table 2 contains columns %s which do not exist in table 1"%c2
#line3 = "Table 1 contains row values for %s which don't exist in table 2. These values are:"
#line4 = "Table 2 contains row values for %s which don't exist in table 2. These values are:"
print(line1)
print(line2)
