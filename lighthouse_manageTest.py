##Program intent:
#(1) copy lighthouse data to MetroOne
#(2) label copied files as the timestamp for their last modification
#(3) repeat every 5 minutes
#Author: Mattias Herrfurth
import os,  shutil,  time

sourceTool=r'\\LMS-110694002\dataShare\lastTenMinRpt2Node1'
destNode=r'E:\Metrology\lighthouse'


def copyLighthouse(sourceTool, destNode):
    if os.path.exists(sourceTool)==False:
        os.mkdir(sourceTool)
    if os.path.exists(destNode+r'\PROCESSED\RAW')==False:
        os.makedirs(destNode+r'\PROCESSED\RAW')
    if os.path.exists(destNode+r'\UNPROCESSED\RAW')==False:
        os.makedirs(destNode+r'\UNPROCESSED\RAW')
    if os.path.exists(r'E:\Metrology\FlatFiles\processed')==False:
        os.makedirs(r'E:\Metrology\FlatFiles\processed')
    if os.path.exists(r'E:\Metrology\FlatFiles\Unprocessed')==False:
        os.makedirs(r'E:\Metrology\FlatFiles\Unprocessed')
    
    #stepping through files and directories within source directory
    for subdirs, dirs, files in os.walk(sourceTool):
        for file in files:
            #getting a string to represent the timestamp for each file
            t=time.strftime('%Y-%m-%d %H_%M_%S', time.gmtime(os.path.getmtime(subdirs+'\\'+file)))
            #checking for if the files exist in any output directories, else copy the file to UNPROCESSED\RAW
            if os.path.exists(destNode+'\\PROCESSED\\RAW\\LHRAW-'+str(t)+'.txt')==True or os.path.exists(destNode+'\\UNPROCESSED\\RAW\\LHRAW-'+str(t)+'.txt')==True or os.path.exists(destNode+'\\PROCESSED\\DEBUG\\LHRAW-'+str(t)+'.txt')==True:
                pass
            else:
                shutil.copy(subdirs+'\\'+file, destNode+'\\UNPROCESSED\\RAW\\LHRAW-'+str(t)+'.txt')
                print("Lighthouse: "+subdirs+'\\'+file)
#infinite loop calling function every 300 seconds
while True:
    copyLighthouse(sourceTool, destNode)
    time.sleep(300)
