#https://www.hackerrank.com/challenges/quicksort1

n = int(input())
arr = [int(i) for i in input().strip().split(' ')]

pivot = arr[0]
left = []
right = []
equal = []
for e in arr:
    if e == pivot:
        equal.append(e)
    elif e < pivot:
        left.append(e)
    else: # If e > pivot
        right.append(e)

new_arr = left + equal + right
print(*new_arr)