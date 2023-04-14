##Program intent:
#(1) Manage HRP files (see below for details)
#(2) Manage Lighthouse files (see below for details)
#(3) Manage CDS Files (see below for details)
#Author: Mattias Herrfurth and Will Dirschka
import os, shutil, time, sys
    
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

while True:
	#infinite loop calling function every 5 seconds
    time.sleep(5)
	
	##Program intent: 
	#(1) copy all "seqstat" files from HRP to E: drive on MetroOne
	#(2) move all files from active HRP directory to archived HRP directory
	#(3) delete empty directories in the active HRP directory
	#(4) have all these things occur every 10 seconds
	#Authors: Mattias Herrfurth, Will Dirschka
	#import os, shutil, time, sys
	sourceTool=r'Z:\eagle\seqexp'
	sourceToolReturn=r'Z:\eagle\seqexpseq'
	destNode=r'E:\Metrology\HRP'
    try:
		movecopyHRP(sourceTool, sourceToolReturn, destNode)
	except:
		mainError=sys.exc_info() 
		errorLine=mainError[2].tb_lineno
		print('%s line:%s'%(mainError, errorLine))
    
	##Program intent:
	#(1) copy lighthouse data to MetroOne
	#(2) label copied files as the timestamp for their last modification
	#(3) repeat every 5 minutes
	#Author: Mattias Herrfurth
	#import os,  shutil, time, sys
	sourceTool=r'\\LMS-110694002\dataShare\lastTenMinRpt2Node1'
	destNode=r'E:\Metrology\lighthouse'
    try:
		copyLighthouse(sourceTool, destNode)
	except:
		mainError=sys.exc_info() 
		errorLine=mainError[2].tb_lineno
		print('%s line:%s'%(mainError, errorLine))
	
	##Program intent:
	#(1) copy CDS files from source to MetroOne
	#(2) remove empty directories from source
	#(3) repeat every 5 seconds
	#Author: Mattias Herrfurth
	#import os, time, shutil, sys
	##variable setting for G-mod
	sourceTool=r'\\169.254.103.243\share\DataFiles'
	sourceToolReturn=r'\\169.254.103.243\share\Processed DataFiles'
	destNode=r'E:\Metrology\cds'
    try:
		CDSmanage(sourceTool, sourceToolReturn, destNode)
	except:
		mainError=sys.exc_info() 
		errorLine=mainError[2].tb_lineno
		print('%s line:%s'%(mainError, errorLine))
	


	
	
	
	
	
