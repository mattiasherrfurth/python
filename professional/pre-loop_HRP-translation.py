#program intent:
#External interaction:
import os, shutil, time
sourceTool=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\source1'
#sourceTool=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\source1'
sourceToolReturn=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\source2'
destNode=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\output'
    
def movecopyHRP(sourceTool, sourceToolReturn, destNode):
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
        
    for subdirs, dirs, files in os.walk(sourceTool):
        for file in files:
            if 'seqstat' in file:
                time.sleep(0.1)
                while os.path.exists(sourceToolReturn+'\\0_processed_seqstat\\'+str(n)+'seqstat.txt')==True:
                    n=n+1
                shutil.copy2(subdirs+'\\'+file, destNode+'\\UNPROCESSED\\RAW\\HPRRAW-'+str(n)+'seqstat.txt')
                shutil.move(subdirs+'\\'+file, sourceToolReturn+'\\0_processed_seqstat\\'+str(n)+'seqstat.txt')
                print("HRP250: "+subdirs+'\\'+file)
            else:
                if os.path.exists(subdirs.replace(sourceTool, sourceToolReturn))==False:
                    os.mkdir(subdirs.replace(sourceTool, sourceToolReturn))
                shutil.move(subdirs+'\\'+file, subdirs.replace(sourceTool, sourceToolReturn)+'\\'+file)
        if not dirs and not files and not subdirs==sourceTool :
            os.rmdir(subdirs)

while True:
    movecopyHRP(sourceTool, sourceToolReturn, destNode)
    time.sleep(10)

    
    


    #making target folders

    ##making target folders for E: drive
    #if os.path.exists(r'E:\Metrology\FlatFiles\processed')==False:
    #    os.mkdir(r'E:\Metrology\FlatFiles\processed')
    #if os.path.exists(r'E:\Metrology\FlatFiles\Unprocessed')==False:
    #    os.mkdir(r'E:\Metrology\FlatFiles\Unprocessed')


    #clean out non Seqstat.txt
    #moving files: >shutil.move(source, destination)
    #copying files: >shutil.copy(source, destination)
    #make filename string: >ntpath.basename("filepath")

    #retain metadata of files moved
    #loop
