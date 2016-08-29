#https://www.hackerrank.com/challenges/missing-numbers

a_n = int(input())
a_arr = [int(i) for i in input().strip().split()]
b_n = int(input())
b_arr = [int(i) for i in input().strip().split()]

arr = []
for i in range(100):
    arr.append(0)

for n in a_arr:
    n = n%100
    arr[n] -= n

for n in b_arr:
    n = n%100
    arr[n] += n

lower = min(b_arr)
multiplier = (lower//100)*100
missing = []
for i in range(len(arr)):
    if arr[i] > 0:
        n = multiplier + i
        if n < lower:
            n += 100
        missing.append(n)

missing.sort()
print(*missing)
