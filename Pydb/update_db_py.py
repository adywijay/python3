# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:15:33 2021

@author: Notebook
"""
import pymysql

koneksi = pymysql.connect(
    host="localhost",
    user="root",
    database="db_py",
    passwd=""
)

mycursor = koneksi.cursor() #cursor
 
#query to update database data
update_query = "UPDATE students set Lastname = 'Seth' WHERE StudentID = 2"
 
#executing the query
mycursor.execute(update_query)
 
#showing the rows
res = "Select * from students;"
mycursor.execute(res)
rows = mycursor.fetchall()
 
for row in rows:
   print(row)
 
#closing the db
koneksi.commit()
koneksi.close()