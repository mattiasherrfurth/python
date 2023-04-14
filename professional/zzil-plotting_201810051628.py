import pandas as pd,  math,  seaborn as sns,  datetime
import matplotlib.pyplot as plt
import numpy as np

#tabol = input("Where is your CSV file? ")
#while os.path.exists(tabol) == False and tabol != 0:
#    tabol = input("Please enter a real filepath, or enter 0 to kill me...")
#tabal = pd.read_csv(tabol)

##listing part numbers
jsf_pn = ['261K775G03', '261K775G04']
sabr_pn = ['255K250G07']
gator_pn = ['282K097G05', '282K097G06', '282K097G05']
triton_pn = ['267K400G03']
all_pn = jsf_pn + sabr_pn + gator_pn + triton_pn
criteria = ['A', 'R']

##ms access query sorts for the following:
##      ZZIL_PART_NO = the part numbers in 'all_pn'
##      ZZIL_ILOR_QTY = 1
##      ZZIL_ILOR_END_DT >= Date() - 30
##      ZZIL_PELE_DESC = "InProcess Sample Inspection (Insp scrn)"
##      ZZIL_PLNT_ID = "P001"
##      ZZIL_ILOR_VALIDITY_CD = "VALID"
##      ZZIL_ILOR_ELEM_QNCT_TIER3_CD = 'A' or 'R'
tabal = pd.read_excel(open(r'C:\Users\J20032\Documents\PYTHON\p-charts\ZZIL_query_201810051024.xlsx', 'rb'))

##pulling unique dates
def getdates(table):
    dates = pd.to_datetime(table.ZZIL_ILOR_END_DT.unique()).sort_values()
    return dates
def lcl(CL, Y,  Q):
    return CL - 3*math.sqrt(Y*((1-Y)/Q))
def ucl(CL, Y,  Q):
    return CL + 3*math.sqrt(Y*((1-Y)/Q))

#input("Which part do you want to plot for?")

def jsfplot(table):
    jsf_tbl = table[(table['ZZIL_PART_NO'].isin(jsf_pn)) & (table['ZZIL_OROP_ID']==4500) & (table['ZZIL_WCTR_CD']=='MYVAHVL')]
    col = ['Date', 'QuantityInspected', 'QuantityAccepted','Yield', 'CenterLine', 'LCL', 'UCL', 'DayNumber']
    yld = []
    yld.append(col)
    x=1
    dates = getdates(jsf_tbl)
    #    ##parsing through table, where x is the index for the rows
    while x < len(dates):
        y=0
        yld.append([])
        ##parsing through row, where y is the index for column values
        while y < len(col)+1:
            ##append date to row
            if y == 0:
                yld[x].append(dates[x])
            ##append quantity inspected to row
            elif y == 1:
                yld[x].append(len(jsf_tbl[(jsf_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (jsf_tbl.ZZIL_PART_NO.isin(jsf_pn))]))
            ##append quantity accepted to row
            elif y == 2:
                yld[x].append(len(jsf_tbl[(jsf_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (jsf_tbl.ZZIL_PART_NO.isin(jsf_pn)) & (jsf_tbl.ZZIL_ILOR_ELEM_QNCT_TIER3_CD == 'A')]))
            ##append yield to row
            elif y == 3:
                yld[x].append(yld[x][2]/yld[x][1])
            ##append center line to row
            elif y == 4:
                yld[x].append(0.95)
            ##append lower control limit to row
            elif y == 5:
                prop = yld[x][3]
                cent = yld[x][4]
                qty = yld[x][1]
                yld[x].append(lcl(cent, prop,  qty))
            ##append upper control limit to row
            elif y==6:
                prop = yld[x][3]
                cent = yld[x][4]
                qty = yld[x][1]
                if ucl(cent, prop,  qty) >= 1:
                    yld[x].append(1)
                else:
                    yld[x].append(ucl(cent, prop,  qty))
            ##append date number to row
            elif y==7:
                w = dates[x]-dates[0]
                yld[x].append(int(str(w).split(' ')[0]))
            y+=1
        x+=1
    pchart = pd.DataFrame(yld,  columns = col, dtype=float)
    vx
#    print(jsf_tbl.shape)

jsfplot(tabal)












#############MIGHT NOT NEED THIS CODE, SEABORN AGGREGATES ROWS WITH CONDITIONS WHEN PLOTTING#############
########################################
#    ##parsing through table, where x is the index for the rows
##    while x < len(dates):
##        y=0
##        yld.append([])
##        ##parsing through row, where y is the index for column values
##        while y < len(col)+1:
##            ##append date to row
##            if y == 0:
##                yld[x].append(dates[x])
###                yld[x].append(str(dates[x]).split(' ')[0])
##            ##append quantity inspected to row
##            elif y == 1:
##                yld[x].append(len(jsf_tbl[(jsf_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (jsf_tbl.ZZIL_PART_NO.isin(jsf_pn))]))
##            ##append quantity accepted to row
##            elif y == 2:
##                yld[x].append(len(jsf_tbl[(jsf_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (jsf_tbl.ZZIL_PART_NO.isin(jsf_pn)) & (jsf_tbl.ZZIL_ILOR_ELEM_QNCT_TIER3_CD == 'A')]))
##            ##append yield to row
##            elif y == 3:
##                yld[x].append(yld[x][2]/yld[x][1])
##            ##append center line to row
##            elif y == 4:
##                yld[x].append(0.95)
##            ##append lower control limit to row
##            elif y == 5:
##                prop = yld[x][3]
##                cent = yld[x][4]
##                qty = yld[x][1]
##                yld[x].append(lcl(cent, prop,  qty))
##            ##append upper control limit to row
##            elif y==6:
##                prop = yld[x][3]
##                cent = yld[x][4]
##                qty = yld[x][1]
##                if ucl(cent, prop,  qty) >= 1:
##                    yld[x].append(1)
##                else:
##                    yld[x].append(ucl(cent, prop,  qty))
##            ##append date number to row
##            elif y==7:
##                w = dates[x]-dates[0]
##                yld[x].append(int(str(w).split(' ')[0]))
##            y+=1
##        x+=1
#############################################
#
#    pchart = pd.DataFrame(yld,  columns = col, dtype=float)
#
#
#
##    xdates = []
##    yield_line = []
##    ucl_line = []
##    lcl_line = []
##    center = []
##    for h in yld[1:]:
##        if h[1] >=3:
##            print(h)
##            xdates.append(h[0])
##            yield_line.append(h[3])
##            ucl_line.append(h[6])
##            lcl_line.append(h[5])
##            center.append(h[4])
##        else:
##            pass
##    hg
##    plt.plot(xdates, yield_line)
##    plt.plot(xdates, lcl_line)
##    plt.show()
#
##    print(len(yld))
##    print(len(yield_line))
##    sns.set_style("darkgrid")
##    plt.plot(np.cumsum(yield_line))
##    plt.show()
#    
##    pchart = pd.DataFrame(yld,  columns = col, dtype=float)
##    for x in jsf_tbl:
##        for y in x:
##            print(y)
#
#
#
#
#
#
#
###can loop through dates
##for x in dates:
##    print(x)
##    print('break')
#
###filter after access querying
##jsf_tbl = tabel[(tabel['ZZIL_PART_NO'].isin(jsf_pn)) & (tabel['ZZIL_OROP_ID']==4500) & (tabel['ZZIL_WCTR_CD']=='MYVAHVL')]
#
##print(jsf_tbl)
