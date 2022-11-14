# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:17:31 2021

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
 
#query to delete database data
delete_query = "DELETE FROM students WHERE Standard > 8"
 
#executing the query
mycursor.execute(delete_query)
 
#showing the rows
res = "Select * from students;"
mycursor.execute(res)
rows = mycursor.fetchall()
 
for row in rows:
   print(row)
 
#closing the db
koneksi.commit()
koneksi.close()