import contextlib
import getpass
import pyodbc
import sys

login_attempts = 0

while login_attempts < 3:
    try:
        user = input("Username: ")
        if getpass.GetPassWarning() or sys.stdin.isatty():
            print("WARNING: Unsecure password handling")
            pwd = getpass.getpass()
        else:
            pwd = getpass.getpass()
        conn = pyodbc.connect("DSN=ORACLE 64BIT ORAD;uid=" + user + ";pwd=" + pwd)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM TDWHSUPL FETCH FIRST 5 ROWS ONLY")
        row = cursor.fetchall()
        print(row)
    except Exception as error:
        print("ERROR", error)
    else:
        print("SUCCESS")
        break
    
    login_attempts = login_attempts + 1