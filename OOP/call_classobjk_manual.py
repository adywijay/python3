# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 22:57:17 2021

@author: Notebook
"""

class Mobil(object):
    countinpt = 0

    def __init__(self, tp):
        self.tpembuatan = tp
        Mobil.countinpt += 1

    def setMerk(self, mrk):
        self.merek = mrk

    def getMerk(self):
        return self.merek

    def getJmlData(self):
        counter = Mobil.countinpt
        return counter

#pemanggilan objeck manual
mobil1 = Mobil('2019')
mobil1.setMerk('Nissan 203ds')
mobil2 = Mobil('2019')
mobil2.setMerk('Xenia Matic jZ#3')

print(mobil1.getMerk(), mobil2.getMerk())
print(mobil1.getJmlData())