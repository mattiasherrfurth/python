##Program intent:
##plot SPC data with control limits and target value
##Author: Mattias Herrfurth
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as dates
##opening up an array of date and data values
with open(r'C:\Users\J20032\Documents\Python-Plotting\examples_spc\hrp-ex1-spc.csv',  "r") as doc:
    f=list(csv.reader(doc))
    histdat = f[1:]
    for slot in histdat:
        slot[0]=slot[0].strip()
uplim=500
lowlim=200
target=350

##function to plot array of (time, data) and upper limits, lower limits, and target line
##plotvs for selecting what to plot along the x-axis (time or wafer id)
def plotSPC(uplim, lowlim, target, histdat):
    time=[None]*histdat.__len__()
    data=[None]*histdat.__len__()
    lot=[]
    x=0
    ##pulling time and data from histdat array
    for item in histdat:
        ##converting string for time to strftime format (can only take this format)
        time[x]=datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S")
        data[x]=float(item[1])
        lot+=[str(item[2])+str(item[3])]
        x+=1
    ##assigning fig and ax to figure and axes objects in pyplot
    fig, ax = plt.subplots(1)
    ##formatting for x-axis to plot by date-time
    fig.autofmt_xdate()
    ##plotting data over time as a scatter plot
    plt.plot(time, data, "o")
    ##formatting x-axis
    timefmt=dates.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(timefmt)
    ##creating horizontal lines for upper limit (red), lower limit (red), and target (green)
    plt.axhline(uplim, color = 'r')
    plt.axhline(lowlim, color='r')
    plt.axhline(target, color='g')
    plt.show()

##calling function
plotSPC(uplim, lowlim, target, histdat)

