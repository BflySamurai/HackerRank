#https://www.hackerrank.com/challenges/camelcase

#!/bin/python3

import sys


s = input().strip()

words = 1
A = ord("A")
Z = ord("Z")
for i in range(len(s)):
    letter = s[i]
    if ord(letter) >= A and ord(letter) <= Z:
        words += 1
print(words)
