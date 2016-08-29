#https://www.hackerrank.com/challenges/mars-exploration

#!/bin/python3

import sys


s = input().strip()

wrong = 0
toggle = 0
for i in range(len(s)):
    if toggle == 0 and s[i] != "S":
        wrong += 1
    if toggle == 1 and s[i] != "O":
        wrong += 1
    if toggle == 2 and s[i] != "S":
        wrong += 1
    toggle += 1
    if toggle >= 3:
        toggle = 0

print(wrong)
