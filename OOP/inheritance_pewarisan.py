# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 05:33:26 2021


Konstruktor pada kelas turunan memiliki perilaku yang sedikit berbeda dengan konstruktor yang terdapat pada kelas induk.

        Apa yang terjadi ketika kelas turunan memiliki konstruktor sendiri?

Ia akan menimpa konstruktor dari kelas induk sehingga konstruktor kelas induk tidak akan pernah dieksekusi.
    


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