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
    print(t1.shape, t1.__class__, '\n\n', t2.shape, t2.__class__)
    col1_unique=[]
    col2_unique=[]
    row1_unique=[]
    row2_unique=[]
    if t1.shape != t2.shape:
        if t1.shape[0] > t2.shape:
            for x in t1.columns:
                if x not in t2.columns:
                    col1_unique.append(x)
        elif t2.shape > t1.shape:
            for x in t2.columns:
                if x not in t1.columns:
                    col2_unique.append(x)
        elif t1.shape[0] == t2.shape[0] and sorted(t1.columns) != sorted(t2.columns):
            for x in t1.columns:
                if x not in t2.columns:
                    col1_unique.append(x)
        else:
            print('Both tables have the same columns')
    
print(dir_path)
t1 = pd.read_excel(dir_path+'\\_INPUT_\\jsf_testing.xlsx', encoding='utf-8') 
t2 = pd.read_excel(dir_path+ '\\_INPUT_\\sabr_testing.xlsx', encoding='utf-8') 
#print(os.getcwd())
tabdiff(t1, t2)

jk

##########################################

dir_path = os.getcwd()

print(os.path.isdir(dir_path))
print(os.walk)

#for root, dirs, files in os.walk(".", topdown=False):
##     print(files)
##     print(dirs)
#    print(root)
## print(os.fwalk)
