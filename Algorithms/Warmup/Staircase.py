#https://www.hackerrank.com/challenges/staircase

#!/bin/python3

import sys


n = int(input().strip())

for i in range(1,n+1):
    string = " "*(n-i) + "#"*i
    print(string)