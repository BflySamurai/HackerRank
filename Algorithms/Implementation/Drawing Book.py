#https://www.hackerrank.com/challenges/drawing-book

#!/bin/python3

import sys
import math

def solve(n, p):
    paper_count = 1 + math.floor(n/2)
    paper_p = 1 + math.floor(p/2)
    from_front = paper_p - 1
    from_back = paper_count - paper_p
    if from_front < from_back:
        return(from_front)
    else:
        return(from_back)
    

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)