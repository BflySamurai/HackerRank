#https://www.hackerrank.com/challenges/sherlock-and-squares

import math

test_cases = int(input())

for n in range(test_cases):
    beginning,end = input().strip().split(' ')
    beginning,end = [int(beginning),int(end)]

    start = math.ceil(pow(beginning,0.5))
    finish = math.floor(pow(end,0.5))+1
    print(finish-start)
