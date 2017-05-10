#https://www.hackerrank.com/challenges/correctness-invariant

def insertion_sort(arr):
    for sort_index in range(1, len(arr)):
        compare_index = sort_index-1
        sort_number = arr[sort_index]
        while (compare_index >= 0) and (arr[compare_index] > sort_number):
            arr[compare_index+1] = arr[compare_index] # Shift the compar_number to the right if it's smaller than the sort_number
            compare_index -= 1
        arr[compare_index+1] = sort_number # Insert the sort_number into the appropriate index


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))