# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:30:52 2021

@author: Notebook
"""

# Program Simple ######################################33
"""
import os # memanggil modul system

# imbuhan string r ===> artinya unicode error pemanggilan oleh system code read files

old_name = r"D:\python3\File\tester.txt"
new_name = r"D:\python3\File\testers.txt"

os.rename(old_name, new_name)

"""


import os
os.chdir("d:/python3/File")   # baca direktori posisi aktif


# print list file dir posisi aktif
# print(os.listdir(os.getcwd()))

# renaming directory ''tutorialsdir"
os.rename("df.txt", "asu.txt")

print("Successfully renamed.")

# listing directories after renaming "python3"
#print("the dir is: %s" % os.listdir(os.getcwd()))
