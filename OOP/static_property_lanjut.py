# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 05:07:13 2021

    Pada materi ini mendefinisikan penggunaan methode property() dimana diinisialisasi
    dengan variabel yg nantinya dpt dipanggil dalam 1x panggil pada saat instance object

@author: Notebook
"""

class StaticProper:

    def __init__(self, a=None, b=None):
        self.__a = a
        self.__b = b

    def getA(self):
        return self.__a


    def setA(self, nilai):
        self.__a = nilai

    a = property(getA, setA)    #

    def getB(self):
        return self.__b


    def setB(self, nilai):
       self.__b = nilai
       
    b = property(getB, setB)    #
    
    
z = StaticProper()
z.a = 9
z.b = 3

b = StaticProper()
b.a = 2
b.b = 4

print(z.b,z.a)
print(z.a,b.b)