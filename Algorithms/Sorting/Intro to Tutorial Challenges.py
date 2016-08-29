#https://www.hackerrank.com/challenges/tutorial-intro

value = int(input())
n = int(input())
arr = [int(i) for i in input().strip().split(' ')]

for i in range(len(arr)):
    if arr[i] == value:
        print(i)