# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:43:12 2021

@author: Notebook
"""
import copy

print("####### Before #############")
a = [2, 1, 3, 5, 4]
print('Isi list var A         : ', a)
print('Id Memory var A adalah : ', id(a))
print(" \n\n\n\n")

print("========= After ============= \n\n")
while True:
    try:
        b = copy.deepcopy(a)
        urut = sorted(b)
        print('Isi list var B : ', b)
        print('Isi list sorted B : ', urut)
        print('Id Memory var B adalah : ', id(b))
        break
    except ValueError:
        print("Oops!  Inputan tidak valid.  silakan coba lagi...")
