#https://www.hackerrank.com/challenges/hackerrank-in-a-string

#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    
    check_string = "hackerrank"
    check_index = 0
    length = len(check_string)
    
    for c in s:
        if c == check_string[check_index]:
            check_index += 1
        if check_index == length:
            break
    
    if check_index == length:
        print("YES")
    else:
        print("NO")