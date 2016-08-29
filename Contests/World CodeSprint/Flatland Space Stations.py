#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()

max_dist = 0

#check the very first city
if c[0] - 0 > max_dist:
    max_dist = c[0] - 0
#check the very last city
if n-1 - c[-1] > max_dist:
    max_dist = n-1 - c[-1]
#check all the cities at the middle point between two space stations
for i in range(len(c)-1):
    dist = (c[i+1]-c[i])//2
    if dist > max_dist:
        max_dist = dist

print(max_dist)