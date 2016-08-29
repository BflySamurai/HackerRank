#https://www.hackerrank.com/challenges/the-time-in-words

#!/bin/python3

import sys


h = int(input().strip())
m = int(input().strip())

number_word_map = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "twenty one",
    "twenty two",
    "twenty three",
    "twenty four",
    "twenty five",
    "twenty six",
    "twenty seven",
    "twenty eight",
    "twenty nine",
    "thirty",
    ]


arr = []

if m == 0:
    arr.append(number_word_map[h])
    arr.append("o' clock")
else:
    #minutes
    if m == 30:
        arr.append("half")
    elif m == 15 or m == 45:
        arr.append("quarter")
    elif m < 30:
        arr.append(number_word_map[m])
        arr.append("minutes")
    else:
        arr.append(number_word_map[60-m])
        arr.append("minutes")

    #past / to the hour
    if m <= 30:
        arr.append("past")
        arr.append(number_word_map[h])
    else:
        arr.append("to")
        new_h = h+1
        if new_h > 12:
            new_h%12
        arr.append(number_word_map[(new_h)])

string = " ".join(arr)
print(string)
