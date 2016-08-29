#https://www.hackerrank.com/challenges/string-construction

#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    cost = 0
    letters = []
    for l in s:
        if not l in letters:
            letters.append(l)
            cost += 1
    print(cost)
