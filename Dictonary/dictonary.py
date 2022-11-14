print("=================== Intro Dictonary ======================= \n")
list_jabatan={'Manager':'Andi Suprobo','Direktur':'Soekiran','Jongos':'Sadirun'}
print(list_jabatan) #Akses seluruh value yg berada pada variabel list_jabatan


print("=========================================================== \n")
biodata={'Nama':'Ady Wijanarko','Alamat':'Yogyakarta, Kotdya','NIK':'09874747484'}
print(biodata['Nama']) #akses key nama
print(biodata['Alamat']) #akses key alamat
print(biodata['NIK']) #akses key nik
print("Data keseluruhan Before : \n\n\n\n", biodata) #Akses seluruh value yg berada pada variabel

biodata['Umur']='23 Tahun' #penambahan value
biodata['Pendidikan']='S1 - Informatika' #penambahan value
biodata['Gelar']=input("Masukkan Gelar : ") #penambahan value


print("=========================================================== \n")
print("Data keseluruhan setelah ditambah \n", biodata)


del biodata['Umur'] #penambahan value
del biodata['Pendidikan'] #penambahan value
del biodata['Gelar'] #penambahan value

print("=========================================================== \n")
print("Data keseluruhan setelah dihapus \n", biodata)
