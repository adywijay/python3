# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:35:12 2021

@author: Notebook
"""


class staticClass:
    @classmethod
    def panggilClass(cls):
        print('methode statis class decorator dipanggil')


contoh = staticClass()
contoh.panggilClass()
