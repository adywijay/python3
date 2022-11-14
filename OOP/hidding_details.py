# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:11:43 2021

@author: Notebook
"""

class Student:
    def __init__(self, name, roll_no, age):
       
        self.name = name
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    
    def get_roll_no(self):
        return self.__roll_no

    
    def set_roll_no(self, number):
        
        if number < 100:
            print('inputan invalid')
        else:
            self.__roll_no = number

jessa = Student('Jessa', 10, 15)

jessa.show()
jessa.set_roll_no(200)


jessa.set_roll_no(25)
jessa.show()
