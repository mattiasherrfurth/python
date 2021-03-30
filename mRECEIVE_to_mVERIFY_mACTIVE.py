from pywinauto import Application
import pywinauto
import time
import psutil 
import pypyodbc 
import pymysql
print('Loaded.')
#find all reticles in factory works at the mRECEIVE step
conn1 = pypyodbc.connect("""Driver={Oracle in OraClient11g_home1}; 
            DBQ=ORAF;
            Uid="FWREAD";
            Pwd="FWREAD";
            """)
cursor1 = conn1.cursor() 
cursor1.execute("""SELECT FWLOT.APPID
FROM ATLWIP.FWWIPSTEP
INNER JOIN ATLWIP.FWLOT_N2M 
ON FWWIPSTEP.SYSID=FWLOT_N2M.TOID
INNER JOIN ATLWIP.FWLOT
ON FWLOT_N2M.FROMID=FWLOT.SYSID
WHERE STEPNAME LIKE 'mRECEIVE_MASK'
AND FWLOT.PROCESSINGSTATUS  LIKE 'Active';""" )
cursor1.commit()
myReticles = cursor1.fetchall() 
cursor1.close() 
conn1.close() 
mymACTIVE = []
mymVERIFY = []
#Function to check if each reticle at mRECIEVE_MASK has been used on one of the ASML steppers and how many unique runs. 
def getusage(i,stepper):
    conn2 = pymysql.connect(
            host="atldev1",user="metrouser",
            passwd="readonly",db="metrodbwill",
            cursorclass = pymysql.cursors.SSCursor)
    cursor2 = conn2.cursor() 
    cursor2.execute("""SELECT `batch_finished`
    FROM `metrodbwill`.%s
    WHERE `Reticle` LIKE '%s';""" %(stepper,i[0].split(" ")[0]))
    myMaskUse = cursor2.fetchall()
    cursor2.close() 
    conn2.close() 
    if myMaskUse != []:
        mydates.append(myMaskUse)
mACTIVE = "001300"
mVERIFY = "001200"
def FWBlaster(step, mylist):
    z=pywinauto.controls.win32_controls.ComboBoxWrapper(app.FACTORYworksIntelligentClient.ComboBox)
    z.Select('aMASK_ACTIVE')
    app.Dialog.YESbutton.click()
    #wait for Factory Works to load dispatch area
    time.sleep(30)
    #Select step for each reticle that is at mRECEIVE step, yet has been used on the steppers. 
    for i in range(len(mylist)):
        #wait for factory works to catch up
        time.sleep(5)
        #select the dispatch area
        thunderrtformdc = app.FACTORYworksIntelligentClient
        listviewwndclass = thunderrtformdc[u'7']
        #Factory Works is smart enough to know characters produced by "type_keys" are not coming from the keyboard and therefore doesn't invoke the yellow lot search box when the program starts typing. 
        #To trick Factory Works into thinking the characters are coming from the keyboard, send Factory works an "Insert" or "Space" bar followed by the desired characters to enter. Type_keys also does not send spaces in your string.
        #for spaces you must replace the empty space between words with "{SPACE}". 
        listviewwndclass.type_keys('{INSERT}{BACK}%s'%(mylist[i].replace(" ","{SPACE}")))
        time.sleep(5)
        app.FACTORYworksIntelligentClient.menu_select("Activities->ClientRules")
        #Factory Works was having issues with calling a menu within a menu within a menu. Instead, I went two menu levels down and then used the quick keys features by sending Factory Works the first letter of the desired menu option and 
        #hitting enter instead of trying to select the menu item by name. Hence "s{ENTER}".
        app.FACTORYworksIntelligentClient.type_keys("s{ENTER}")
        time.sleep(2)
        #type step number
        app.Dialog.Edit.type_keys(step)
        app.Dialog.OKbutton.click()
        while True:
            try:
                app.Dialog.Yes.click()
            except:
                continue
            break
        z2=pywinauto.controls.common_controls.ListViewWrapper(app.Dialog.Pane6)
        z2.Click()
#determine by usage which reticles need to go to mACTIVE or mVERIFY
if myReticles != []:
    for i in myReticles:
        mydates = []
        getusage(i,"`duv-4035`")
        getusage(i,"`duv-7128`")
        getusage(i,"`iln-6496`")
        bearcat = [item for sublist in mydates for item in sublist]
        kittycub = [str(i).split("_")[0] for i in bearcat]
        if kittycub != []:
            #to mACTIVE
            if len(set(kittycub))>1:
                mymACTIVE.append(i[0])
            #to mVERIFY
            if len(set(kittycub)) == 1:
                mymVERIFY.append(i[0])
    print("Lists Made")
    if mymACTIVE != []:
        print("New mACTIVE Reticles:%s"%(mymACTIVE))
    else:
        print("No new active reticles")
    if mymVERIFY != []:
        print("New mVERIFY Reticles:%s"%(mymVERIFY))
    else:
        print("No new reticles at verification")
if mymACTIVE != [] or mymVERIFY != []:
    #check to see if Factory Works is open
    pythons_psutil = []
    for p in psutil.process_iter():
        try:
            if p.name() == "FwCliLoader_SA.exe":
                pythons_psutil.append(p)
        except psutil.Error:
            pass
    if not pythons_psutil:
        #If Factory Works is not open, then open FW and log in
        Application().start(r"S:\ADVTECH\TrackingFWUser\FW Client OUTSIDE Lab\FwCliLoader_SA.exe", timeout = 30)
        time.sleep(30)
        app = Application(backend="uia").connect(path="FwCliLoader_SA.exe", title="FACTORYworks Intelligent Client")
        app.FACTORYworksIntelligentClient.menu_select("File->Login")
        app.Dialog.Edit2.type_keys("J30052")
        app.Dialog.Edit1.type_keys("qwER12#$")
        app.Dialog.OKbutton.click()
        #If Factory Works IS open, connect to the open application
    else:
        app = Application(backend="uia").connect(path="FwCliLoader_SA.exe", title="FACTORYworks Intelligent Client")
    FWBlaster(mACTIVE, mymACTIVE)
    FWBlaster(mVERIFY, mymVERIFY)
print("Your dirty deed is done.")














            






         




