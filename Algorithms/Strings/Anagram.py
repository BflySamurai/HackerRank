#https://www.hackerrank.com/challenges/anagram

import math


test_cases = int(input())

for t in range(test_cases):
    s = input()
    changes = 0
    length = math.floor(len(s))
    middle = int(length/2)
    if length%2 == 0: #if even number of letters
        #turn string into 2 lists
        list_1 = list(s[:middle])
        list_1.sort()
        list_2 = list(s[middle:])
        list_2.sort()
        #find the number of changes we'll need to make
        i = 0
        while i < len(list_1):
            if list_1[i] in list_2:
                list_2.remove(list_1[i])
                list_1.pop(i)
            else:
                i += 1
        print(len(list_1))
    else: #if odd number of letters
        print(-1)
