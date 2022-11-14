# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:35:39 2021

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