##Program intent:
##plot data obtained from a CSV data file
#import os, sys, time
#import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook
from csv import reader

file_name=r'C:\Users\J20032\Documents\Python-Plotting\examples\HRP-example.csv'

##opening the csv file and creating the header and data lists
with open(file_name,  'r') as f:
    file = list(reader(f))
    header = file[0]
    data = file[1:]

##asking what should be plotted
print('Enter the x-axis:')
xname=input()
xdat=[]
print('Enter the y-axis:')
yname=input()
ydat=[]

##obtaining index for data to be plotted
for item in header:
    if item == xname:
        xval = header.index(item)
    if item == yname:
        yval = header.index(item)

##creating list of data to be plotted
for list in data:
    for item in list:
        if list.index(item) == xval:
            xdat.append(item)
        if list.index(item) == yval:
            ydat.append(item)
plt.plot(xdat, ydat)

plt.show()
