# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:10:28 2021

@author: Notebook
"""

import pymysql

koneksi = pymysql.connect(
    host="localhost",
    user="root",
    database="db_py",
    passwd=""
)

mycursor = koneksi.cursor() #cursor created
 
#work with the cursor
query1 = "INSERT INTO students(Name, Lastname, Standard) VALUES('Anik', 'Das', 6);"
query2 = "INSERT INTO students(Name, Lastname, Standard) VALUES('Subhash', 'Neel', 8);"
query3 = "INSERT INTO students(Name, Lastname, Standard) VALUES('Prateek', 'Neel', 8);"
query4 = "INSERT INTO students(Name, Lastname, Standard) VALUES('Prem', 'Dutta', 9);"
 
mycursor.execute(query1)
mycursor.execute(query2)
mycursor.execute(query3)
mycursor.execute(query4)
 
#closing the db
koneksi.commit()
koneksi.close()