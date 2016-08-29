#https://www.hackerrank.com/challenges/time-conversion

#!/bin/python3

import sys

def print_hhmmss(arr):
    hours = arr[0]
    minutes = arr[1]
    seconds = arr[2]
    if hours >= 10:
        hours = str(hours)
    else:
        hours = '0' + str(hours)
    if minutes >= 10:
        minutes = str(minutes)
    else:
        minutes = '0' + str(minutes)
    if seconds >= 10:
        seconds = str(seconds)
    else:
        seconds = '0' + str(seconds)
    print(hours + ':' + minutes + ':' + seconds)
    

time = input()

pm = False
if 'PM' in time:
    pm = True

time_just_numbers = time.strip('APM')
arr = [int(i) for i in time_just_numbers.strip().split(':')]

if pm:
    if not arr[0] == 12:
        arr[0] += 12
else:
    if arr[0] == 12:
        arr[0] = 0

print_hhmmss(arr)