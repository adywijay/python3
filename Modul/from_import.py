# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:06:48 2021

    syntax umumnya adalah sbg berikut :
       From NamaModul import NamaFungsi1,  NamaFungsi2...
@author: Notebook
"""

from ucapan import greeting
greeting('ASUUUUUUUUUUU')
print('modul import from biasa \n\n\n\n')


import contoh
coba = contoh.GFG()
print(coba.add(2, 2))
print('modul import dari kelas \n\n\n\n')


from contoh import method
method()
print('modul import method dari kelas \n\n\n\n')