import sqlite3
from sqlite3 import Error

DbaseName     = 'MasterBase.db3'
DBaseDirName  = 'DBase'

def sql_connection(DbaseName,DBaseDirName):
    DbaseFullName = '.\\'+DBaseDirName
    DbaseFullName = DbaseFullName + '\\' + DbaseName
    try:
        con = sqlite3.connect(DbaseFullName)
        return con
    except Error:
        print('! '+Error)

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM EDIdocs')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    return rows

con  = sql_connection(DbaseName,DBaseDirName)
print('con='+str(con))
rows = sql_fetch(con)

print(rows)

con.close()



