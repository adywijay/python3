# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:19:34 2021

@author: Notebook
"""


class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"
        
        
"""
Analoginya : dasarnya adalah membuat kelas proteksi sehingga bagaimana caranya
    agar dapat dipanggil. Agar dapat dipanggil maka dilakukan pewarisan kelas proteksi
    menjadi public sehingga kelas yg awalnya proteksi dapat diakses semua kelas
"""
            
                                #ATAU

"""
dideklarasikan dalam kontrukstor kemudian dipanggil pada method yang nantinya
    dipanggil pada intance atau outinstance
"""


# Inheritance dari kelas Proteksi 
class Employee(Company):
    def __init__(self, name):
        self.name = name
        
        Company.__init__(self) # Memanggil konstruktor protected class

    def show(self):
        print("Employee name :", self.name)
        
        """
        Memanggil atribut property Protected
        """
        
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

print('\n\n\n')
# pemanggilan manual protected data member
print('Project:', c._project)
print('Nama:', c.name)
