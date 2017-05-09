#https://www.hackerrank.com/challenges/the-birthday-bar

#!/bin/python3

import sys

def getWays(squares, d, m):
    ways_to_break = 0
    n = len(squares)
    for i in range(n-(m)+1):
        this_sum = 0
        for j in range(m):
            this_sum += squares[i+j]
        if this_sum == d:
            ways_to_break += 1
    return(ways_to_break)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)