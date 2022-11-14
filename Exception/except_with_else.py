# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:55:39 2021

@author: Notebook
"""

while True:
    try:
        x = int(input("Masukkan angka: "))
        # break
    except ValueError:
        print("Oops!  Inputan tidak valid.  silakan coba lagi...")
    else:
        print('Inputan sudah valid')
        break
"""
Kode diatas akan berhenti jika inputan benar yaitu nomr bukan string
"""
