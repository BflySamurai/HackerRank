#https://www.hackerrank.com/challenges/cut-the-sticks

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]

while True:
    if len(arr) == 0:
        break
    print(len(arr))
    
    #find smallest number
    smallest = -1
    for i in range(len(arr)):
        if smallest == -1 or arr[i] < smallest:
            smallest = arr[i]
    
    #cut the numbers by the value of the smallest number
    list_to_pop = []
    for i in range(len(arr)):
        arr[i] = arr[i] - smallest
    arr = [i for i in arr if i not in [0]] #remove the 0's from the list