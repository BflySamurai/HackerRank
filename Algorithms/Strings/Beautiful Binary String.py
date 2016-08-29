#https://www.hackerrank.com/challenges/beautiful-binary-string

#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()

changes = 0
i = 0
while i <= n-3:
    if "010" == s[i:i+3]:
        changes += 1
        i += 3
    else:
        i += 1

print(changes)
