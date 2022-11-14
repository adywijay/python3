# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:15:40 2021

@author: Notebook
"""

try:
    list_file = open('D:/python3/Exception/tes.txt', 'r+')
    out = list_file.read()
    satu_baris = list_file.readline()
    print(out)

finally:
    list_file.close()


"""
    try
    
            finally
            
digunakan untuk sebuah sub rutin yang memiliki pasangan open & closes / akhiran
dalam block try
"""
