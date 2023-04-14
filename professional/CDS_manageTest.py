##Program intent:
#(1) copy CDS files from source to MetroOne
#(2) remove empty directories from source
#(3) repeat every 5 seconds
#Author: Mattias Herrfurth

import os, time, shutil
##variable setting for G-mod
sourceTool=r'\\169.254.103.243\share\DataFiles'
sourceToolReturn=r'\\169.254.103.243\share\Processed DataFiles'
destNode=r'E:\Metrology\cds'

def CDSmanage(sourceTool, sourceToolReturn, destNode):
    n=0
    if os.path.exists(sourceTool)==False:
        os.mkdir(sourceTool)
    if os.path.exists(sourceToolReturn)==False:
        os.mkdir(sourceToolReturn)    
    if os.path.exists(destNode)==False:
        os.mkdir(destNode)
    if os.path.exists(sourceToolReturn+r'\0_processed_seqstat')==False:
        os.mkdir(sourceToolReturn+r'\0_processed_seqstat')    
    if os.path.exists(destNode+r'\UNPROCESSED\RAW')==False:
        os.makedirs(destNode+r'\UNPROCESSED\RAW')
    if os.path.exists(r'E:\Metrology\FlatFiles\processed')==False:
        os.mkdir(r'E:\Metrology\FlatFiles\processed')
    if os.path.exists(r'E:\Metrology\FlatFiles\Unprocessed')==False:
        os.mkdir(r'E:\Metrology\FlatFiles\Unprocessed')
    for subdirs, dirs, files in os.walk(sourceTool):
        #removing empty directories before move/copy
        if not dirs and not files and not subdirs==sourceTool :
            os.rmdir(subdirs)
        for file in files:
            n=0
            print(file)
            #loop to give new copies of files unique sequential names
            while os.path.exists(destNode+'\\UNPROCESSED\\RAW\\CDSRAW-'+file.replace('.xls', '_'+str(n)+'.xls'))==True:
                n=n+1
            shutil.copy(subdirs+'\\'+file, destNode+'\\UNPROCESSED\\RAW\\CDSRAW-'+file.replace('.xls', '_'+str(n)+'.xls'))
            if os.path.exists(subdirs.replace(sourceTool, sourceToolReturn))==False:
                os.makedirs(subdirs.replace(sourceTool, sourceToolReturn))
            shutil.move(subdirs+'\\'+file, subdirs.replace(sourceTool, sourceToolReturn)+'\\'+file)
            #removing empty directories after move/copy
            if not dirs and not files and not subdirs==sourceTool :
                os.rmdir(subdirs)
#infinite loop calling function every 5 seconds
while True:
    CDSmanage(sourceTool, sourceToolReturn, destNode)
    time.sleep(5)
