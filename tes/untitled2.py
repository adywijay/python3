# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:27:54 2022

@author: WIN_10_PRO
"""

daftar = [102, 32, 99, 32, 45, 102, 45, 67, 67, 100, 100]

for i in daftar:
    if daftar.count(i) == 1:
        bilangan = daftar.index(i)+1
        print("Maka bilangan yang tidak berpasangan adalah",i , "pada posisi ke-",bilangan)