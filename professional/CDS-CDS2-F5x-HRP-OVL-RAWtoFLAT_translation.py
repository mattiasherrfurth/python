##program intent:
import os, time, csv, re

#save function
def OutputSQLFile(BlackList, mask, lotID, header, dataHeader, Result, FileName, tool, file, FLATout):
    if mask in BlackList and not 'c3' or 'cl' or 'pm' or 'jm' or 'p3' in lotID:
        print('black %s'%mask)
        resultData = header + dataHeader + Result
        if os.path.exists(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\LMS-simfolder')==False:
            os.makedirs(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\LMS-simfolder')
        sw1 = open(FileName.replace(FLATout, r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\LMS-simfolder'))
        sw1.write(resultData)
            
        #incomplete

########## OVL FLAT generation ##########
#def OVLFlat():
#    tool = 'OVL'
#    RAWin = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\OVL\UNPROCESSED\RAW'
#    RAWout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\OVL\PROCESSED\RAW'
#    FLATout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\FlatFiles\Unprocessed'
    #incomplete
    
########## HRP FLAT generation ##########
def HRPFlat():
#    tool = 'HRP'
    RAWin = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\HRP\UNPROCESSED\RAW'
#    RAWout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\HRP\PROCESSED\RAW'
#    FLATout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\FlatFiles\Unprocessed'
    for dirpath, dirs, files in os.walk(RAWin):
        for doc in files:
                ##PUT THESE IN A TRY STATEMENT
                print(str(os.path.dirname(doc)))
                file = dirpath + '\\' + doc
                seqSource = file.replace(os.path.basename(file), "")
                #various timestamps
                runDate = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(dirpath+'\\'+doc)))
                runTime = time.strftime('%H:%M:%S', time.gmtime(os.path.getmtime(dirpath+'\\'+doc)))
                inDate = time.strftime('%m%d%Y', time.gmtime(os.path.getmtime(dirpath+'\\'+doc)))
                inTime = time.strftime('%H%M%S', time.gmtime(os.path.getmtime(dirpath+'\\'+doc)))
                dt = time.strftime('%m%d%Y-%H%M', time.gmtime(os.path.getmtime(dirpath+'\\'+doc)))
                dtAlt = time.strftime('%Y%m%d-%H%M', time.gmtime(os.path.getmtime(dirpath+'\\'+doc)))
                #process data
                Result = []
                dataHeader = 'subrecipe,SiteName,Site,Success,X,Y'   
                rawData=open(file, 'r').readlines() except if whitespace
                for line in rawData:
                    print(line)
#                rawData =open(file,  'r').readlines()
                junk
                header = []
                print(rawData)
#                for line in rawData:
#                    if 'Lot ID: ' in str(line):
#                        try:
#                            lotIDraw = line[8:]
#                            lotID = re.sub(r'[\x00-\x20\x22\x2a\x2c\x2f\x3a\x3c\x3e-\x3f\x5c\x7c\x7f\s]','',lotIDraw)
#                            CleanedLotID = lotID.replace('_', '-').split('-')
#                            CleanedLotID = CleanedLotID[0]
#                            if CleanedLotID == '':
#                                CleanedLotID = 'BlankCleanedLotID'
#                            if lotID == '':
#                                lotID = 'BlankLotID'
#                            print(CleanedLotID)
#                            print(lotID)
#                        except Exception as e:
#                            print(e)
#                    elif 
#                        
#            except Exception as e:
#                print(e)
            
HRPFlat()
