# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:57:28 2021

Fungsi break adalah berhenti sejenak apabila suatu keputusan tercapai

@author: Notebook
"""

for i in range(0, 10):
    if i == 5:
        break
    print(i)

for i in range(0, 10):
    if i // 2 == 0:
        continue
    print(i)
