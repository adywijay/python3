# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:12:46 2021
** Pengenalan dan Penggunaan fungsi**

variabel python dalam fungsi :

   1.variabel global ==> variabel yang pemanggilannya diluar block kode fungsi
   2.vaiabel lokal   ==> variabel yang pemanggilannya didalam block kode fungsi

@author: User
"""
a = 2
b = 4  # variabel global
inputan = 100


#======================= Program 1 fungsi parameter aktual =============================#
def test():

    global inputan

    """
    syntax global, agar var global dapat dikonvert /
    dibaca kedalam var lokal
    dengan inputan / nilai value baru
    
    """

    inputan = 30  # inputan / nilai value baru

    hasil = inputan + 1
    return hasil  # inputan / nilai menghasilakan nilai balik


#======================= Program 2 fungsi parameter formal =============================#
def tester(a, b):
    maximum = max(a, b)  # nilai maximum
    print('nilai maximumnya adalah', maximum)


#======================= Program 3  parameter =============================#

tester(a, b)  # parameter formal / default
tester(a=2, b=200)  # parameter + argumen
tester(1200, 200)  # parameter + variabel length / langsung

test()  # parameter default
