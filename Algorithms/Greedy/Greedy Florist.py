#https://www.hackerrank.com/challenges/greedy-florist

flowers_needed,group_size = input().strip().split(" ")
flowers_needed,group_size = [int(flowers_needed),int(group_size)]
flower_costs = [int(c) for c in input().strip().split(' ')]
flower_costs.sort(reverse = True) #so we can buy the most expensive ones first

total_cost = 0
h = 0
i = 0
while i < flowers_needed:
    price_multiplier = (h+1)
    for j in range(group_size):
        total_cost += flower_costs[i] * price_multiplier
        i += 1
        if i >= flowers_needed:
            break
    h += 1

print(total_cost)
