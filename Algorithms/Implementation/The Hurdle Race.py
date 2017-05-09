#https://www.hackerrank.com/challenges/the-hurdle-race

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))

drinks_needed = 0
for i in height:
    if i > k:
        if i - k > drinks_needed:
            drinks_needed = i - k

print(drinks_needed)