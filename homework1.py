############### PROBLEM 1 ##################
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

################# PROBLEM 2 #################
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#  A pandas Series made from 800 random values, drawn 
#  from a Gaussian (normal) distribution
series = pd.Series(np.random.normal(size=800))

# Cut the window in 2 parts
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
 
#  Add a graph in each part
#
#  Note that the axes object can be specified at the 
#  time we generate the graph, letting us customize
#  displaying multiple graphs at once.
sns.boxplot(series, ax=ax_box)
sns.distplot(series, ax=ax_hist)
 
#  Remove x axis name for the boxplot
ax_box.set(xlabel='')

#  A pandas Series made from 800 random values, drawn 
#  from a Gaussian (normal) distribution
series = pd.Series(np.random.normal(size=800))

# Cut the window in 2 parts
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
 
#  Add a graph in each part
#
#  Note that the axes object can be specified at the 
#  time we generate the graph, letting us customize
#  displaying multiple graphs at once.
sns.boxplot(series, ax=ax_box)
sns.distplot(series, ax=ax_hist)
 
#  Remove x axis name for the boxplot
ax_box.set(xlabel='')

#  A pandas Series made from 800 random values, drawn 
#  from a Gaussian (normal) distribution
series = pd.Series(np.random.normal(size=800))

# Cut the window in 2 parts
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
 
# #  Add a graph in each part
# #
# #  Note that the axes object can be specified at the 
# #  time we generate the graph, letting us customize
# #  displaying multiple graphs at once.
# sns.boxplot(series, ax=ax_box)
# sns.distplot(series, ax=ax_hist)
 
# #  Remove x axis name for the boxplot
# ax_box.set(xlabel='')


def distboxplot(data):
    #defining a plot with two subplots for a box plot and a distribution plot
    f, (ax_hist, ax_box) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.85, .15)})
    sns.boxplot(data, ax=ax_box)
    sns.distplot(data, ax=ax_hist)
    ax_box.set(xlabel='')


#  A pandas Series made from 800 random values, drawn 
#  from a Gaussian (normal) distribution
series = pd.Series(np.random.normal(size=200))
distboxplot(series)

def distboxplot(data):
    #defining a plot with two subplots for a box plot and a distribution plot
    f, (ax_hist, ax_box) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.85, .15)})
    sns.boxplot(data, ax=ax_box)
    sns.distplot(data, ax=ax_hist)
    ax_box.set(xlabel='')


#  A pandas Series made from 800 random values, drawn 
#  from a Gaussian (normal) distribution
series = pd.Series(np.random.normal(size=200))
distboxplot(series)

############## PROBLEM 3 #######################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=4000, centers=3, n_features=2, random_state=0)

blobs = pd.DataFrame(dict(zip(("x", "y", "group"), (X[:,0], X[:,1], y))))

########https://seaborn.pydata.org/generated/seaborn.scatterplot.html

sns.scatterplot(blobs.x, blobs.y)

X, y = make_blobs(n_samples=4000, centers=3, n_features=2, random_state=0)

# X = make_blobs(n_samples=4000, centers=3, n_features=1, random_state=None)
# y = make_blobs(n_samples=4000, centers=3, n_features=1, random_state=None)
# print(X,'\n\n',y,'\n\n',X.shape,y.shape)
# print(X.__class__,y.__class__)
blobs = pd.DataFrame(dict(zip(("x", "y", "group"), (X[:,0], X[:,1], y))))

# sns.scatterplot(blobs.x, blobs.y)

blobs = pd.DataFrame(dict(zip(("x", "y", "group"), (X[:,0], X[:,1], y))))
sns.jointplot(blobs.x, blobs.y, kind='hex',color='#4CB391')

blobs = pd.DataFrame(dict(zip(("x", "y", "group"), (X[:,0], X[:,1], y))))
# print(blobs.x)
# print(blobs.y)
# sns.scatterplot(blobs.x,blobs.y,marker="+")

sns.scatterplot(blobs.x,blobs.y,marker=0)

sns.jointplot(blobs.x, blobs.y, kind="kde", height=7, space=0)

############ PROBLEM 4 ################
###Assumption 1: only strings will be passed to pattern and text
###Assumption 2: text will need to be parsed by line
    
def searchy(pattern, text, ignorecase=False):
    import re
    pres = 0
    if ignorecase==True:
        pattern1 = pattern.lower()
        text1 = text.lower()
        n=0
        for x in text1.split('\n'):
            n+=1
            if pattern1 in x:
                return([text.split('\n')[n-1]])
                pres = 1
            else:
                pass
    elif ignorecase==False:
        for x in text.split('\n'):
            if pattern in x:
                return([x])
                pres = 1
            else:
                pass
    else:
        print('Please give ignorecase a boolean')
    if pres == 0:
        return([])
    
# A sample string to search through
rain_in_spain = 'The rain\n in spain \nfalls mainly on the plane'

# print(searchy('rain', rain_in_spain))

assert searchy('rain', rain_in_spain) == ['The rain']
assert searchy('Rain', rain_in_spain) == []
assert searchy('Rain', rain_in_spain, ignorecase=True) == ['The rain']

print('good')

# print(searchy('Rain', rain_in_spain, ignorecase=True))