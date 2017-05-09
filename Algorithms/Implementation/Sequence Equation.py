#https://www.hackerrank.com/challenges/permutation-equation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
arr = list(map(int, input().strip().split(' ')))

sequence = {}
for i in range(len(arr)):
    sequence[i+1] = arr[i]

for i in range(1, len(arr)+1):
    for key in sequence:
        if sequence[key] == i:
            for key2 in sequence:
                if sequence[key2] == key:
                    print(key2)
                    break
            break