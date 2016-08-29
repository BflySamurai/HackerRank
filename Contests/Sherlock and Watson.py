arr_temp = [int(i) for i in input().strip().split(' ')]
n = arr_temp[0]
right_shift = arr_temp[1]
q = arr_temp[2]
arr = [int(i) for i in input().strip().split(' ')]

queries = []
for i in range(q):
    a = int(input())
    queries.append(a)

arr_shifted = []
for i in range(len(arr)):
    b = right_shift%n
    a = arr[i-b]
    arr_shifted.append(a)

for i in range(len(queries)):
    a = arr_shifted[queries[i]]
    print(a)