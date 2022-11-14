x = set([1,2,3,4])
y = set([3,5])
union = x | y #gabungan (union)
intersect = x & y #irisan
deference = x - y # anggota x yg tidak ada pada himpunan y
symetric = x ^ y # anggota x atau y yg tidak sama pada anggota keduannya

print("Diket :")
print("x =",x)
print("y =",y)
print("Union / penggabungan : ",union)
print("Intersect / irisan : ",intersect)
print("Deference / Himpunan x yg tidak ada anggota himpuan y : ",deference)
print("Symetric : ",symetric)
