# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:56:28 2021

    Dalam sebuah inheritance apabila sebuah kelas turunan memiliki konstruktor sendiri
     dari kelas induk, maka kana menyebabkan peninbunan atribut properti, dengan
     demikian ada beberapa cara agar tidak tertimbun oleh atribut properti lain
     
     Caranya ada 2:

         1. yang pertama menggunakan fungsi super().__init__(), fungsi super() ada 2 macam yaitu:
             1. memanggil kontruktor kelas induk agar tidak tertimpa ketika dipanggil
             2. untuk memanggil methode dari kelas induk
             
         2. dan yang kedua menggunakan KelasInduk.__init__()


@author: Notebook
"""
##################### Program 1  ##################
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
        super().__init__(nama, asal) #
        super().perkenalan()


class Pekerja (Orang):
    def __init__(self, nama, asal):
        
      Orang.__init__(self, nama, asal) #


andi = Orang('Andi', 'Surabaya')
andi.perkenalan()
print('\n\n\n')

rika = Orang('Rikha', 'Gablok')
rika.perkenalan()
print('\n\n\n')


deni = Pelajar('Deni', 'Makassar')
#deni.perkenalan()
print('\n\n\n')


budi = Pekerja('Budi', 'Pontianak')
budi.perkenalan()

##################### Program 2  ##################
class Person:
     def walk(self):
         print('Person walks')
         
         
class Student(Person):
     def gotoClass(self):
         super().walk()
 
obj = Student()
obj.gotoClass()
