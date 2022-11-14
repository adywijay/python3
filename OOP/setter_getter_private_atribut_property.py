# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:11:13 2021

@author: Notebook
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def get_age(self):
        return self.__age

  
    def set_age(self, age):
        self.__age = age


stud = Student('Jessa', 14)
print('Name:', stud.name, stud.get_age())
print('############### Before modification ################# \n\n\n') 

stud.set_age(160)
print('Name:', stud.name, stud.get_age())
print('############### After modification #################')
print(hasattr(stud, 'name'))

"""
Note : Setter dan Getter atribut properti builtin hanya bisa digunakan oleh Public
    selain itu tidak bisa (private,protected)
    
"""