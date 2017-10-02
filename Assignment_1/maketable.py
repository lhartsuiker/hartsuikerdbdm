import sqlite3 as lite
import csv
import numpy as np
con = lite.connect('DDM17.db')






with con: 
    # Get a cursor. 
    cur = con.cursor() 
    # Create MagTable
    command = """CREATE TABLE IF NOT EXISTS {0} (Name varchar(10),
    Ra DOUBLE , Dec DOUBLE, B FLOAT, R FLOAT)""".format('MagTable')

    # create the coloumns with their values
    MagTable_Name = ['V0-001','V0-002','V0-003','V0-004']
    Ra = ['12:34:04.2','12:15:00.0','11:55:43.1','11:32:42.1']
    Dec = ['-00:00:23.4','-14:23:15','-02:34:17.2','-00:01:17.3']
    B = [15.4,15.9,17.2,16.5]
    R = [13.5,13.6,16.8,14.3]

    cur.execute(command) 

    # insert values into MagTable
    for i in np.arange(len(MagTable_Name)):
        command="INSERT OR IGNORE INTO MagTable VALUES('{0}','{1}','{2}',{3},{4}) ".format(MagTable_Name[i],Ra[i],Dec[i],B[i],R[i])
        cur.execute(command)

    # Same process for PhysTable
    command = """CREATE TABLE IF NOT EXISTS {0} (Name varchar(10),
    Teff FLOAT, FeH FLOAT)""".format('PhysTable')

    PhysTable_Name = ['V0-001','V0-002','V0-003']
    Teff = [4501,5321,6600] #Kelvin
    FeH = [0.13,-0.53,-0.32]

    cur.execute(command) 

    for i in np.arange(len(PhysTable_Name)):
        command="INSERT OR IGNORE INTO PhysTable VALUES('{0}',{1},{2})".format(PhysTable_Name[i],Teff[i],FeH[i])
        cur.execute(command)


    # a
    print 'exercise a:','\n'
    rows=con.execute('select Name,Ra,Dec from MagTable where B>16')
    for row in rows:
        print(row)

    #b
    print '\n','exercise b:','\n'
    rows=con.execute('select M.Name, B,R,Teff,FeH from MagTable as M join PhysTable as P on M.Name=P.Name')
    for row in rows:
        print(row)

    #c
    print '\n','exercise c:','\n'
    rows=con.execute('select M.Name, B,R,Teff,FeH from MagTable as M join PhysTable as P on M.Name=P.Name where FeH>0')
    for row in rows:
        print(row)

    #d
    print '\n','exercise d:','\n'

    command = """CREATE TABLE IF NOT EXISTS {0} (Name varchar(10),
    br FLOAT)""".format('brTable')
    cur.execute(command)
    rows= con.execute('select Name,B-R as br from MagTable')

    for row in rows:
        command="INSERT OR IGNORE INTO brTable VALUES('{0}',{1})".format(row[0],row[1])
        cur.execute(command)
        print(row)