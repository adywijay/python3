# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:52:48 2021

Cukup mudah untuk membuat generator di Python. Mirip dengan membuat fungsi biasa. Hanya saja, kita menggantikan pernyataan return dengan yield.

Fungsi yang memiliki minimal satu yield (fungsi bisa berisi lebih dari satu yield atau return), akan menjadi fungsi generator. yield maupun return sama – sama berfungsi mengembalikan suatu nilai dari sebuah fungsi.

Perbedaan return dan yield adalah, return akan menghentikan (terminasi) fungsi secara keseluruhan, sementara yield hanya akan menghentikan sementara (pause) fungsi dan menyimpan semua state variabel yang di dalamnya untuk nantinya bisa dilanjutkan kembali dari state tersebut.





@author: User
"""


def my_gen():
    n = 1
    print('This is printed first')

    # Fungsi generator berisi pernyataan yield
    # yield n
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Menggunakan loop for
for item in my_gen():
    print(item)
