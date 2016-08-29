#https://www.hackerrank.com/challenges/strange-code

#!/bin/python3

import sys


t = int(input().strip())
n = 3



column_value = n
remainder = t
while True:
    if remainder <= column_value:
        break
    else:
        remainder -= column_value
        column_value *= 2

result = column_value - (remainder-1)

print(result)
