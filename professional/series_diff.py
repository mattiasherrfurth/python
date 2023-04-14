##Purpose: take two pandas series and return differences for values, metadata, etc.

import os, pandas as pd, seaborn as sb
dir_path = os.getcwd()
t1 = pd.read_excel(dir_path+'\\_INPUT_\\jsf_testing.xlsx', encoding='utf-8') 
t2 = pd.read_excel(dir_path+ '\\_INPUT_\\sabr_testing.xlsx', encoding='utf-8') 

def series_diff(s1, s2):
    for x in s1:
        for y in s2:
            if x == y:
                print(x, 'is the same as', y)
                break

series_diff(t1['Yield'], t2['Yield'])










#f1 = pd.concat([t1['Yield'], t2['Yield']],  axis=1)
#
#
##print(f1)
##print(t1.shape, t2.shape)
#print(f1)
