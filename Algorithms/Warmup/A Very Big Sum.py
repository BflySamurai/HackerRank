#https://www.hackerrank.com/challenges/a-very-big-sum

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr_sum = 0
for i in range(n):
    arr_sum += arr[i]

print(arr_sum)