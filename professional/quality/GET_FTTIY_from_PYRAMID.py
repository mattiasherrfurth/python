# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:35:27 2018

@author: mattias
"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import math

df = pd.read_excel(r'C:\path\to\excel\file.xlsx')
#df = pd.read_excel(r'C:\Users\J20032\FTTIY_INPUT.xlsx')

jsf_eval = {'prog':'JSF',"Part Number":['261K775G03 - TWIN TRANSMIT / RECEIVE ASSEMBLY','261K775G04 - TWIN TRANSMIT / RECEIVE ASSEMBLY'],"WCTR_CD":['MYVAHVL'],"Oper":4500,"Result":'ACCEPTED','CL':0.955}

sabr_eval = {'prog':'SABR',"Part Number":['255K250G07 - ECA, QUAD T/R MODULE','255K250G08 - ECA, QUAD T/R MODULE'],"WCTR_CD":['MYVAHVL'],"Oper":4500,"Result":'ACCEPTED','CL':0.955}

gator_eval = {'prog':'GATOR',"Part Number":['282K097G05 - ELECTRONIC CIRCUIT ASSEMBLY, TRANSMIT/RE','282K097G06 - ELECTRONIC CIRCUIT ASSEMBLY, TRANSMIT/RE','282K097G07 - ELECTRONIC CIRCUIT ASSEMBLY, TRANSMIT/RE'],"WCTR_CD":['MYVA02','MYVA04'],"Oper":3300,"Result":'ACCEPTED','CL':0.835}

triton_eval = {'prog':'TRITON',"Part Number":['267K400G03 - TWIN TRANSMIT / RECEIVE ASSEMBLY'],"WCTR_CD":['MYVAHVL'],"Oper":4500,"Result":'ACCEPTED','CL':0.98}

all_eval = [jsf_eval,sabr_eval,gator_eval,triton_eval]
all_yields = []
n = 1
plt.style.use('seaborn-whitegrid')

def pchart_get(df,dic):
    date_init = df.Date.min()
    date_end = df.Date.max()
    totyld = []
    col = ["Date","Program","Inspected","Accepted","Yield","CenterLine","UCL","LCL","OOC"]
    cl = dic['CL']
    d = date_init
    progyld = []
    n = 0
    while d < date_end:
        inspect = df[(df['Date'] == d) & (df['Part Number'].isin(dic['Part Number'])) & (df['WCTR_CD'].isin(dic['WCTR_CD'])) & (df['Oper'] == dic['Oper'])].shape[0]
        accept = df[(df['Date'] == d) & (df['Part Number'].isin(dic['Part Number'])) & (df['WCTR_CD'].isin(dic['WCTR_CD'])) & (df['Oper'] == dic['Oper']) & (df['Result'] == dic['Result'])].shape[0]
        if inspect == 0 or inspect == 1:
            pass
        else:
            yld = accept/inspect
            ucl = min([cl+3*math.sqrt((cl*(1-cl))/inspect),1.0])
            lcl = max([cl-3*math.sqrt((cl*(1-cl))/inspect),0.0])
            if yld < lcl or yld > ucl:
                grp = 'o'
            else:
                grp = ''
            ## ADD HANDLING FOR OTHER OOC POINT CRITERIA (n points decreasing, oscillating, etc.)
#            if yld < progyld[n]:
#                grp = 'o'
#            else:
#                grp = ''
            progyld.append([str(d).split(' ')[0],dic['prog'],inspect,accept,yld,cl,ucl,lcl,grp])
        d += datetime.timedelta(days=1)
        n+=1
    totyld.append(progyld)
    progyldpd = pd.DataFrame(data=progyld,columns=col)
    return(progyldpd)

def allyield_get(all_eval):
    for x in all_eval:
        writer = pd.ExcelWriter(os.getcwd()+r'\OUT\%s_test_%s.xlsx'%(x['prog'],datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        pgm_yld = pchart_get(df,x)
        all_yields.append(pgm_yld)
        plt.figure(figsize=(10, 4), dpi=80, facecolor='w', edgecolor='k')
        yld = sns.lineplot(x="Date",y="Yield",data=pgm_yld,color='navy')
        ucl = sns.lineplot(x="Date",y="UCL",data=pgm_yld,color='firebrick')
        lcl = sns.lineplot(x="Date",y="LCL",data=pgm_yld,color='firebrick')
        cl = sns.lineplot(x="Date",y="CenterLine",dashes=True,palette='Blues_r',data=pgm_yld,color='goldenrod')
        plt.xticks(rotation=90)
        plt.ylim(min([pgm_yld['LCL'].min(),pgm_yld['Yield'].min(),0.5]),1.0)
        plt.ylabel('Proportion')
        plt.title('P-chart for %s'%x['prog'])
        for line in range(0,pgm_yld.shape[0]):
            yld.text(pgm_yld['Date'][line], pgm_yld['Yield'][line], pgm_yld['OOC'][line], horizontalalignment='center',verticalalignment='center', size='large', color='red', weight='semibold')
        plt.show()
        pgm_yld.to_excel(writer,'%s'%x['prog'])
        writer.save()

allyield_get(all_eval)
