# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:42:16 2021

@author: Notebook
"""


while True:
    try:
        x = int(input("Masukkan angka: "))
        break
    except ValueError:
        print("Oops!  Inputan tidak valid.  silakan coba lagi...")

"""
Kode diatas akan berhenti jika inputan benar yaitu nomr bukan string
"""
