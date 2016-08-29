#https://www.hackerrank.com/challenges/handshake

def factorial(n):
    factorial = 0
    for i in range(n):
        factorial += i
    return(factorial)


n = int(input())
arr = [int(input()) for i in range(n)]

for i in range(n):
    print(factorial(arr[i]))