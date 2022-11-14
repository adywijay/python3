# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:13:12 2021

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
 
#work with the cursor
perintah = "Select * from students;"
 
#executing the query
mycursor.execute(perintah)
 
rows = mycursor.fetchall()
 
#showing the rows
for row in rows:
   print(row)
 
#closing the db
koneksi.commit()
koneksi.close()