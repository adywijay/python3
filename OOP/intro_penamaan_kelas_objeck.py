# -*- coding: utf-8 -*-
"""
######################################
Created on Fri Nov 19 20:16:34 2021
@author: 247
######################################
- pendefinisian pembuatan kelas dan abstarksi objek
    1. secara umum penulisan kelas bentuk umumnya adalah sbg berikut :
        
        class NamaKelas(object):
            def __init__(self, **param1,**param2):   --> konstruktor
            def __del__(self, **param1,**param2)     --> destruktor
            def NamaMethod(self, **param1,**param2): --> method 1
            def NamaMethod(self, **param1,**param2): --> method 2
            
    2. secara umum penulisan Object bentuk umumnya adalah sbg berikut :
        NamaObjeck = NamaKelas(param1, param2 ... N )
        
    3. sedangkan pemanggilan object umunya :
        NamaObjeck.NamaAtribut / NamaObjeck.NamaMethode (param 1, param 2)
        
"""


class Manusia(object):
    def __init__(self, nm, jk, um, alt):  # konstruktor

        #Definisian Atribut
        self.nama = nm
        self.jenkel = jk
        self.umur = um
        self.alamat = alt

        #Method
        
    def GetGreetings(self):
        nama = self.nama
        return nama


#Abstraction Objeck
orang1 = Manusia("Sugeng Sunarso", "L", "23", "Plupuh, Godangrejo, Nganjuk")

#Pemanggilan object
print(f'Hallo Berohw {orang1.GetGreetings()}')
print("\n\n\n")
print(f'Nama Saya     : {orang1.nama}')
print(f'Jenis Kelamin : {orang1.jenkel}')
print(f'Umur          : {orang1.umur}')
print(f'Alamat        : {orang1.alamat}')
