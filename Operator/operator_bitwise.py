# operator bitwise sama seperti operator logika hanyasaja bitwise digunakan untuk
# numerik integer dengan pembacaanya perbit / dirubah kebentuk bit bilangan basis 2

print("============= Operasi Bitwise =================")

# x = eval(input("Masukkan jumlah print kriteria = "))
# y = eval(input("Masukkan jumlah print kriteria = "))
x = 10
y = 12

print("Diketahui Nilai x : ", x,"biner : " + bin(x))
print("Diketahui Nilai y : ", y,"biner : " + bin(y))
#
print("============= Operasi Relasi AND =================")
print("x And y  Hasilnya",x & y)

print("============= Operasi Relasi OR =================")
print("x Or y  Hasilnya",x | y)

print("============= Operasi Relasi XOR =================")
print("x XOr y  Hasilnya",x ^ y)

print("============= Operasi Relasi NOT =================")
print("Not x  Hasilnya",~ x)
print("Not y  Hasilnya",~ y)

print("============= Operasi Betwen shift left =================")
print("<< x  Hasilnya",x << 1)
print("<< y  Hasilnya",y << 1)

print("============= Operasi Betwen shift right =================")
print(">> x  Hasilnya",x >> 1)
print(">> y  Hasilnya",y >> 1)
