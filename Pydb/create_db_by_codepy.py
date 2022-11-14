# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:33:14 2021

@author: Notebook
"""

import pymysql


while True:
    try:
        db = pymysql.connect(
            host="localhost",
            user="root",
            passwd=""
        )
    except ConnectionError:
        print("Koneksi Bermasalah silakan cek service server")
    else:
        print('Koneksi Sukses !!')
        input_nama = input('Masukkan nama database : ')
        
        mycursor = db.cursor()
        script = mycursor.execute(f"CREATE DATABASE {input_nama};\n\n")
        
        if script == True:
            print(f"Database {input_nama} berhasil dibuat \n")
        else:
            print(f"Database {input_nama} ERROR \n")
            
        mycursor.close()
        break