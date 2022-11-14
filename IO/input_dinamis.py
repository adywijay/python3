print(input("Masukkan nama Anda :"))
print('{} dan {}'.format('Huda', 'Budi'))
# Huda dan Budi

print('{1} dan {0}'.format('Huda', 'Budi'))
# Budi dan Huda


print('Halo {namaDepan} {namaBelakang}'
  .format(namaDepan='Agus', namaBelakang='Priyono'))
# Halo Agus Priyono

# begini juga bisa:
print('Halo {namaDepan} {namaBelakang}'
  .format(
    namaBelakang='Priyono',
    namaDepan='Agus'
  )
)
# Halo Agus Priyono
