# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:17:42 2021

    kelas Abstrak adalah kelas dasar / blueprint yang dapat digunakan untuk 
        menciptakan Objek baru agar tidak duplicate, namun tidak dapat diinstance secara langsung
        melainkan harus dibuat pewarisan dahulu

bentuk syntax dasarnya :
    from abc import ABC, abstractmethod
        class NamaKelas (ABC):
            @abstractmethod
            namaMethod(self, parameter 1,parameter 2, ....... )
            
            
@author: Notebook
"""

from abc import ABC, abstractmethod

class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        print("All checks")

    @abstractmethod
    def land(self):
        print("All checks completed")

class Jet(Aircraft):

    def fly(self):
        super().fly()
        print("My jet is flying")

    def land(self):
        super().land()
        print("My jet has landed")

jet1 = Jet()
jet1.land()
jet1.fly()