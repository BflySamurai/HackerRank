#https://www.hackerrank.com/challenges/insertionsort1

l = int(input())-1 #location of the value to sort
arr = [int(i) for i in input().strip().split(' ')]

v =  arr[l] #value

while True:
    if arr[l-1] <= v <= arr[l+1]:
        arr[l] = v
        print(*arr)
        break
    if l == 0 and v < arr[l+1]: #if it's reached the beginning
        arr[l] = v
        print(*arr)
        break
    if l == len(arr)-1 and arr[l-1] < v: #if it's reached the end
        arr[l] = v
        print(*arr)
        break
    if arr[l-1] > v:
        arr[l] = arr[l-1] #shift the value over in the array
        l -= 1 #shift or location marke over
    if arr[l+1] < v:
        arr[l] = arr[l+1] #shift the value over in the array
        l += 1 #shift or location marke over
    print(*arr)