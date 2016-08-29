#https://www.hackerrank.com/challenges/the-love-letter-mystery

import math


test_cases = int(input())

for t in range(test_cases):
    s = input()
    decrements = 0
    length = math.floor(len(s))
    if length%2 == 0: #if even number of letters
        for i in range(int(length/2)):
            decrements += abs(ord(s[i])-ord(s[length-1-i]))
    else:
        for i in range(int(length/2)):
            decrements += abs(ord(s[i])-ord(s[length-1-i]))
    print(decrements)
