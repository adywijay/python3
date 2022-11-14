# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:37:30 2021

    mendefinisikan code cek koneksi mysql dengan python code

@author: Notebook
"""
import pymysql


while True:
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd=""
        )
    except ConnectionError:
        print("Koneksi Bermasalah silakan cek service server")
    else:
        print('Koneksi Sukses !!')
        mydb.close()
        break
