# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:10:01 2021

@author: Notebook
"""


import pymysql

# database connection
connection = pymysql.connect(
    host="localhost", user="root", passwd="", database="spkh")
cursor = connection.cursor()

# queries for retrievint all rows
retrive = "Select * from tbl_akses;"

# executing the quires
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
    print(row)


# commiting the connection then closing it.
connection.commit()
connection.close()
