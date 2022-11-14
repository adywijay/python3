# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:19:18 2021

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

#query to drop table
drop_query = "DROP TABLE IF EXISTS students;"
 
#executing the query
mycursor.execute(drop_query)