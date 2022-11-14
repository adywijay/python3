# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 00:29:09 2021


    getattr(obj, name[, default]) – Mengakses atribut objek
    hasattr(obj, name) – Memeriksa apakah objek memiliki atribut tertentu atau tidak
    setattr(obj, name, value) – Mengatur nilai atribut. Jika atribut tidak ada, maka atribut tersebut akan dibuatkan
    delattr(obj, name) – Menghapus atribut dari objek




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


mobil1 = Mobil('2019')
#setter & getter menggunalan fungsi builtin python
setattr(mobil1, 'merek', 'Inova Matic')
b = getattr(mobil1, 'merek')

print('Merek Mobil : ', b)
print('Tahun Perakitan : ', mobil1.tpembuatan)
