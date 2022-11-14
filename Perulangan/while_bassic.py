# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:03:21 2021

@author: Notebook
"""
"""
mulai = eval(input("Masukkanawal : "))
batas = eval(input("Masukkan Batas Perulangan : "))

i = mulai
while i <= batas:
   print(i)
   i+=mulai
   
"""
print("==============Nested while loops===========\n")

count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
# print ("Good bye!")


i = 1
while i <= 10:
    j = 1
    while j <= i:
        print(" %s " % (i*j), end='')
        j += 1
    print()
    i += 1

i = 1
while i <= 10:
    j = 1
    while j <= i:
        print(" %s " % (i*j), end='')
        j += 1
        if i % 2 == 0:
            break
    print()
    i += 1
