# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:41:08 2021

@author: Notebook
"""
import importlib
import contoh as cth
print('fungsi yg dapat dipakai pada modul cth \n\n', dir(cth))
importlib.reload(cth)

coba = cth.GFG()
print(coba.add(2, 2))
print('modul import dari kelas \n\n\n\n')