#https://www.hackerrank.com/challenges/chocolate-feast

#!/bin/python3

import sys


trips = int(input().strip())
for t in range(trips):
    dollars,chocolate_cost,trade_in = input().strip().split(' ')
    dollars,chocolate_cost,trade_in = [int(dollars),int(chocolate_cost),int(trade_in)]

    bars = 0
    bars_total = 0
    wrappers = 0
    while dollars >= chocolate_cost or wrappers >= trade_in:
        #convert wrappers to bars
        if wrappers >= trade_in:
            bars += wrappers//trade_in
            wrappers = wrappers%trade_in
            bars_total += bars
        #convert dollars to bars
        if dollars >= chocolate_cost:
            bars += dollars//chocolate_cost
            dollars = dollars%chocolate_cost
            bars_total += bars
        #convert chocolates to wrappers
        wrappers += bars
        bars = 0
    print(bars_total)
