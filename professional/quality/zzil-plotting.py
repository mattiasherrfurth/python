import pandas as pd,  math,  seaborn as sns,  datetime
import matplotlib.pyplot as plt

##pulling unique dates
def getdates(table):
    dates = pd.to_datetime(table.ZZIL_ILOR_END_DT.unique()).sort_values()
    return dates
def lcl(CL, Y,  Q):
    return CL - 3*math.sqrt(Y*((1-Y)/Q))
def ucl(CL, Y,  Q):
    return CL + 3*math.sqrt(Y*((1-Y)/Q))

def jsfplot(table):
    jsf_tbl = table[(table['ZZIL_PART_NO'].isin(jsf_pn)) & (table['ZZIL_OROP_ID']==4500) & (table['ZZIL_WCTR_CD']=='MYVAHVL')]
    col = ['Date', 'QuantityInspected', 'QuantityAccepted','Yield', 'CenterLine', 'UCL', 'LCL','DayNumber']
    yld = []
    yld.append(col)
    x=1
    dates = getdates(jsf_tbl)
    ###parsing through table, where x is the index for the rows
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
                yld[x].append(0.955)
            ##append upper control limit to row
            elif y == 5:
                prop = yld[x][4]
                cent = prop
                qty = yld[x][1]
                if ucl(cent, prop,  qty) >= 1:
                    yld[x].append(1)
                else:
                    yld[x].append(ucl(cent, prop,  qty))
            ##append lower control limit to row
            elif y==6:
                prop = yld[x][4]
                cent = prop
                qty = yld[x][1]
                yld[x].append(lcl(cent, prop,  qty))
            ##append date number to row
            elif y==7:
                w = dates[x]-dates[0]
                yld[x].append(int(str(w).split(' ')[0]))
            y+=1
        x+=1
    pchart = pd.DataFrame(yld[1:],  columns = col, dtype=float)
    pchart = pchart[(pchart.QuantityInspected > 2)]
    jsf_tbl.to_csv(r'C:\path\to\csv\file1.csv')
    pchart.to_csv(r'C:\path\to\csv\file2.csv')
    sns.set_style("darkgrid")
    sns.lineplot(x='Date',y='Yield', data=pchart, markers=True)
    sns.lineplot(x='Date',y='LCL', data=pchart, color='red')
    sns.lineplot(x='Date',y='UCL', data=pchart, color='red')
    sns.lineplot(x='Date',y='CenterLine', data=pchart, color='green')
    plt.show()
    
def sabrplot(table):
    sabr_tbl = table[(table['ZZIL_PART_NO'].isin(sabr_pn)) & (table['ZZIL_OROP_ID']==4500) & (table['ZZIL_WCTR_CD']=='MYVAHVL')]
    col = ['Date', 'QuantityInspected', 'QuantityAccepted','Yield', 'CenterLine', 'UCL', 'LCL','DayNumber']
    yld = []
    yld.append(col)
    x=1
    dates = getdates(sabr_tbl)
    ###parsing through table, where x is the index for the rows
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
                yld[x].append(len(sabr_tbl[(sabr_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (sabr_tbl.ZZIL_PART_NO.isin(sabr_pn))]))
            ##append quantity accepted to row
            elif y == 2:
                yld[x].append(len(sabr_tbl[(sabr_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (sabr_tbl.ZZIL_PART_NO.isin(sabr_pn)) & (sabr_tbl.ZZIL_ILOR_ELEM_QNCT_TIER3_CD == 'A')]))
            ##append yield to row
            elif y == 3:
                yld[x].append(yld[x][2]/yld[x][1])
            ##append center line to row
            elif y == 4:
                yld[x].append(0.956)
            ##append upper control limit to row
            elif y == 5:
                prop = yld[x][4]
                cent = prop
                qty = yld[x][1]
                if ucl(cent, prop,  qty) >= 1:
                    yld[x].append(1)
                else:
                    yld[x].append(ucl(cent, prop,  qty))
            ##append lower control limit to row
            elif y==6:
                prop = yld[x][4]
                cent = prop
                qty = yld[x][1]
                yld[x].append(lcl(cent, prop,  qty))
            ##append date number to row
            elif y==7:
                w = dates[x]-dates[0]
                yld[x].append(int(str(w).split(' ')[0]))
            y+=1
        x+=1
    pchart = pd.DataFrame(yld[1:],  columns = col, dtype=float)
    pchart = pchart[(pchart.QuantityInspected > 2)]
    pchart.to_csv(r'C:\path\to\csv\file3.csv')
    sns.set_style("darkgrid")
    sns.lineplot(x='Date',y='Yield', data=pchart, markers=True)
    sns.lineplot(x='Date',y='LCL', data=pchart, color='red')
    sns.lineplot(x='Date',y='UCL', data=pchart, color='red')
    sns.lineplot(x='Date',y='CenterLine', data=pchart, color='green')
    plt.show()    
    
def gatorplot(table):
    gator_tbl = table[(table['ZZIL_PART_NO'].isin(gator_pn)) & (table['ZZIL_OROP_ID']==3300) & (table['ZZIL_WCTR_CD']=='MYVA02')]
    col = ['Date', 'QuantityInspected', 'QuantityAccepted','Yield', 'CenterLine', 'UCL', 'LCL','DayNumber']
    yld = []
    yld.append(col)
    x=1
    dates = getdates(gator_tbl)
    ###parsing through table, where x is the index for the rows
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
                yld[x].append(len(gator_tbl[(gator_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (gator_tbl.ZZIL_PART_NO.isin(gator_pn))]))
            ##append quantity accepted to row
            elif y == 2:
                yld[x].append(len(gator_tbl[(gator_tbl.ZZIL_ILOR_END_DT == str(dates[x]).split(' ')[0]) & (gator_tbl.ZZIL_PART_NO.isin(gator_pn)) & (gator_tbl.ZZIL_ILOR_EVALUATION_CD == 'ACCEPTED')]))
            ##append yield to row
            elif y == 3:
                yld[x].append(yld[x][2]/yld[x][1])
            ##append center line to row
            elif y == 4:
                yld[x].append(0.955)
            ##append upper control limit to row
            elif y == 5:
                prop = yld[x][4]
                cent = prop
                qty = yld[x][1]
                if ucl(cent, prop,  qty) >= 1:
                    yld[x].append(1)
                else:
                    yld[x].append(ucl(cent, prop,  qty))
            ##append lower control limit to row
            elif y==6:
                prop = yld[x][4]
                cent = prop
                qty = yld[x][1]
                yld[x].append(lcl(cent, prop,  qty))
            ##append date number to row
            elif y==7:
                w = dates[x]-dates[0]
                yld[x].append(int(str(w).split(' ')[0]))
            y+=1
        x+=1
    pchart = pd.DataFrame(yld[1:],  columns = col, dtype=float)
    pchart = pchart[(pchart.QuantityInspected > 2)]
    pchart.to_csv(r'C:\path\to\csv\file4.csv')
    sns.set_style("darkgrid")
    sns.lineplot(x='Date',y='Yield', data=pchart, markers=True)
    sns.lineplot(x='Date',y='LCL', data=pchart, color='red')
    sns.lineplot(x='Date',y='UCL', data=pchart, color='red')
    sns.lineplot(x='Date',y='CenterLine', data=pchart, color='green')
    plt.show()

##listing part numbers
jsf_pn = ['261K775G03', '261K775G04']
sabr_pn = ['255K250G07']
gator_pn = ['282K097G05', '282K097G06', '282K097G05']
triton_pn = ['267K400G03']
all_pn = jsf_pn + sabr_pn + gator_pn + triton_pn
criteria = ['A', 'R']

#tabal = pd.read_excel(open(r'C:\Users\J20032\Documents\PYTHON\p-charts\AMEC-30days-UNFILTERED_201810081911.xlsx', 'rb'))
tabal = pd.read_excel(open(r'C:\path\to\excel\file5.xlsx', 'rb'))
#jsfplot(tabal)
sabrplot(tabal)
gatorplot(tabal)
