# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:52:35 2021

    isinstance(Objeck, NamaKelas)
    issubclass(KelasTurunan, KelasInduk)

@author: Notebook
"""

class Orang:

  def __init__(self, nama, asal):
    self.nama = nama
    self.asal = asal
    print('konstruktor Orang dipanggil')

  def perkenalan(self):
    print(f'Perkenalkan nama saya {self.nama} dari {self.asal}')


#inheritance

class Pelajar (Orang):
  
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal


class Pekerja (Orang):
  def __init__(self, nama, asal):
      self.nama = nama
      self.asal = asal


andi = Orang('Andi', 'Surabaya')
andi.perkenalan()

rika = Orang('Rikha', 'Gablok')
rika.perkenalan()

deni = Pelajar('Deni', 'Makassar')
deni.perkenalan()

budi = Pekerja('Budi', 'Pontianak')
budi.perkenalan()

a = isinstance(andi, Orang)
b = issubclass(Pelajar, Orang)
print(a,b)