#https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem


n = int(input())
arr = sorted(int(i) for i in input().split())

i = n-3

output = ""
while i >= 0:
    if arr[i] + arr[i+1] > arr[i+2]:
        output = str(arr[i]) + " " + str(arr[i+1]) + " " + str(arr[i+2])
        break
    i -= 1

if output == "":
    output = "-1"
    
print(output)