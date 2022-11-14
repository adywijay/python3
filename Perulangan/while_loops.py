# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:42:41 2021

@author: Ady
"""

i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(j, end='')
        j = j + 1
    i = i + 1
    print()

    print('Show Perfect number fom 1 to 100')
    
n = 2
# outer while loop
while n <= 100:
    x_sum = 0
    # inner for loop
    for i in range(1, n):
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print('Perfect number:', n)
    n += 1

    numbers = [[1, 2, 3], [4, 5, 6]]

cnt = 0
for i in numbers:
    for j in i:
        print('iteration', cnt, end=': ')
        print(j)
        cnt = cnt + 1
