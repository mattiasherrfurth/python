import os, time, csv, re, shutil
##save function
def OutputSQLFile(BlackList, mask, lotID, header, dataHeader, result, fileName, tool, file, FLATout, dirpath, RAWin):
    if mask in BlackList and not ('c3' or 'cl' or 'pm' or 'jm' or 'p3' in lotID):
        print('black %s'%mask)
        resultData = header + dataHeader + result
        if os.path.exists(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\LMS-simfolder')==False:
            os.makedirs(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\LMS-simfolder')
        sw1 = open(fileName.replace(FLATout, r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\LMS-simfolder'))
        sw1.write(resultData)
        sw1.close()
        if os.path.exists(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\BlackSource'+'\\'+tool)==False:
            os.makedirs(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\BlackSource'+'\\'+tool)
        shutil.move(dirpath+'\\'+file, dirpath.replace(RAWin, r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\BlackSource')+'\\'+file)
    else:
        resultData='' + header + dataHeader + result
        sw1 = open(fileName, 'w')
        sw1.write(resultData)
        sw1.close()
        

##loading blacklist
if os.path.exists(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\BlackList.csv')==True:
    with open(r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\BlackList.csv', 'r') as f:
        reader = csv.reader(f)
        BlackList = str(list(reader))
else:
    BlackList = ''
##function for HRP file reading
def HRPFlat():
    tool = 'HRP'
    RAWin = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\HRP\UNPROCESSED\RAW'
    RAWout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\HRP\PROCESSED\RAW'
    FLATout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\FlatFiles\Unprocessed'
    t1=0; t2=0
    #stepping through source directory
    for dirpath, dirs, files in os.walk(RAWin):
        time.sleep(0.01)
        try:
            #looking at each file in directory
            for file in files:
                #assigning various time stamps
                runDate = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(dirpath+'\\'+file)))
                runTime = time.strftime('%H:%M:%S', time.localtime(os.path.getmtime(dirpath+'\\'+file)))
                inDate = time.strftime('%m%d%Y', time.localtime(os.path.getmtime(dirpath+'\\'+file)))
                inTime = time.strftime('%H%M%S', time.localtime(os.path.getmtime(dirpath+'\\'+file)))
                doc = dirpath + '\\' + file
                result = ''
                dataHeader = 'subrecipe,SiteName,Site,Success,X,Y'
                reading = open(doc, 'r').readlines()
                header = ''
                headerPlus = ''
                #reading each line in file
                for line in reading:
                    #array used to look at specific elements in lines
                    array = line.replace(' ', '').split('\t')
                    #series of if and elif statements to handle lines individually
                    if 'Lot ID: ' in line:
                        try:
                            lotID = line.replace('\n','').replace('Lot ID: ','')
                            lotID = re.sub(r'[\x00-\x20\x22\x2a\x2c\x2f\x3a\x3c\x3e-\x3f\x5c\x7c\x7f\s]','',lotID)
                            cleanedLotID = lotID.replace('_', '-').split('-')
                            cleanedLotID = cleanedLotID[0]
                            if lotID == '':
                                lotID = 'BlankLotID'
                            if cleanedLotID == '':
                                cleanedLotID = 'BlankCleanedLotID'
                        except Exception as e:
                            print(e)
                    elif 'Sequence ID:' in line:
                        try:
                            sequenceRecipe = line.replace('\n', '').replace('Sequence ID: ', '').strip()
                            product = re.sub(r'[\x00-\x20\x22\x2a\x2c\x2f\x3a\x3c\x3e-\x3f\x5c\x7c\x7f\s]','',sequenceRecipe).split('_')
                            spec = product[1]
                            if spec != None and (spec[:1]=="Q" or spec[:1]=="P" or spec[:1]=="E") and len(spec)==5:
                                try:
                                    specNum = 0+spec[1:len(spec)].replace(' ', '')
                                    if specNum == '' or specNum == None:
                                        spec = 'BlankSpec'
                                    if (10000 < 0+specNum) or (0+specNum < -1):
                                        spec = 'BlankSpec'
                                except Exception as e:
                                    print(e)
                            else:
                                spec = 'BlankSpec'
                            mask = product[0].strip()
                        except Exception as e:
                            print(e)
                        try:
                            sequence = sequenceRecipe.replace('-', '_').split('_')
                            if sequence[1][:1] == 'M' or sequence[1][:1] == 'I' or sequence[1][:1] == 'V':
                                level = sequence[1].strip()
                                step = sequence[2].strip()
                            else:
                                level = 'BlankLevel'
                                step = sequence[1].strip()
                        except Exception as e:
                            print(e)
                            mask = 'BlankMask'
                            step = 'BlankStep'
                            level = 'BlankLevel'
                    elif 'Operator ID: ' in line:
                        try:
                            user = line.replace('\n', '').replace('Operator ID: ', '').strip()
                            if user =='':
                                user='BlankUser'
                        except Exception as e:
                            print(e)
                    elif 'Recipe: ' in line:
                        scanRecipe = line.replace('\n', '').replace('Recipe: ', '').strip()
                        waferID=''; siteName=''; site=''; name=''; units=''; success=''; x=''; y=''; results=''
                    elif 'Params:' in line:
                        t1 = 1
                    elif t1 == 1:
                        t1 = 0
                        name = array
                    elif 'Units:' in line:
                        t2 = 1
                    elif t2 == 1:
                        t2 = 0
                        units = array
                    elif len(array)>2 and ('None' in array[1] or 'Passed' in array[1]):
                        waferID = array[0].strip()
                        if 'slot' in waferID:
                            slot = waferID.replace('slot', '')
                        else:
                            slot = 'BlankSlot'
                        if waferID=='' or 'slot' in waferID:
                            waferID = 'BlankWaferID'
                    elif 'Site:' in line:
                        if result!='':
                            headerPlus = ''+headerPlus+header+dataHeader+'\n'+result
                            useHeader = True
                        #making header
                        oldSite = 0
                        dataHeader = 'Subrecipe,SiteName,Site,Success,X,Y'
                        result = ''
                        header = ''
                        header += '<HEADER>\n'
                        header += 'ToolArea,Metrology\n'
                        header += 'ToolType,Profiler\n'
                        header += 'Tool,%s\n' %tool
                        header += 'CleanedLotID,%s\n' %cleanedLotID
                        header += 'LotID,%s\n' %lotID
                        header += 'Mask,%s\n' %mask
                        header += 'Level,%s\n' %level
                        header += 'Step,%s\n' %step
                        header += 'CollectionDateTime,%s ' %runDate + '%s\n' %runTime
                        header += 'User,%s\n' %user
                        header += 'ProcessSpec,%s\n' %spec
                        header += 'WaferID,%s\n' %waferID
                        header += 'Slot,%s\n' %slot
                        header += 'Recipe,%s\n' %sequenceRecipe
                        header += 'SourceFile,%s\n' %doc
                        header += '<DATA>\n'
                    elif len(array)>3 and ('Y' in array[2]):
                        site = array[0]
                        siteName = array[1]
                        success = array[2]
                        x = array[3]
                        y = array[4]
                        for p in range(5, len(array)):
                            results = array[p].replace('\n', '').replace('\t', '').strip()
                            resultUnits = units[p].replace('\n', '').replace('\t', '').strip()
                            resultName = name[p].replace('\n', '').replace('\t', '').strip()
                            if oldSite != site:
                                try:
                                    tempResult = '%s,%s,%s,%s,%s,%s,'%(scanRecipe, siteName, site, success, x, y)
                                except Exception as e:
                                    print(e)
                                oldSite=site
                            if len(results)>0:
                                try:
                                    tempResult+=(',%s,%s'%(results, resultUnits))
                                    if resultName not in dataHeader:
                                        dataHeader+=',%s,%s units'%(resultName, resultName)
                                except Exception as e:
                                    print(e)
                        result+=tempResult+'\n'
                        print(result)
                        resultName=''; resultUnits = ''; siteName=''; site=''; success=''; x=''; y=''
                    elif len(array)>3 and ('N' in array[2]):
                        site = array[0]
                        siteName = array[1]
                        success = array[2]
                        x = array[3]
                        y = array[4]
                        if oldSite != site:
                            try:
                                tempResult = '%s,%s,%s,%s,%s,%s,'%(scanRecipe, siteName, site, success, x, y)
                            except Exception as e:
                                print(e)
                            oldSite = site
                        result+=tempResult+'\n'
                        resultName=''; resultUnits = ''; siteName=''; site=''; success=''; x=''; y=''
                if result != '':
                    headerPlus = ''+headerPlus+header+dataHeader+'\n'+result+'\n'
                    useHeader = True
                header = headerPlus
                result = ''
                dataHeader = ''
                if useHeader == True:
                    fileName = FLATout+'\\'+tool+'-'+mask+'-'+cleanedLotID+'-'+sequenceRecipe+'-'+inDate+'-'+inTime+'.txt'
                    OutputSQLFile(BlackList, mask, lotID, header, dataHeader, result, fileName, tool, file, FLATout, dirpath, RAWin)
                    shutil.move(dirpath+'\\'+file, dirpath.replace(RAWin, RAWout)+'\\'+file)
                else:
                    print('Issue with file empty %s' %file)
                    result=''
                    shutil.move(dirpath+'\\'+file, dirpath.replace(RAWin, r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\HRP\UNPROCESSED\DEBUG')+'\\'+file)
        except Exception as e:
            print(e)

HRPFlat()
