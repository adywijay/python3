# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:49:01 2021

@author: Notebook
"""

##################### Prog.1 destruktur panggil manual #######################


class Mobil:
    countinpt = 0

    def __init__(self):
        a = print('Objeck berhasil dibuat')
        return a

    def __del__(self):  # ---------------> Destruktor
        b = print('Objeck berhasil dihapus')
        return b


mobil1 = Mobil()
del mobil1  # destruktur panggil manual


##################### Prog.2 destruktur panggil auto ########################
class Test:

   def __init__(self):
      print("Constructor called file opened")

   def __del__(self):
      print("Destructor called file closed")


def test():#destrucor of t is called after program exit
    t = Test()


test()
