# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 12:12:33 2021

@author: Notebook
"""


class Employee:
    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


    # public instance methods
    def show(self):
        print("Name: ", self.name)
        print('Salary:', self.__salary)


emp = Employee('Jessa', 10000)
emp.show()

"""
Memanggil atribut property private
"""

print('Nama:', emp.name)
print('Salary:', emp._Employee__salary)



"""
skrip diatas akan error karena method yang dipanggil bersifat privat dan harus
    dideklarasikan public terlebih dahulu  def show(self): 
agar dpt ditampilkan outputnya

"""