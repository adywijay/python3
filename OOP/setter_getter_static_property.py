# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:45:54 2021

@author: Notebook
"""

##################### Program 1 settergetter property kelas Private ##################
class StaticProper:

    def __init__(self, a=None, b=None):
        self.__a = a
        self.__b = b

      # menggunakan dekorator (@property)
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, nilai):
        self.__a = nilai

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, nilai):
       self.__b = nilai


param0 = StaticProper()
param1 = StaticProper(4, 2)

param0.a = 3
param0.b = 8

print("[",param0.a, param0.b,"]")
print("[",param1.a, param1.b,"]")

print('######## settergetter prop kelas Private ######### \n')

##################### Program 2 settergetter property kelas Private ##################
class StaticProtect:

    def __init__(self, c='', d=''):
        self._c = c
        self._d = d

      # menggunakan dekorator (@property)
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, nilai):
        self._c = nilai

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, nilai):
       self._d = nilai


atrrc = StaticProtect()
attrd = StaticProtect()

atrrc.c = 4
atrrc.d = 9
attrd.c = 8
attrd.d = 1

s = print("[",atrrc.c, atrrc.d,"]")
print("[",attrd.c, attrd.d,"]")
print('######## settergetter prop kelas Protect ######### \n')