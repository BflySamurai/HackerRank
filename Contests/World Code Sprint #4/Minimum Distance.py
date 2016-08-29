#!/bin/python3

import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

minimum = -1

for ii in range(0,n):
    i = A[ii]
    for jj in range(ii+1,n):
        j = A[jj]
        if i == j:
            tempMin = abs(ii-jj)
            if minimum == -1:
                minimum = tempMin
            else:
                minimum = min(minimum,tempMin)

print(minimum)