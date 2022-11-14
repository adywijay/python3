#type set seperti list akan tetapi pendefinisiannya beda, seperti array multi dimensi

print("====================== intro set type numerik ==================== \n")
angka = set([10,20,30,40,40])
print(angka) #print seluruh array
print(list(angka)[1]) #print array index


print("====================== intro set type alfabet ==================== \n")
angka = set("PYTHON")
print(angka) #print seluruh array
print(list(angka)[1]) #print array index

print("====================== manipulasi set ==================== \n")
angka = set([10,20,30,40,60])
print("====================== before ==================== \n")
print(angka) #print seluruh array
print("====================== penambahan ==================== \n")
angka.add(50) #callback penambahan list set array
print("methode add () :", angka) #print seluruh arrayprint()

angka.update([70]) #callback penambahan list set array9
print("methode update () :", angka) #print seluruh arrayprint()

print("====================== penghapusan ==================== \n")
angka.remove(50) #calback menghapus array tertentu dari list set array
print("methode remove () :", angka) #print seluruh arrayprint()

angka.clear() #calback menghapus seluruh list set array
print("methode clear () :", angka) #print seluruh arrayprint()
