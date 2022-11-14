# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:55:17 2021

@author: Notebook
"""


class Mobil:

    def __init__(self):
       print('Objeck berhasil dibuat')

    def __del__(self):  # ---------------> Destruktor
        print('Objeck berhasil dihapus')


# def CalldstruckAut():
#     test = Mobil()


# CalldstruckAut()


cek = Mobil()
print(cek)