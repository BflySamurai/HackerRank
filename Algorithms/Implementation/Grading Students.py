#https://www.hackerrank.com/challenges/grading

#!/bin/python3

import sys

def solve(grades):
    new_grades = []
    for g in grades:
        if (g>37) and (g%5 > 2):
            new_grades.append(g + 5 - g%5)
        else:
            new_grades.append(g)
    return(new_grades)

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
for r in result:
    print(r)