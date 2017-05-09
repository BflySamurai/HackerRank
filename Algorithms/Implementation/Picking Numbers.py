#https://www.hackerrank.com/challenges/picking-numbers

#!/bin/python3

import sys


n = int(input().strip())
integers = [int(a_temp) for a_temp in input().strip().split(' ')]
integers.sort()

current_int = integers[0]
int_count = 0
int_count_last = 0
this_count = 0
highest_count = 0
for i in integers:
    if i == current_int:
        int_count += 1
    elif i == current_int + 1:
        current_int = i
        int_count_last = int_count
        int_count = 1
    else: # If this number is at least 2 larger than the previous
        current_int = i
        int_count_last = 0 # We can't use the previous numbers
        int_count = 1
    
    # Check to see if this is the longest string of integers
    this_count = int_count + int_count_last
    if this_count > highest_count:
        highest_count = this_count

print(highest_count)