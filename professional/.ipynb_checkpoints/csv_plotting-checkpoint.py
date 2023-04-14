##Program intent:
##plot data obtained from a CSV data file
##Author: Mattias Herrfurth
#import os, sys, time
#import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook
import csv

file_name=r'C:\Users\J20032\Documents\Python-Plotting\examples\hrp-ex1.csv'

def plotCSV(file_name):
    ##opening the csv file and creating the header and data lists
    f=open(file_name,  "r")
    file=list(csv.reader(f))
    header = file[0]
    n=0
    ##removing spaces from file
    for obj in header:
        header[n]=header[n].strip()
        n+=1
    data = file[1:]
    for item in data:
        if item.__len__() != header.__len__():
            data.remove(item)
    ##asking what should be plotted
    ##group = column id from CSV file
    ##example: "waferid"
    print('What is the group?')
    #group=input()
    group='collectiondatetime'
    ##group_item = set of samples from the column
    ##example: waferid = "8"
    print('Which group item?')
    #group_item=input()
    group_item='2017-02-28 10:56:54'
    print('Enter the x-axis data name:')
    #xname=input()
    xname='site'
    xdat=[]
    print('Enter the y-axis data name:')
    #yname=input()
    yname='height'
    ydat=[]
    ##obtaining index for data to be plotted
    for item in header:
        if item == xname:
            xval = header.index(item)
        if item == yname:
            yval = header.index(item)
        if item == group:
            groupval = header.index(item)
##if metrovision code has menu to select group, xname, etc, then don't need error handling for improper variables
#    if 'xval' not in locals():
#        print("The x-axis is not valid!")
#    if 'yval' not in locals():
#        print("The y-axis is not valid!")
#    if 'groupval' not in locals():
#        print("The group is not valid!")
    ##creating list of data to be plotted
    for par in data:
        if par[groupval].strip() == group_item:
            ##index variable because couldn't assign
            ind=0
            for item in par:
                if ind == xval:
                    xdat.append(item)
                if ind == yval:
                    ydat.append(item)
                ind+=1
    ##creating plot, labels, and titles
    plt.plot(xdat, ydat)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title('Plot of %s'%group + ' %s'%group_item)
    #plt.savefig("test.pdf")
    plt.show()

##calling function
plotCSV(file_name)
