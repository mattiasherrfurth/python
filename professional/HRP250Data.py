##Program intent: 
#(1) copy all "seqstat" files from HRP to E: drive on MetroOne
#(2) move all files from active HRP directory to archived HRP directory
#(3) delete empty directories in the active HRP directory
#(4) have all these things occur every 10 seconds
#Authors: Mattias Herrfurth, Will Dirschka
import os, shutil, time

sourceTool=r'Z:\eagle\seqexp'
sourceToolReturn=r'Z:\eagle\seqexpseq'
destNode=r'E:\Metrology\HRP'
    
def movecopyHRP(sourceTool, sourceToolReturn, destNode):
    n=0
    #checking for if directories exist, creating them if they don't exist
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
    #making target folders for MetroOne
    if os.path.exists(r'E:\Metrology\FlatFiles\processed')==False:
        os.mkdir(r'E:\Metrology\FlatFiles\processed')
    if os.path.exists(r'E:\Metrology\FlatFiles\Unprocessed')==False:
        os.mkdir(r'E:\Metrology\FlatFiles\Unprocessed')
        
    #stepping through directories and folders inside HRP active directory
    for subdirs, dirs, files in os.walk(sourceTool):
        #stepping through files to find all "seqstat" files
        for file in files:
            if 'seqstat' in file:
                #time delay for not copying files during a write
                time.sleep(0.1)
                while os.path.exists(sourceToolReturn+'\\0_processed_seqstat\\'+str(n)+'seqstat.txt')==True:
                    n=n+1
                #copy2 used to copy metadata as well as file contents
                shutil.copy2(subdirs+'\\'+file, destNode+'\\UNPROCESSED\\RAW\\HPRRAW-'+str(n)+'seqstat.txt')
                shutil.move(subdirs+'\\'+file, sourceToolReturn+'\\0_processed_seqstat\\'+str(n)+'seqstat.txt')
                print("HRP250: "+subdirs+'\\'+file)
            else:
                #making directories in archive directory identical to original directory paths in active directory
                if os.path.exists(subdirs.replace(sourceTool, sourceToolReturn))==False:
                    os.mkdir(subdirs.replace(sourceTool, sourceToolReturn))
                shutil.move(subdirs+'\\'+file, subdirs.replace(sourceTool, sourceToolReturn)+'\\'+file)
        #removing empty directories from active directory
        if not dirs and not files and not subdirs==sourceTool :
            os.rmdir(subdirs)

#infinite loop; calls function every 10 seconds
while True:
    movecopyHRP(sourceTool, sourceToolReturn, destNode)
    time.sleep(10)
