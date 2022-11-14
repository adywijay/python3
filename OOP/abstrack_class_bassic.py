# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:01:09 2021

kelas Abstrak adalah kelas dasar / blueprint yang dapat digunakan untuk 
   1. menciptakan Objek baru agar tidak duplicate, namun tidak dapat diinstance secara langsung
    melainkan harus dibuat pewarisan dahulu & dioverride ---> pengulangan method yg sama.
    
   2. fungsinya hampir sama dengan inheritance biasa hanya saja, kelas abstrak difungsikan
       sebagai kelas bassic / dasar
       
bentuk syntax dasarnya :
   1.  class NamaKelasAbstrak():
            def NamaMethod(self, param 1, param 2,...........)
           pass
   2. class NamaKelasAbstrak():
            def NamaMethod(self, param 1, param 2,...........)
           raise NotImplementedError
    
    
    
@author: Notebook
"""

class Person :
    
    def makan(self) :
        print('method kelas abstrak dipanggil')
        pass
        #raise NotImplementedError
    
    def berjalan(self):
        print('method kelas abstrak dipanggil')
        pass
        #raise NotImplementedError
        
        
class Mantan(Person):
    def __init__(self, nama, umur):
        self.nama  = nama
        self.umur  = umur
        
    def makan(self):
        super().makan()
        print(f"Seorang Mantan : {self.nama}, berumur {self.umur} tahun sedang makan")
        
    def berjalan(self):
        super().berjalan()
        print(f"Seorang Mantan : {self.nama}, berumur {self.umur} tahun sedang berjalan")
        
        
mantan1 = Mantan('Inisial A', 27)
mantan1.makan()
mantan1.berjalan()