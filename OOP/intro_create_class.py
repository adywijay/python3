# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:18:10 2021

@author: Notebook
"""


class Manusia(object):
    def __init__(self, nm):  # konstruktor

        #Definisian Atribut
        self.nama = nm

        #Method

    def GetGreetings(self):
        nama = self.nama
        return nama


a = str(input('Masukkan Nama Anda : '))
orang1 = Manusia(a) #Istance
print(f'Hallo Berohw {orang1.GetGreetings()}')
