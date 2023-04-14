##Program intent:
#(1) Copy CDS files from tool to MetroOne
#Authors: Mattias Herrfurth

import os, time, shutil
##variable setting for G-mod
#sourceTool=r'\\169.254.103.243\share\DataFiles'
#sourceToolReturn=r'\\169.254.103.243\share\Processed DataFiles'
#destNode=r'E:\Metrology\cds'
sourceTool=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\source1'
sourceToolReturn=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\source2'
destNode=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\output'

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
    ##making target folders for E: drive
    #if os.path.exists(r'E:\Metrology\FlatFiles\processed')==False:
    #    os.mkdir(r'E:\Metrology\FlatFiles\processed')
    #if os.path.exists(r'E:\Metrology\FlatFiles\Unprocessed')==False:
    #    os.mkdir(r'E:\Metrology\FlatFiles\Unprocessed')
    for dirpath, dirnames, files in os.walk(sourceTool):
        ##removing empty directories before move/copy
        #if does not contain directories and does not contain files and is not the source directory, remove the directory
        if not dirnames and not files and not dirpath==sourceTool :
            os.rmdir(dirpath)
        for file in files:
            n=0
            print(file)
            ##loop to give new copies of files unique sequential names
            #file.replace - replace works to replace one string in a longer string with another string
            #n is the number for the file to be written
            while os.path.exists(destNode+'\\UNPROCESSED\\RAW\\CDSRAW-'+file.replace('.xls', '_'+str(n)+'.xls'))==True:
                n=n+1
            ##copying file with sequential enumeration
            shutil.copy(dirpath+'\\'+file, destNode+'\\UNPROCESSED\\RAW\\CDSRAW-'+file.replace('.xls', '_'+str(n)+'.xls'))
            if os.path.exists(dirpath.replace(sourceTool, sourceToolReturn))==False:
                os.makedirs(dirpath.replace(sourceTool, sourceToolReturn))
            shutil.move(dirpath+'\\'+file, dirpath.replace(sourceTool, sourceToolReturn)+'\\'+file)
            ##removing empty directories
            if not dirnames and not files and not dirpath==sourceTool :
                os.rmdir(dirpath)
#infinite loop calling function every 5 seconds
while True:
    CDSmanage(sourceTool, sourceToolReturn, destNode)
    time.sleep(5)
