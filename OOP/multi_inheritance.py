# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:12:04 2021

 pada penggunaan multi inheritance tidak bisa menggunakan fungsi bulitin super(). melainkan hanya
      bisa KelasInduk.__init__() karena dipakai lebih dari 1 turunan kelas


@author: Notebook
"""

##################### Program 1  ##################
class Base1(object):
    def __init__(self):
        self.str1 = "Ibarat seorang Ayah"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Ibarat sorang Ibu"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)

        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()


##################### Program 2  ##################
class Base(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
