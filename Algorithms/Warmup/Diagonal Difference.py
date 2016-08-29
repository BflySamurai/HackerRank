#https://www.hackerrank.com/challenges/diagonal-difference

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diagonal_1 = 0
diagonal_2 = 0

for i in range(n):
    diagonal_1 += a[i][i]
    diagonal_2 += a[n-1-i][i]

diff = abs(diagonal_1 - diagonal_2)
    
print(diff)