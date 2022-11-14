# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:07:24 2021

@author: Notebook
"""

file_dir = open('D:\python3\File\DE_result_miss_20200428.txt', 'w+')
file_dir.write('Belajar Pemrograman Python Versi 3.10.0 Tahun 2021')
file_dir.close()
# print('Status Akses File :', file_dir.closed)


file_dirs = open('D:\python3\File\DE_result_miss_20200428.txt', 'r+')
print('Posisisi Sebelum  Pointer: ', file_dirs.tell())
out = file_dirs.read(7)
print('Posisisi Setelah  Pointer: ', file_dirs.tell())
file_dirs.write(str(input('Masukkan text sembarang : ')))
file_dir.close()
print('Posisisi Setelah  insert text: ', file_dirs.tell())
print(out)
