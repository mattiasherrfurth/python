#import contextlib
#import getpass
#import pyodbc
#import sys
#
#login_attempts = 0
#
#while login_attempts < 3:
#    try:
#        user = input("Username: ")
##        if user == "quit":
##            break
#        if getpass.GetPassWarning() or sys.stdin.isatty():
#            print("WARNING: Unsecure password handling")
#            pwd = getpass.getpass()
#        else:
#            pwd = getpass.getpass()
##        conn = pyodbc.connect("DRIVER = {Oracle in OraClient 12Home1};DSN=ORACLE 32BIT ORAD;uid=" + user + ";pwd=" + pwd)
#        conn = pyodbc.connect("DRIVER = Oracle in OraClient 12Home1;SERVER=EIM-DB-AG40.NORTHGRUM.COM;uid=" + user + ";pwd=" + pwd)
#        cursor = conn.cursor()
#        cursor.execute("SELECT * FROM TDWHSUPL FETCH FIRST 5 ROWS ONLY")
#        row = cursor.fetchall()
#        print(row)
#    except Exception as error:
#        print("ERROR", error)
#    else:
#        print("SUCCESS")
#        break
#    
#    login_attempts = login_attempts + 1

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EIM-DB-AG40.NORTHGRUM.COM;'
                      'Database=j20032_yield;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM j20032_yield.dbo.PyramidYieldData')

n = 0

for row in cursor:
    n = n + 1
    print(row)
    if n == 100:
        break