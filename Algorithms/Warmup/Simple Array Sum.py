#https://www.hackerrank.com/challenges/simple-array-sum

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

sum = 0
for i in range(n):
    sum += arr[i]
print(sum)