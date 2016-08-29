#https://www.hackerrank.com/challenges/equal-stacks

#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

height = 0
a = sum(h1)
b = sum(h2)
c = sum(h3)

#while all of the stacks are larger than 0
while a > 0 and b > 0 and c > 0:
    if a > b or a > c: #if a is not the same height as another stack
        a = a - h1[0] #remove the height of the first item from the stack
        h1.pop(0) #remove the first item from h1
    elif b > a or b > c:
        b = b - h2[0]
        h2.pop(0)
    elif c > a or c > b:
        c = c - h3[0]
        h3.pop(0)
    else: #if all of the stacks are equal size
        height = a #set 'height' to equal any of the stack heights
        break
        
print(height)