import pyodbc,  pandas as pd,  sqlalchemy,  pymysql
db_file = 'C:\\Users\\J20032\\Documents\\PYTHON\\zzil-for-python.accdb'
user = 'J20032'
pw = 'Data2020Ware'

#odbc_conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"r"DBQ=%s;UID=%s;PWD=%s;" %(db_file, user, pw))
#odbc_conn_str = (r"mysql+pymysql://J20032:Data2020Ware@SELEBRUORA03/ORAD")
#odbc_conn_str = pymysql.connect(host='SELEBRUORA03',  user='J20032', db='db', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

#odbc_conn_str = (
#    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
#    r"DBQ=%s;UID=%s;PWD=%s;" %(db_file, user, pw)
#    )


#odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' %(db_file)
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %(db_file, user, pw)

conn = pyodbc.connect(odbc_conn_str)
sql="""\
{CALL Query4}"""
curs = conn.execute(sql)
conn.commit()
curs.close()
conn.close()

#curs = conn.cursor()

#with open(r'C:\Users\J20032\Documents\PYTHON\zzil-pull-sql.txt', 'r') as myfile:
#    sql = myfile.read().replace('\n', '')

print(str(sql))
curs.execute(sql)
results = curs.fetchall()
for row in results:
    for cell in row:
        print(cell)

#print(conn)
#print(conn.__class__)

#with open(r'C:\Users\J20032\Documents\PYTHON\zzil-pull-sql.txt', 'r') as myfile:
#    sql = myfile.read().replace('\n', '')
#    
#curs.execute(sql)
#
#for data in curs.fetchall():
#    print(data)

#df = pd.read_sql("SELECT CDAS_TDWHZZIL.ZZIL_ILOT_NO, CDAS_TDWHZZIL.ZZIL_ORDR_RTG_NO FROM CDAS_TDWHZZIL;",  odbc_conn_str)
