#https://www.hackerrank.com/challenges/migratory-birds

#!/bin/python3

import sys


n = int(input().strip())
birds = list(map(int, input().strip().split(' ')))

types = [0] * n
for b in birds:
    types[b] += 1

largest_value = 0
largest_value_index = 0
for i in range(1, len(types)):
    t = types[i]
    if t > largest_value:
        largest_value = t
        largest_value_index = i

print(largest_value_index)