# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:01:29 2021

@author: Notebook
"""

import pymysql

koneksi = pymysql.connect(
    host="localhost",
    user="root",
    database="db_py",
    passwd=""
)

panggil = koneksi.cursor() #cursor created
 
#work with the cursor
perintah = "CREATE TABLE Students(StudentID int  PRIMARY KEY AUTO_INCREMENT, Name CHAR(20), Lastname CHAR(20),Standard int);"
 
panggil.execute(perintah)
panggil.close()