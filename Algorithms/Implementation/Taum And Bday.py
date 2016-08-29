#https://www.hackerrank.com/challenges/taum-and-bday

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    blacks_needed,whites_needed = input().strip().split(' ')
    blacks_needed,whites_needed = [int(blacks_needed),int(whites_needed)]
    black_cost,white_cost,convert_cost = input().strip().split(' ')
    black_cost,white_cost,convert_cost = [int(black_cost),int(white_cost),int(convert_cost)]

    #finding the lowest price for blacks and whites
    if black_cost > white_cost + convert_cost:
        black_cost = white_cost + convert_cost
    elif white_cost > black_cost + convert_cost:
        white_cost = black_cost + convert_cost

    #buy all the presents
    cost = blacks_needed*black_cost + whites_needed*white_cost
    print(cost)
