# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:33:28 2021

        Operator String

@author: Notebook
"""

kalimat_1 = "Belajar"
kalimat_2 = "Python"

# OPERATOR OPERASI STRING

a = kalimat_1 + kalimat_2
b = kalimat_1 * 5  # atau kalimat_2 * 2
c = kalimat_1[4]
d = kalimat_1[1:4]
e = 'x' in kalimat_2
f = 'y' not in kalimat_2
g = 'Zara', 21

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("My name is %s and weight is %d kg!" % g)  # operator %
