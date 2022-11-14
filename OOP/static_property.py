# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:00:01 2021

  1. static Property berarti hanya propertinya saja yang dipanggil diluar instance
     ketika sudah dideklarasikan
     
  2. dengan kata lain parameter syntax @property adalah sebagi Getter nya / yang
      digunakan untuk output / retrive output yang dipanggil diluar instance

@author: Notebook
"""

##################### Program 1 staic property kelas Private ##################
class StaticProper:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

      # menggunakan dekorator (@property)

    @property
    def getA(self):
            return self.__a
    
    @property
    def getB(self):
            return self.__b


param1 = StaticProper(4, 2)
print('Nilai Parameter A : ',param1.getA)
print('Nilai Parameter B : ',param1.getB)
print('################## kelas Private ############# \n\n')


##################### Program 2 staic property kelas Publics ##################
class Coba:

    def __init__(self, d, f):
        self.d = d
        self.f = f

      # menggunakan dekorator (@property)

    @property
    def getD(self):
            return self.d
    
    @property
    def getF(self):
            return self.f


x = Coba(4, 9)
print('Nilai Parameter A : ',x.getD)
print('Nilai Parameter B : ',x.getF)
print('################## kelas Public ############# \n\n')


##################### Program 3 staic property kelas Protect ##################
class Coba1:

    def __init__(self, g, h):
        self._g = g
        self._h = h

      # menggunakan dekorator (@property)

    @property
    def getG(self):
            return self._g
    
    @property
    def getH(self):
            return self._h


y = Coba1(14, 90)
print('Nilai Parameter A : ',y.getG)
print('Nilai Parameter B : ',y.getH)
print('################## kelas Protected ############# \n\n')