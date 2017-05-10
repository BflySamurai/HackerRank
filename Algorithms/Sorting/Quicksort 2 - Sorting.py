#https://www.hackerrank.com/challenges/quicksort2

def quicksort (arr):
    if len(arr) < 2:
        return(arr)
    pivot = arr[0]
    left, right, equal = [], [], []
    for e in arr:
        if e == pivot:
            equal.append(e)
        elif e < pivot:
            left.append(e)
        else: # If e > pivot
            right.append(e)
    
    left = quicksort(left)
    right = quicksort(right)
    new_arr = left + equal + right
    print(*new_arr)
    return(new_arr)

n = int(input())
arr = [int(i) for i in input().strip().split(' ')]
quicksort(arr)