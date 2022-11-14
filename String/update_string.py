# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:00:23 2021

manipulasi string
@author: Notebook
"""


var1 = 'Hello Python!'
var2 = "I love Python"

print("var1[0]", var1[1:10])
print("var2[2:6]:", var2[2:6])
print("\n\n\n")
# ---------------------teknik slice / pemotongan string dasar -----------

print("--------------------+++--------------------------")
kalimat = 'belajar mencintai dia'
print("kalimat asli : ", kalimat)
print("kalimat setelah update : ", kalimat[0:8] + 'pencak silat')


################################ contoh program sederhana ##########################################


print("--------------------+++--------------------------\n\n")


kalimat = "belajar mencintai dia"
print("kalimat dasar :", kalimat)
print('jumlah kalimat tersebut adalah : ', len(kalimat), 'karakter')

start = eval(input('Masukkan nilai awal :\t'))
end = eval(input('Masukkan nilai akhir :\t'))
replace = input('Masukkan kalimat pengganti :\t')


print(str.center('HASIL', 20, '-'))
print("kalimat asli : ", kalimat)
print("kalimat setelah update : ", kalimat[start:end] + replace)
