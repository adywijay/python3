# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:45:16 2021

@author: Notebook

statement assert digunakan untuk melakukan pengecekan suatu blok kode
bernilai boolean (T or F)

"""


def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(5))


a = float(input('Masukkan bilangan positif : '))
if a <= 0:
    raise AssertionError('Nilai harus lebih besar dari 0')
else:
    print('Inputan sudah valid')
