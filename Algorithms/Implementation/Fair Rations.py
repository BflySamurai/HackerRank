#https://www.hackerrank.com/challenges/fair-rations

#!/bin/python3

import sys


n = int(input().strip())
elements = [int(B_temp) for B_temp in input().strip().split(' ')]

bread_distributed = 0
while True:
    if len(elements) == 0:
        break
    if elements[0]%2 == 0: #if this element is even
        elements.pop(0)
    elif len(elements) == 1: #if there's only one element and it's odd
        break
    else: #if there's more than one element and this one is odd
        elements[0] += 1
        elements[1] += 1
        bread_distributed += 2

if len(elements) > 0:
    print("NO")
else:
    print(bread_distributed)
