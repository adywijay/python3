# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:45:16 2021

@author: Notebook
"""

####################### Program 1 Try dgn multiple except banyak #############
a, b = 1, 0

try:
    print(a/b)
    print("This won't be printed")
    print('10'+10)
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You divided by 0")

####################### Program 2 Try dgn single method except multi value ####
try:
    print('10'+10)
    print(1/0)
except (TypeError, ZeroDivisionError):
    print("Invalid input")
