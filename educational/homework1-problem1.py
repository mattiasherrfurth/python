############### PROBLEM 1 ##################
import seaborn as sns
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
sns.set_style('darkgrid')
print('imported everything')

df = sns.load_dataset('anscombe')
print('imported anscombe')
print(df.head(),'\n\n',df.tail(),'\n\n',df.columns,'\n\n',df.__class__,'\n\n',df.dataset.__class__)

##### https://en.wikipedia.org/wiki/Anscombe%27s_quartet

dfI = df.loc[df['dataset'] == 'I']
dfII = df.loc[df['dataset'] == 'II']
dfIII = df.loc[df['dataset'] == 'III']
dfIV = df.loc[df['dataset'] == 'IV']

print(df.shape,'\n\n',dfI.shape,'\n\n',dfII.shape,'\n\n',dfIII.shape,'\n\n',dfIV.shape)

# print(df.shape[0],'   ',df.shape[1])
# print('dfI now contains filtered df\n\n',dfI.head(),'\n\n',dfI.tail(),'\n\n',df.shape)

print('here is are the central tendencies for y-values in df:\n',df.y.describe())
print('\n\nnow here they are for dfI:\n',dfI.y.describe())
print('\n\nnow here they are for dfII:\n',dfII.y.describe())
print('\n\nnow here they are for dfIII:\n',dfIII.y.describe())
print('\n\nnow here they are for dfIV:\n',dfIV.y.describe())

sns.lineplot(x='x',y='y',data=df)
sns.lineplot(x='x',y='y',data=dfI)
sns.lineplot(x='x',y='y',data=dfII)
sns.lineplot(x='x',y='y',data=dfIII)
sns.lineplot(x='x',y='y',data=dfIV)
print('test')
