import os, time, csv, re, shutil
from time import strftime
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
        dataHeader+='\n'
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
##function for F5x file reading
def F5xFlat():
    tool = 'F5x'
    RAWin = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\F5x\UNPROCESSED\RAW'
    RAWout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\F5x\PROCESSED\RAW'
    FLATout = r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\FlatFiles\Unprocessed'
    for dirpath, dirs, files in os.walk(RAWin):
        time.sleep(0.01)
        #INSERT TRY STATEMENT
            #looking at each file in directory
        for file in files:
            tool=''; spec=''; specNum=''; user=''; mask=''; level=''; step=''; recipe=''; cassette=''; waferID=''; lotID=''; slot=''
            date=''; thyme=''; l9=''; l8=''; l7=''; l6=''; l5=''; l4=''; l3=''; l2=''; l1=''; substrate=''
            filmstack=''; resultNum=1; resultName=''; resultUnits=''; results=''; inTime=0; result=''; header=''
            first=0; save=0
            doc = dirpath + '\\' + file
            dataHeader = 'subrecipe,SiteName,Site,Success,X,Y'
            reading = open(doc, 'r').readlines()
            for line in reading:
                if 'SYSTEM NAME:' in line:
                    tool = line.replace('SYSTEM NAME:', '').strip()
                elif 'USER:' in line:
                    user = line.replace('USER:', '').strip()
                elif 'RECIPE:' in line:
                    recipe = line.replace('RECIPE:', '').strip().replace(' ', '-')                        
                    recipe = re.sub(r'[\x00-\x20\x22\x2a\x2c\x2f\x3a\x3c\x3e-\x3f\x5c\x7c\x7f]','',recipe)
                    spec = recipe.replace('_', '-').split('-')
                    recipe = recipe.replace('-', '')
                    spec = spec[0]
                    if spec != None and (spec[0] == 'Q' or spec [0] == 'P' or spec[0] == 'E') and len(spec)==5:
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
                elif 'CASSETTE:' in line:
                    cassette = line.replace('CASSETTE:', '').strip()
                    cassette = re.sub(r'[\x00-\x20\x22\x2a\x2c\x2f\x3a\x3c\x3e-\x3f\x5c\x7c\x7f]','',cassette)
                    step = cassette.replace('-', '_').split('_')
                    mask = step[0]
                    if mask == '':
                        mask = 'BlankMask'
                    try:
                        if step[1][:1] == 'M' or step[1][:1] == 'I' or step[1][:1] == 'V':
                            level = step[1]
                            step = step[2]
                        else:
                            level = ''
                            step = step[1]
                    except:
                        level = ''
                        step = ''
                    if step == '':
                        step = 'BlankStep'
                    if level == '':
                        level = 'BlankLevel'
                elif 'WAFER ID:' in line:
                    waferID = line.replace('WAFER ID:', '').strip()
                    waferID = re.sub(r'[\x00-\x20\x22\x2a\x2c\x2f\x3a\x3c\x3e-\x3f\x5c\x7c\x7f]','',waferID)
                elif 'LOT ID:' in line:
                    try:
                        lotID = line.replace('LOT ID:', '').strip()
                        lotID = re.sub(r'[\x00-\x20\x22\x2a\x2c\x2f\x3a\x3c\x3e-\x3f\x5c\x7c\x7f]','',lotID)
                        cleanedLotID = lotID.replace('_', '-').split('-')
                        cleanedLotID = cleanedLotID[0]
                        if lotID == '':
                            lotID = 'BlankLotID'
                        if cleanedLotID == '':
                            cleanedLotID = 'BlankCleanedLotID'
                    except Exception as e:
                        print(e)
                elif 'PROCESS DATE:' in line:
                    date = line.replace('PROCESS DATE:', '').strip().replace(',', '')
                    date=date.split(' ')
                    if date[0] == 'January':
                        date[0] = '01'
                    elif date[0] == 'February':
                        date[0] = '02'
                    elif date[0] == 'March':
                        date[0] = '03'
                    elif date[0] == 'April':
                        date[0] = '04'
                    elif date[0] == 'May':
                        date[0] = '05'
                    elif date[0] == 'June':
                        date[0] = '06'
                    elif date[0] == 'July':
                        date[0] = '07'
                    elif date[0] == 'August':
                        date[0] = '08'
                    elif date[0] == 'September':
                        date[0] = '09'
                    elif date[0] == 'October':
                        date[0] = '10'
                    elif date[0] == 'November':
                        date[0] = '11'
                    elif date[0] == 'December':
                        date[0] = '12'
                    inDate = '%s%s%s'%(date[0], date[1], date[2])
                    slotDate = '%s/%s/%s'%(date[2], date[0], date[1])
                    date = '%s-%s-%s'%(date[2], date[0], date[1])
                elif 'PROCESS TIME:' in line:
                    thyme = line.replace('PROCESS TIME:', '').strip()
                    inTime = thyme.replace(':', '')
                    slotFilter = slotDate + ' ' + thyme
                    if slotFilter in waferID:
                        slot = waferID.replace(slotFilter, '').strip()
                        waferID = 'BlankWaferID'
                    else:
                        slot = 'BlankSlot'
                elif 'FILM STACK:' in line:
                    if result != '':
                        header = header+dataHeader+result
                    result=''
                    first=0
                    header += '<HEADER>\n'
                    header += 'ToolArea,Metrology\n'
                    header += 'ToolType,Profiler\n'
                    header += 'Tool,%s\n' %tool
                    header += 'CleanedLotID,%s\n' %cleanedLotID
                    header += 'LotID,%s\n' %lotID
                    header += 'Mask,%s\n' %mask
                    header += 'Level,%s\n' %level
                    header += 'Step,%s\n' %step
                    header += 'CollectionDateTime,%s ' %date + '%s\n' %thyme
                    header += 'User,%s\n' %user
                    header += 'ProcessSpec,%s\n' %spec
                    header += 'WaferID,%s\n' %waferID
                    header += 'Slot,%s\n' %slot
                    header += 'Recipe,%s\n' %cassette
                    header += 'SourceFile,%s\n' %doc
                    header += '<DATA>\n'
                    dataHeader = 'subrecipe,sitename,Site,X,Y'
                    filmstack = line.replace('FILM STACK:', '').strip()
                    l9=''; l8=''; l7=''; l6=''; l5=''; l4=''; l3=''; l2=''; l1=''; substrate=''; resultName=''; resultUnits=''
                elif 'LAYER 9:' in line:
                    l9 = line.replace('LAYER 9:', '').strip()
                elif 'LAYER 8:' in line:
                    l8 = line.replace('LAYER 8:', '').strip()
                elif 'LAYER 7:' in line:
                    l7 = line.replace('LAYER 7:', '').strip()
                elif 'LAYER 6:' in line:
                    l6 = line.replace('LAYER 6:', '').strip()
                elif 'LAYER 5:' in line:
                    l5 = line.replace('LAYER 5:', '').strip()
                elif 'LAYER 4:' in line:
                    l4 = line.replace('LAYER 4:', '').strip()
                elif 'LAYER 3:' in line:
                    l3 = line.replace('LAYER 3:', '').strip()
                elif 'LAYER 2:' in line:
                    l2 = line.replace('LAYER 2:', '').strip()
                elif 'LAYER 1:' in line:
                    l1 = line.replace('LAYER 1:', '').strip()
                elif 'SUBSTRATE:' in line:
                    substrate = line.replace('SUBSTRATE:', '').strip()
                #result data
                elif 'RESULTS:' in line:
                    first+=1
                    resultName = line.replace('RESULTS:', '').strip().replace(' ','')
                    resultUnits = ''
                elif 'UNITS:' in line:
                    resultUnits = line.replace('UNITS:', '').strip().replace(' ', '')
                elif (' %s:'%resultNum) in line:
                    results = line.replace(('%s:'%resultNum), '').strip()
                    results = re.sub('\s+', ',', results).split(',')
                    ##try:
                    if resultName not in dataHeader:
                        dataHeader += ',%s,%s units' %(resultName, resultName)
                    if first == 1:
                        result += '%s,%s,%s,%s,%s,%s,%s'%(recipe, filmstack, resultNum, results[1].strip(), results[2].strip(), results[0].strip(), resultUnits)
                        if l9 != '':
                            if 'layer9Material' not in dataHeader:
                                dataHeader += ',layer9Material'
                            result+=',%s'%l9
                        if l8 != '':
                            if 'layer8Material' not in dataHeader:
                                dataHeader += ',layer8Material'
                            result+=',%s'%l8
                        if l7 != '':
                            if 'layer7Material' not in dataHeader:
                                dataHeader += ',layer7Material'
                            result+=',%s'%l7
                        if l6 != '':
                            if 'layer6Material' not in dataHeader:
                                dataHeader += ',layer6Material'
                            result+=',%s'%l6
                        if l5 != '':
                            if 'layer5Material' not in dataHeader:
                                dataHeader += ',layer5Material'
                            result+=',%s'%l5
                        if l4 != '':
                            if 'layer4Material' not in dataHeader:
                                dataHeader += ',layer4Material'
                            result+=',%s'%l4
                        if l3 != '':
                            if 'layer3Material' not in dataHeader:
                                dataHeader += ',layer3Material'
                            result+=',%s'%l3
                        if l2 != '':
                            if 'layer2Material' not in dataHeader:
                                dataHeader += ',layer2Material'
                            result+=',%s'%l2
                        if l1 != '':
                            if 'layer1Material' not in dataHeader:
                                dataHeader += ',layer1Material'
                            result+=',%s'%l1
                        if substrate != '':
                            if 'substrateMaterial' not in dataHeader:
                                dataHeader += ',substrateMaterial'
                            result+=',%s'%substrate
                    ##NEED TO MAKE RESULT A LIST TO APPEND OTHER DATA
                    elif first > 1:
                        dum = result.split('\n')
                        dum[(resultNum-1)]+=',%s,%s'%(results[0].strip(), resultUnits)
                        result = '\n'.join(dum)
                    ##except Exception as e:
                        ##print(e)
                    results=''
                    resultNum+=1
                    result+='\n'
                elif '---' in line:
                    resultNum=1
                elif ('F5x' in line) or ('KLA' in line):
                    save=1
                elif line.strip() == '00001A':
                    save=1
                    lotID=' '
                    result=''
                    os.remove(dirpath+'\\'+file)
            if (save==1) and (lotID==''):
                result=''
            elif save==0:
                result=''
                shutil.move(dirpath+'\\'+file, dirpath.replace(RAWin, r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\F5x\UNPROCESSED\DEBUG')+'\\'+file)
            elif len(result) > 0:
                fileName = FLATout+'\\'+tool+'-'+mask+'-'+cleanedLotID+'-'+cassette+'-'+recipe.replace('-', '_')+'-'+inDate+'-'+inTime+'-'+strftime('%H%M%S', time.localtime())+'.txt'
                OutputSQLFile(BlackList, mask, lotID, header, dataHeader, result, fileName, tool, file, FLATout, dirpath, RAWin)
                shutil.move(dirpath+'\\'+file, dirpath.replace(RAWin, RAWout)+'\\'+file)
            else:
                print('Issue with file empty %s' %file)
                result=''
                shutil.move(dirpath+'\\'+file, dirpath.replace(RAWin, r'C:\Users\J20032\Documents\PS-PY\myTie\test_code\python_test\RtF_source\F5x\UNPROCESSED\DEBUG')+'\\'+file)
#        except Exception as e:
#            print(e)



F5xFlat()
