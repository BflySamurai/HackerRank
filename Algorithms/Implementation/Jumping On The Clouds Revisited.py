#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

energy = 100
position = 0

while True:
    position = (position+k)%n
    energy -=1
    if c[position] == 1:
        energy -= 2
    if position == 0:
        break

print(energy)
