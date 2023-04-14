##program intent:
import os, socket, sys, time, select
from threading import Timer
from datetime import datetime
destNode=r'E:\Metrology\F5x'
issueflag=0
try:
        
    while True:
        if os.path.exists(destNode)==False:
            os.mkdir(destNode)
        if os.path.exists(destNode+r'\PROCESSED\RAW')==False:
            os.makedirs(destNode+r'\PROCESSED\RAW')
        if os.path.exists(destNode+r'\UNPROCESSED\RAW')==False:
            os.makedirs(destNode+r'\UNPROCESSED\RAW')
        if os.path.exists(destNode+r'E:\Metrology\FlatFiles\processed')==False:
            os.makedirs(destNode+r'E:\Metrology\FlatFiles\processed')
        if os.path.exists(destNode+r'E:\Metrology\FlatFiles\Unprocessed')==False:
            os.makedirs(destNode+r'E:\Metrology\FlatFiles\Unprocessed')
        TCP_IP = '192.168.6.65'
        TCP_PORT = 100
        TIMEOUT = 1
        rawData = ''
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)
            sock.connect((TCP_IP,TCP_PORT))
            print('Connected to F5x')
            issueflag=0
            conn=1
        except:
            if issueflag==0:
                print('%s - F5x Unreachable'% datetime.now())
                issueflag=1
            
            conn=0
            sock.close()
        
        tim1=0
        
        while conn==1:
            try:#see if network connected
                socktest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socktest.settimeout(TIMEOUT/10)
                socktest.connect((TCP_IP,80))
                socktest.close()
            except:
                conn+=1
                print('issue:network disconnected')
            
            try:#see if power cycled
                socktest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socktest.settimeout(TIMEOUT/10)
                socktest.connect((TCP_IP,TCP_PORT))
                socktest.close()
                conn+=1
                print('issue:power cycled')
            except:
                trash=1
            #pulling data from F5x
            dataFlag, w, e = select.select([sock], [], [],0.1)
            if(dataFlag.__len__() > 0):
                #decoding input data
                output = sock.recv(1024).decode()
                rawData += output
                tim1=time.time()
            
            if (time.time()>(tim1+1) or not conn==1) and rawData.__len__()>0:
                file = open(destNode+'\\UNPROCESSED\\RAW\\F5xRAW-%s'%datetime.now().strftime('%Y-%m-%d %H_%M_%S')+'.txt','w+')
                print('wrote file %s'%datetime.now().strftime('%Y-%m-%d %H_%M_%S'))
                trash=file.write(rawData)
                file.close()
                rawData=''
        
        try:
            sock.close()
        except:
            conn=0
except KeyboardInterrupt:
    try:
        sock.close()
    except:
        conn=0

