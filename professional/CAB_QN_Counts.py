import pandas as pd

df = pd.read_excel(r'C:\Users\J20032\Documents\AMEC_CAB_RAW_20190520.xlsx')

cnts = []

for x in df['Part Number'].unique():
    cnt = df[df['Part Number'] == x].shape[0]
    cnts = cnts + [{'PN':x, 'cnt':cnt}]

cnts = sorted(cnts, key = lambda i: i['cnt'])