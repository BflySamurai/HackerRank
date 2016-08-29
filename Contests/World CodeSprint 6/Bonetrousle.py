trips = int(input())

for t in range(trips):
    sticks_buy, boxes_sale, boxes_buy = input().strip().split()
    sticks_buy, boxes_sale, boxes_buy = [int(sticks_buy), int(boxes_sale), int(boxes_buy)]

    bought = []
    for i in range(boxes_buy):
        bought.append(i+1)

    difference = sticks_buy - sum(bought)
    div = difference // boxes_buy
    mod = difference % boxes_buy
    if div < 0:
        print(-1)
    elif sum(bought) > sticks_buy:
        print(-1)
    else:
        #create the smallest set of numbers that equals the target
        for i in range(len(bought)): #distribute evenly across all numbers
            bought[i] += div
        for i in range(1,mod+1): #distribute remainder evenly starting from the end to ensure no number is larger than the next
            bought[-i] += 1

        if bought[-1] > boxes_sale:
            print(-1)
        else:
            print(*bought)
