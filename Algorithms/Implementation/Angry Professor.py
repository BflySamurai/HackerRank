#https://www.hackerrank.com/challenges/angry-professor

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    arr = [int(a_temp) for a_temp in input().strip().split(' ')]

    late_students = 0
    for i in range(n):
        if arr[i] > 0:
            late_students += 1
    
    students_on_time = n-late_students
    if students_on_time < k: #Class canceled
        print("YES")
    else: #Class proceeds
        print("NO")