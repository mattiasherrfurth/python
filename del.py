import datetime

timeAstart=datetime.datetime.now()
time=[None]*100000
for index in range(100000):
    time[index]="asd"
timeAend=datetime.datetime.now()


timeBstart=datetime.datetime.now()
lot=[]
for index in range(100000):
    lot+=["asd"]
timeBend=datetime.datetime.now()
    
print(timeAend-timeAstart)
print(timeBend-timeBstart)
