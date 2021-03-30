## FTTIY CONNECTION ##

import pandas as pd
import pyodbc 
from datetime import datetime as dt
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EIM-DB-AG40.NORTHGRUM.COM;'
                      'Database=j20032_yield;'
                      'Trusted_Connection=yes;')
sql = """
WITH

---------- 
              QnotTbl AS 
                                  (          
                                             SELECT 
                                                        ORDR_PLNT_ID AS "Plant",
                                                        PCLL_CELL_NM AS "Cell",
                                                        PMCD_MCMD_CD AS "Scheduler", 
                                                        PMCD_DESC AS "Scheduler Description",
                                                        WBSE_CD AS "WBS Element",
                                                        WBSE_DESC AS "WBS Description",
                                                        ORDR_PART_NO AS "Part Number",
                                                        PART_DESC AS "Part Description",
                                                        ORDR_SPRT_SER_NO AS "Serial Number",
                                                        ORDR_OCAT_CD AS "Order Type",
                                                        ORDR_NO AS "Order Number",
                                                        ORDR_QTY AS "Order Qty",
                                                        ORDR_OPER_COMPLETED_DT AS "OKFS Date",
                                                        ORDR_TECO_DT AS "TECO Date",
                                                        WCTR_CD AS "Work Center", 
                                                        WCTR_DESC AS "Work Center Description",
                                                        WCCT_DESC AS "Work Center Category",
                                                        OROP_ID AS "Operation",
                                                        OROP_LINE1_DESC AS "Operation Short Text",
                                                        EMPL_LAST_NM AS "Last Name", 
                                                        EMPL_FIRST_NM AS "First Name",
                                                        QNOT_NO AS "QN Number",
                                                        QNOT_QNOT_NO AS "Parent QN",
                                                        QNOT_TYP AS "QN Type",
                                                        QNDF_NO AS "QN Item Number",
                                                        QNDF_DESC AS "QN Item Short Text",
                                                        NOTE_TXT AS "QN Item Long Text",
                                                        QNDF_CREATED_DT AS "QN Item Created Date",
                                                        QNDF_DEFECT_CNT AS "QN Item Qty",
                                                        DCAT_NM AS "Defect Code Group",
                                                        QNCT_TIER3_DESC AS "Defect Code",
                                                        QNDF_COMP_PART_NO AS "Removed Component", 
                                                        QNDF_SPRT_SER_NO AS "Removed Serial Number",
                                                        QNTK_QNCT_TIER3_CD AS "Disposition",
                                                        QNTK_TXT AS "Disposition Text",
                                                        "Rework Hours"

                                             FROM TDWHQNDF
                                                                             INNER JOIN TDWHQNOT
                                                                                                  ON QNOT_NO = QNDF_QNOT_NO
                                                                             INNER JOIN (SELECT * FROM TDWHORDR WHERE ORDR_OCAT_CD = 'ZP11')
                                                                                                  ON (ORDR_NO = QNOT_ORDR_NO AND ORDR_PLNT_ID = QNOT_PLNT_ID)
                                                                             INNER JOIN TDWHPMCD
                                                                                                 ON PMCD_MCMD_CD = ORDR_MCMD_CD AND PMCD_PLNT_ID = ORDR_PLNT_ID
                                                                             INNER JOIN TDWHPCLL
                                                                                                  ON PCLL_CD = PMCD_PCLL_CD AND PCLL_PLNT_ID = PMCD_PLNT_ID
                                                                             INNER JOIN TDWHWBSE
                                                                                                  ON WBSE_ID = ORDR_WBSE_ID
                                                                             INNER JOIN TDWHPART
                                                                                                  ON PART_NO = ORDR_PART_NO
                                                                             INNER JOIN VDWHEMPL
                                                                                                  ON EMPL_ID = QNDF_CREATED_EMPL_ID
                                                                             INNER JOIN TDWHWCTR
                                                                                                  ON WCTR_NO = QNOT_WCTR_NO
                                                                             INNER JOIN TDWHOROP
                                                                                                  ON OROP_NO = QNOT_OROP_NO AND OROP_ORDR_RTG_NO = QNOT_ORDR_RTG_NO
                                                                             INNER JOIN TDWHWCCT
                                                                                                  ON WCCT_ID = WCTR_WCCT_ID
                                                                             INNER JOIN (SELECT * FROM TDWHQNCT)
                                                                                                  ON (
                                                                                                         QNCT_TIER1_CD = QNDF_TYPE_QNCT_TIER1_CD AND 
                                                                                                         QNCT_TIER2_CD = QNDF_TYPE_QNCT_TIER2_CD AND 
                                                                                                         QNCT_TIER3_CD = QNDF_TYPE_QNCT_TIER3_CD
                                                                                                          )
                                                                             INNER JOIN TDWHDCAT
                                                                                                  ON QNCT_DCAT_CD = DCAT_CD
                                                                             LEFT JOIN (SELECT * FROM TDWHNOTE WHERE NOTE_NCAT_TABLE_CD='QNDF')
                                                                                                  ON (NOTE_QNOT_NO = QNOT_NO AND NOTE_QNDF_NO = QNDF_NO)
                                                                             INNER JOIN (SELECT * FROM TDWHQNTK WHERE QNTK_QNCT_TIER2_CD='PRDISP')
                                                                                                  ON QNTK_QNDF_QNOT_NO = QNOT_NO AND QNTK_QNDF_NO = QNDF_NO
                                                                             LEFT JOIN (SELECT QNDT_QNOT_NO, QNDT_QNDF_NO, Sum(QNDT_ACTUAL_HRS) AS "Rework Hours" FROM TDWHQNDT GROUP BY QNDT_QNOT_NO, QNDT_QNDF_NO)
                                                                                                  ON QNDT_QNOT_NO = QNOT_NO AND QNDT_QNDF_NO = QNDF_NO

                                             WHERE QNDF_CREATED_DT>=TO_DATE('06/29/2018','MM/DD/YYYY') AND PCLL_CD = '10004'
                                   )

SELECT *
FROM QnotTbl

            """
df = pd.read_sql(sql,cnxn)

