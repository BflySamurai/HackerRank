#https://www.hackerrank.com/challenges/kangaroo

#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


if v1 == v2:
    if x1 == x2:
        print("YES")
    else:
        print("NO")
else:
    '''
    Solving for the X intersection of two slopes
    Slope 1: y = a*x + b
    Slope 2: y = c*x + d
    ax + b = cx + d
    ax-cx = d-b
    x(a-c) = d-b
    x = (d-b)/(a-c)
    '''
    a = v1
    b = x1
    c = v2
    d = x2
    intersection =  (d-b)/(a-c)
    if intersection%1 == 0 and intersection > 0: #if it's a whole number and a positive number
        print("YES")
    else:
        print("NO")