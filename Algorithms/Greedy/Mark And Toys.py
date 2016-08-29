#https://www.hackerrank.com/challenges/mark-and-toys

toys,money = input().strip().split(" ")
toys,money = [int(toys),int(money)]
costs = [int(c) for c in input().strip().split(' ')]
costs.sort()

total = 0
toys = 0
for i in costs:
    total += i
    if total <= money:
        toys += 1
    else:
        break

print(toys)
