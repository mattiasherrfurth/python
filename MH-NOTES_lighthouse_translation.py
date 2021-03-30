##Program intent:
#(1) copy lighthouse data to MetroOne
#(2) tag lighthouse copied data as when the original file was last modified
#(3) check for new data to copy over every 300 seconds
#Authors: Mattias Herrfurth
import os,  shutil,  time
##variable setting for lighthouse network (UNCOMMENT IN FINAL IMPLEMENTATION)
#sourceTool=r'\\LMS-110694002\dataShare\lastTenMinRpt2Node1'
#destNode=r'E:\Metrology\lighthouse'
##variable setting for testing code (COMMENT OUT IN FINAL IMPLEMENTATION)
sourceTool=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\source1'
destNode=r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\output'

def copyLighthouse(sourceTool, destNode):
    ##checking for if directories exist; making the directories if they don't exist
    if os.path.exists(sourceTool)==False:
        os.mkdir(sourceTool)
    #makedirs used to create file paths for multiple folders
    if os.path.exists(destNode+r'\PROCESSED\RAW')==False:
        os.makedirs(destNode+r'\PROCESSED\RAW')
    if os.path.exists(destNode+r'\UNPROCESSED\RAW')==False:
        os.makedirs(destNode+r'\UNPROCESSED\RAW')
    ##making target folders for E: drive (UNCOMMENT IN FINAL IMPLEMENTATION)
    #if os.path.exists(r'E:\Metrology\FlatFiles\processed')==False:
    #    os.makedirs(r'E:\Metrology\FlatFiles\processed')
    #if os.path.exists(r'E:\Metrology\FlatFiles\Unprocessed')==False:
    #    os.makedirs(r'E:\Metrology\FlatFiles\Unprocessed')
    
    #stepping through files and directories within a directory
    #os.walk returns a tuple of the subdirectories, directories, and files
    for subdirs, dirs, files in os.walk(sourceTool):
        ##stepping through each file in the files from sourceTool
        for file in files:
            ##getting a string to represent the timestamp for each file
            #os.path.getmtime returns the last modified date in total number of seconds since arbitrary date
            #time.gmtime translates number of seconds into a list of date variables (hours, minutes, seconds, etc.)
            #time.strftime makes the time.gmtime data into a human readable string
            t=time.strftime('%Y-%m-%d %H_%M_%S', time.gmtime(os.path.getmtime(subdirs+'\\'+file)))
            ##checking for if the files exist in any output directories, else copy the file to UNPROCESSED\RAW
            #need to double the backslashes since backslash is an escape character
            if os.path.exists(destNode+'\\PROCESSED\\RAW\\'+str(t)+'.txt')==True or os.path.exists(destNode+'\\UNPROCESSED\\RAW\\'+str(t)+'.txt')==True or os.path.exists(destNode+'\\PROCESSED\\DEBUG\\'+str(t)+'.txt')==True:
                pass
            else:
                ##copying file from one path to another
                #shutil.copy copies the file contents, not the metadata
                shutil.copy(subdirs+'\\'+file, destNode+'\\UNPROCESSED\\RAW\\'+str(t)+'.txt')
                print("Lighthouse: "+subdirs+'\\'+file)
#infinite loop calling function every 5 seconds
while True:
    copyLighthouse(sourceTool, destNode)
    time.sleep(300)
