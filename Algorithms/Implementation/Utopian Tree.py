#https://www.hackerrank.com/challenges/utopian-tree

#!/bin/python3

import sys


test_cases = int(input().strip())
for a0 in range(test_cases):
    cycles = int(input().strip())
    height = 1
    for i in range(cycles):
        if i%2 == 0 or i == 0:
            height *= 2
        else:
            height += 1
    print(height)
        
