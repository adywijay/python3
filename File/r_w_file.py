# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:33:15 2021

@author: User
"""
######################### Open Close Files #########################
print('Before==================================\n\n')
list_file = open('D:/python3/File/DE_result_miss_20200428.txt', 'w+')

print(f'Nama File : {list_file.name}')
print(f'Akses Ditutup : {list_file.closed}')
print(f'Mode Akses : {list_file.mode}')

print('After====================================\n\n')
list_file.close()  # menutup akses baik read maupun write
print(f'Akses Ditutup : {list_file.closed}')
print(f'Mode Akses : {list_file.mode}')


######################### Open Write Files #########################
list_file = open('D:/python3/File/DE_result_miss_20200428.txt', 'w+')
list_file.write('Solusi247 BSO Dancuk')  # menulis kal.kedalam direktory
list_file.close()


######################### Open Read Files #########################
list_file = open('D:/python3/File/oprek.csv', 'r')
out = list_file.read()  # membaca file.kedalam direktory
satu_baris = list_file.readline()

print(out)  # baca seluruh isi file

# print(satu_baris) --> baca satu baris dri isi file
list_file.close()
