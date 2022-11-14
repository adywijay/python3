# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:20:48 2021

    module pada python adalah sebuah file berekstensi .py yang berisi skrip python. 
        Nama dari modul adalah nama nama dari file itu sendiri

        syntax umunya adalah :
            import NamaModul dan
            NamaModul.NamaFungsi(param 1, param 2 .....)

@author: Notebook
"""


"""
apabila filenya belum terbaca karena dir yang berbeda, maka harus dpanggil dulu pathnya dengan :
    
    # import os
    # os.getcwd()
    
    atau 
    
    # import sys
    # sys.path.insert(0, 'd:/python3/Modul')
    
"""

# import ucapan
import ucapan
ucapan.greeting("Jonathan")
