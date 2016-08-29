#https://www.hackerrank.com/challenges/plus-minus

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive = 0
negative = 0
zero = 0

for i in range(n):
    if arr[i] > 0:
        positive += 1
    elif arr[i] < 0:
        negative += 1
    else:
        zero += 1

print(positive/n)
print(negative/n)
print(zero/n)