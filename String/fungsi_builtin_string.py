# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:43:52 2021

@author: Notebook
"""

ex_kalimat = 'python'
kalimat_1 = "        Ady Wijanarko      "
alamat = 'Surabaya, Jawa Timur, Indonesia'


print(ex_kalimat.capitalize())  # convert string jadi capital
# menengahkan kalimat dengan penghubung karakter tertentu
print(ex_kalimat.center(20, '$'))
# cek pada index keberapakah kalimat itu ditemukan
print(ex_kalimat.count('p', 1, 5))
# cek apakah pada range index tsb terdapat string tsb
print(ex_kalimat.endswith('tho', 0, 5))
# cek pada index keberapakah kalimat itu ditemukan
print(ex_kalimat.find('o', 0, 5))
# cek pada index keberapakah kalimat itu ditemukan, bila tdk ada mengembalikan error
print(ex_kalimat.index('y', 0, 5))
# cek apakah pada variabel tsb ada string / numerik
print(ex_kalimat.isalnum())
# cek apakah pada variabel tsb ada character / alphabet
print(ex_kalimat.isalpha())
# cek apakah pada variabel tsb ada spasi
print(ex_kalimat.isspace())
# cek apakah pada variabel tsb ada angka / numerik
print(ex_kalimat.isdigit())
print(ex_kalimat.isnumeric())
# cek apakah pada variabel tsb ada huruf kecil
print(ex_kalimat.islower())
# cek apakah pada variabel tsb ada huruf besar
print(ex_kalimat.isupper())
# cek jumlah string pada variabel
print(len(ex_kalimat))

# membuang spasi dari arah kiri (suku kata dl kalimat tidak berpengaruh)
print(kalimat_1.lstrip())  # membuang spasi dari arah kanan
print(kalimat_1.rstrip())  # membuang spasi dari arah kiri
print(kalimat_1.strip())   # membuang spasi dari arah kiri & kanan
# cek pada index keberapakah kalimat itu ditemukan (mundur 1 index)
print(ex_kalimat.rfind("y", 0, 2))
# cek nilai max /min pada string yg dikonvert jadi ordinal (ord)
print(ord(max(ex_kalimat)))
print(ord(min(ex_kalimat)))
# mengganti suku kalimat tertentu
print(kalimat_1.replace('Wijanarko', 'Istiana'))
# auto convert huruf besar / kecil
print(ex_kalimat.swapcase())
# auto convert huruf besar
print(ex_kalimat.upper())
# auto convert huruf kecil
print(ex_kalimat.lower())
# mengisi nilai 0 pada awal, sepanjang karakter
print(str.zfill('82137899982', 12))
print('|'.join(kalimat_1))
print(f'kalimatnya adalah: {kalimat_1}')
print(alamat.split('0'))
# ['Surabaya,', 'Jawa', 'Timur', 'Indonesia']

print(alamat.split(','))
# ['Surabaya', ' Jawa Timur', ' Indonesia']

print(alamat.split(', '))
# ['Surabaya', 'Jawa Timur', 'Indonesia']
