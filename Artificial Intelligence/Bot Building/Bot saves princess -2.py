#https://www.hackerrank.com/challenges/saveprincess2

#!/bin/python
def nextMove(n,r,c,grid):
    #get the coordinates of the princess
    for i in xrange(0,n):
        if "p" in grid[i]:
            princessY = i
            princessX = grid[i].index("p")
    #get the coordinates of the bot
    botY = r
    botX = c
    #get the vector from the bot to the princess
    vectorX = princessX - botX
    vectorY = princessY - botY
    #return the next move of the bot
    if vectorX < 0:
        return "LEFT"
    elif vectorX > 0:
        return "RIGHT"
    elif vectorY < 0:
        return "UP"
    elif vectorY > 0:
        return "DOWN"
    else:
        return ""

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)