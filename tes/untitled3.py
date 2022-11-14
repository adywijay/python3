# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:01:56 2022

@author: WIN_10_PRO
"""
import numpy as np

y = np.array(["apel", "mangga", "durian", "mangga", "apel", "mangga"])
list_ku = list(dict.fromkeys(y))
list_ku.sort(reverse = True)

for i in list_ku:
    cek = np.count_nonzero(y == i)
    if cek == 1:
        continue

    print(i, cek)