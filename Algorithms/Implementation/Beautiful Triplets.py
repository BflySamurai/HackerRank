#https://www.hackerrank.com/challenges/beautiful-triplets

n,d = input().strip().split(' ')
n,d = [int(n),int(d)]
numbers = [int(numbers_temp) for numbers_temp in input().strip().split(' ')]

beautiful_triplets = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        if numbers[j] > numbers[i] + d:
            break
        if numbers[j] == numbers[i] + d:
            for k in range(j+1,n):
                if numbers[k] > numbers[j] + d:
                    break
                if numbers[k] == numbers[j] + d:
                    beautiful_triplets += 1
print(beautiful_triplets)
