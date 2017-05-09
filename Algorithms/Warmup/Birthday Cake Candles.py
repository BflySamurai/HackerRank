#https://www.hackerrank.com/challenges/birthday-cake-candles

#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

count = 1
tallest = height[0]
for i in range(1, n):
    h = height[i]
    if h == tallest:
        count += 1
    elif h > tallest:
        tallest = h
        count = 1

print(count)