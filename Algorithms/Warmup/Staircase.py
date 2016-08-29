#https://www.hackerrank.com/challenges/staircase

#!/bin/python3

import sys


n = int(input().strip())

for i in range(1,n+1):
    string = ""
    for a in range(n-i):
        string += " "
    for b in range(i):
        string += "#"
    print(string)