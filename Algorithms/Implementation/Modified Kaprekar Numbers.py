#https://www.hackerrank.com/challenges/kaprekar-numbers

low_bound = int(input())
high_bound = int(input())+1

kaprekars = []
for i in range(low_bound,high_bound):
    n = str(i)
    d = len(n)
    nn = str(i*i)
    dd = len(nn)
    if d == 1 and dd == 1: #if it's only one digit
        if n == nn:
            kaprekars.append(n)
    elif d == 1 and dd:
        if i == int(nn[:d]) + int(nn[d:]):
            kaprekars.append(n)
    elif dd%2 == 0: #if even number of digits
        if i == int(nn[:d]) + int(nn[d:]):
            kaprekars.append(n)
    else: #if odd number of digits
        if i == int(nn[:d-1]) + int(nn[d-1:]):
            kaprekars.append(n)

if len(kaprekars) > 0:
    print(" ".join(kaprekars))
else:
    print("INVALID RANGE")
