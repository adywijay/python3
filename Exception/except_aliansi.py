# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:52:55 2021

@author: Notebook
"""

# Define a function here.

####################### Program 1 Try Except dengan aliansi #############
print("Program 1 \n\n\n")


def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n", Argument)


# Call above function here.
temp_convert("xyz")


"""
kode di atas adalah contoh aliasi jenis value exception yang dialiansi 
guna menapilkan pesan error berdasar value error yg dipanggil pada except tersebut.
"""


####################### Program 2 Try Except tanpa aliansi #############
print("Program 2 \n\n\n\n\n\n\n\n")


def temp_conv(var):
    try:
        return int(var)
    except ValueError:
        print("The argument does not contain numbers\n")


# Call above function here.
temp_conv("xyz")
