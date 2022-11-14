print("======================== Perulangan FOR =======================\n")
# syntax : for var_inisial in range(mulai,jumlah / akhir, lompat):

for i in range(5):
    print('Perulangan ke = ', i)

print("======================== FOR with jumping =======================\n")
for i in range(2, 15, 3):
    print('Perulangan ke = ', i + 1)

print("======================== FOR  modif =======================\n")
for i in range(7):
    print('$' * (i + 1))

print("======================== FOR  modif =======================\n")
nama_hewan = ['kadhal', 'clarat', 'bunglon', 'asu']

for w in nama_hewan:
    print(w, len(w))  # fungsi len untuk menghitung string

for x in range(ord('a'), ord('z')):
    # print("%c : Huruf Abjad" % chr(x))

    print("%c : Huruf Abjad" % str(chr(x)))

print("======================== FOR  Example =======================\n")
# outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()

rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')

names = ['Kelly', 'Jessa', 'Emma']
# outer loop
for name in names:
    # inner while loop
    count = 0
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()

# 5 rows
for name in range(5):
    # 3 column
    for j in range(3):
        print('*', end='')
    print()

for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j)

first = [2, 4, 6]
second = [2, 4, 6]
for i in first:
    for j in second:
        if i == j:
            continue
        print(i, '*', j, '= ', i * j)

first = [2, 3, 4]
second = [20, 30, 40]
final = []
for i in first:
    for j in second:
        final.append(i + j)
print(final)

first = [2, 3, 4]
second = [20, 30, 40]
final = [i + j for i in first for j in second]
print(final)

final = [[x, y] for x in [10, 20, 30] for y in [30, 10, 50] if x != y]
print(final)
