#https://www.hackerrank.com/challenges/encryption

#!/bin/python3

import sys
import math

string = input().strip()

length = len(string)
floor = math.floor(pow(length,0.5))
ceil = math.ceil(pow(length,0.5))

if floor * floor >= length:
    rows = floor
    cols = floor
elif floor * ceil >= length:
    rows = floor
    cols = ceil
else:
    rows = ceil
    cols = ceil

#put into rows and colunms
arr1 = []
c = 0
r = 0
place = 0
for r in range(rows):
    string_temp = ""
    for c in range(cols):
        if place < length:
            string_temp = string_temp + string[place]
            place += 1
    arr1.append(string_temp)

arr2 = []
for c in range(cols):
    new_string = ""
    for r in range(rows):
        string_row = arr1[r]
        if c <= len(string_row)-1: #if there are still characters in this column (for this row)
            new_string = new_string + string_row[c]
    arr2.append(new_string)

encrypted = " ".join(arr2)
print(encrypted)
