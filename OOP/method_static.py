# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 13:21:47 2021

pendeklarasian static method :
    1. menggunakan dekorator (@staticmethod)
    2. menggunakan function (staticmethod()) : 
        |--> NamaKelas.NamaMethode = staticmethod(NamaKelas.NamaMethode(param 1, param 2))
        
                ATAU 
        Class.staticmethodFunc()
            or even
        Class().staticmethodFunc()
        
        
    3. setelah methode statis didefinisikan kemudian dipanggil dengan
    
    NamaKelas.NamaMethode = NamaKelas.NamaMethode(param 1, param 2)
    
    
    static Method berarti hanya method saja yang dipanggil diluar instance
       ketika sudah dideklarasikan

@author: Notebook
"""

##################### Prog.1  #######################
class ContohStatic:

    @staticmethod  # menggunakan dekorator (@staticmethod)
    def PanggilMeth():
        print('methode statis dipanggil')


param1 = ContohStatic()
param1.PanggilMeth()


##################### Prog.2  #######################
class Mathematics:

    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))
