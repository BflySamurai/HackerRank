#https://www.hackerrank.com/challenges/compare-the-triplets

alice = [int(i) for i in input().strip().split(' ')]
bob = [int(i) for i in input().strip().split(' ')]

a = 0
b = 0

for i in range(len(alice)):
    if alice[i] > bob[i]:
        a += 1
    elif alice[i] < bob[i]:
        b += 1
        
print(a,b)