#https://www.hackerrank.com/challenges/day-of-the-programmer

#!/bin/python3

import sys

def solve(year):
    if year < 1918: # Julian calendar year
        if year % 4 == 0: # Leap year
            return("12.09." + str(year))
        else: # Not leap year
            return("13.09." + str(year))
    elif year == 1918: # Transition year
            return("26.09.1918")
    else: # Gregorian calendar year
        if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)): # Leap year
            return("12.09." + str(year))
        else: # Not leap year
            return("13.09." + str(year))
        
    return(year)

year = int(input().strip())
result = solve(year)
print(result)