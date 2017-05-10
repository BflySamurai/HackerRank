#https://www.hackerrank.com/challenges/runningtime

n = int(input()) #number of elements in the list
arr = [int(i) for i in input().strip().split(' ')]

moves = 0
for i in range(1,n): #start sorting from the second number
    l = i #keep track of location of current number we're moving around
    while True:
        if arr[l-1] <= arr[l] or l == 0:
            break
        else: #swap with number to the left
            temp = arr[l]
            arr[l] = arr[l-1]
            arr[l-1] = temp
            l -= 1
            moves += 1

print(moves)
