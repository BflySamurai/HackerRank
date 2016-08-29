#https://www.hackerrank.com/challenges/divisible-sum-pairs

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
arr = [int(i) for i in input().strip().split(' ')]
pairs = 0

for i in range(1,n):
    for j in range(i):
        if (arr[i] + arr[j])%k == 0:
            pairs += 1

print(pairs)