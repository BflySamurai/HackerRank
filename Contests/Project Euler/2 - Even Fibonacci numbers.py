#https://www.hackerrank.com/contests/projecteuler/challenges/euler002

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fibonacci = [1,2]
    sum_evens = 2
    i = 2
    while i <= n:
        i = fibonacci[0]+fibonacci[1]
        if i > n:
            break
        fibonacci.append(i)
        if i%2 == 0:
            sum_evens += i
        fibonacci.pop(0)

    print(sum_evens)