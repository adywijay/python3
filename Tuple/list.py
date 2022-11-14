print("====================== intro list numerik ==================== \n")
lst=[100, 200, 300, 400, 500]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])


# Formula = jumlahlist
print("====================== Reverse (negatif) ==================== \n")
print(lst[-0])
print(lst[-1])
print(lst[-2])
print(lst[-3])
print(lst[-4])


print("====================== intro list alfabat ==================== \n")
lst_al = ["Januari", "Februari","Maret", "April"]
print("list nama bulan dalam retensi 4 ", lst_al)

#insert methode ---------------------------------------------------------------------------------
print("====================== after insert with method  append ==================== \n")
lst_al.append("Mei") #methode append hanya menambahkan list single saja
print(lst_al)

print("====================== after insert with method  insert ==================== \n")
lst_al.insert(1, "Juni") #methode insert menambahkan list single pada urutan larik tertentu / array index terdefinisi
print(lst_al)

print("====================== after insert with method  extend ==================== \n")
lst_al.extend(["Juli" , "Juni" , "Agustus"]) #methode extends menambahkan list / penggabungan
print(lst_al)


#Remove list methode ------------------------------------------------------------------------------------------

print("====================== after remove ==================== \n")
lst_al.remove("Juli") #methode remove list hanya single saja
print(lst_al)


#Searching list------------------------------------------------------------------------------------------------
metode = lst_al.index("Juni")
print("Hasil pencarian bulan = Juni, ditemukan pada index ke - ", metode)

#Searching Dinamis dgn operator in
inpt = input("Masukkan retensi Bulan : \n")
print(inpt in lst_al)
