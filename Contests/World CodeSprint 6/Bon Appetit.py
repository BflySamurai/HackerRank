n,k = input().strip().split()
n,k = [int(n),int(k)]
item_costs = [int(i) for i in input().strip().split()]
charged = int(input())

cost = 0
for item in range(len(item_costs)):
    if not item == k:
        cost += item_costs[item]
shared = int(cost/2)
if charged == shared:
    print("Bon Appetit")
else:
    print(charged-shared)
