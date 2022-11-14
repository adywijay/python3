# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:46:30 2021

@author: Notebook
"""

class Company:
    def __init__(self, project, name):
        # Protected member
        self._project = "NLP"
        self.name = name
        

    def show(self):
        print("Name: ", self.name)
        print('Salary:', self._project)


emp = Company(10000, 'Jessa')
emp.show()
print('Project:', emp._project)

# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
        
#         Company.__init__(self) # Memanggil konstruktor protected class

#     def show(self):
#         print("Employee name :", self.name)
        
#         """
#         Memanggil atribut property Protected
#         """
        
#         print("Working on project :", self._project)

# c = Employee("Jessa")
# c.show()

# print(f'\n\n\n')
# # pemanggilan manual protected data member
# print('Project:', c._project)
# print('Nama:', c.name)