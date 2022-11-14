# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:17:16 2021

    Polymorphism adalah kemampuan untuk mengambil bentuk yang berbeda dengan sifat yang sama 
    atau override .


@author: Notebook
"""
# 1. Polymorphisme dalam function

def tambah(x, y, z = 0):
    return x + y+z
 
print(tambah(2, 3))
print(tambah(2, 3, 4))



# 2. Polymorphisme dalam kelas

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
  
    def language(self):
        print("Hindi is the most widely spoken language of India.")
  
    def type(self):
        print("India is a developing country.")
  
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
  
    def language(self):
        print("English is the primary language of USA.")
  
    def type(self):
        print("USA is a developed country.")
 
  
obj_ind = India()
obj_usa = USA()

obj_ind.capital()
obj_usa.capital()
