# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:59:33 2021

@author: Notebook
"""

class Mobil :
    
    def __init__(self,tp, nr, cc):
        self.th_pembuatan = tp
        self.nomr_rangka = nr
        self.slider = cc
        
    def getInfo(self):
        list_panggil = [
                        print('Tahun Pembuatan :', self.th_pembuatan), 
                        print('Nomor Rangka :', self.nomr_rangka),
                        print('Isi Slider :', self.slider)
                        ]
        
        return list_panggil
        
    
class MobilDetail(Mobil):
    
    def __init__(self,tp, nr, cc, merk, warna):
        super().__init__(tp, nr, cc)
    
        self.merek = merk
        self.warna = warna

mobil1 = MobilDetail(2014, 'A2145YDFGH780000RT2', '1500cc','Honda Mobilo', 'Silver')
mobil1.getInfo()
print('Merek : ', mobil1.merek)
print('Warna : ',  mobil1.warna)
    