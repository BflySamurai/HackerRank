#https://www.hackerrank.com/challenges/two-arrays

test_cases = int(input())

for t in range(test_cases):
    n,k = input().strip().split(" ")
    n,k = [int(n),int(k)]
    a = [int(i) for i in input().strip().split(' ')]
    b = [int(i) for i in input().strip().split(' ')]
    a.sort()
    b.sort(reverse = True)

    permutation = "YES"
    for i in range(n):
        if not a[i] + b[i] >= k:
            permutation = "NO"
            break

    print(permutation)
