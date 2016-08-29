#https://www.hackerrank.com/challenges/find-digits

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    digits = [int(i) for i in str(n)]
    counter = 0
    for i in range(len(digits)):
        if digits[i] != 0:
            if n%digits[i] == 0:
                counter += 1
    print(counter)
