#https://www.hackerrank.com/challenges/breaking-best-and-worst-records

#!/bin/python3

import sys

def getRecord(s):
    low = s[0]
    low_count = 0
    high = low
    high_count = 0
    for i in range(1, len(s)):
        score = s[i]
        if score < low:
            low = score
            low_count += 1
        elif score > high:
            high = score
            high_count += 1
            
    return(high_count, low_count)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))