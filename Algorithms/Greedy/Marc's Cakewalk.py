#https://www.hackerrank.com/challenges/marcs-cakewalk

#!/bin/python3

import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))

calories.sort(reverse = True)

total_miles = 0
for i in range(len(calories)):
    c = calories[i]
    miles = c*(pow(2,i))
    total_miles += miles

print(total_miles)