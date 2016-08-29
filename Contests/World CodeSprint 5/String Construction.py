#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
    s = input().strip()

    dict_numbers = {}
    for i in range(len(s)):
        number = s[i]
        if not number in dict_numbers:
            dict_numbers[number] = 1

    print(len(dict_numbers))
