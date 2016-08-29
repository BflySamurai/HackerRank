#https://www.hackerrank.com/challenges/jumping-on-the-clouds

#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

jumps = 0
position = 0
while position < n-1: #quit once it reaches the end
    if position == n-2: #if we're in the second to last position
        position += 1
        jumps += 1
    elif c[position+2] == 0: #if we can jump two squares
            position += 2
            jumps += 1
    else: #if we can only jump one square
        position += 1
        jumps += 1

print(jumps)
