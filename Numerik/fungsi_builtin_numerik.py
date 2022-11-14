# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:35:39 2021

@author: Notebook
"""
import math
import random

x = 10
y = -9000
listed = ['a', 'b', 'c', 'd']
listen = [10, 20, 30, 40, 50, 60]

print(abs(-900), abs(900))  # mencari nilai murni / absolut
print(math.ceil(98.05))  # pembulatan keatas terdekat
print(math.exp(10))  # pencarian bilangan exponen
print(math.fabs(2))  # mencari nilai murni / absolut output float
print(math.floor(98.05))  # pembulatan kebawah terdekat
print(math.log(3))  # bilangan logaritma
print(math.log10(100))  # bilangan basis 10
print(min(100, 90, 2))  # nilai minimal
print(max(100, 90, 2))  # nilai max
print(math.modf(10.5))  # memecah bilangan pecahan menjadi tuple
print(pow(2, 3))  # mencari pangkat x ,y
print(round(2.78))  # pembulatan ganda keatas / kebawah
print(math.sqrt(144))  # mencari akar kwadrat
print(random.choice(listed))  # acak bebas baik string / numerik
print(random.randrange(1, 100))  # acak bebas berjarak  numerik
print(random.shuffle(listed))  # acak bebas berjarak  numerik
print(random.shuffle(listen))
