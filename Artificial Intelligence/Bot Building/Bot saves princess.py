#https://www.hackerrank.com/challenges/saveprincess

#!/bin/python
def displayPathtoPrincess(n,grid):
    for i in xrange(0,m):
        #get the coordinates of the princess
        if "p" in grid[i]:
            princessY = i
            princessX = grid[i].index("p")
        #get the coordinates of the bot
        if "m" in grid[i]:
            botY = i
            botX = grid[i].index("m")
    #get the vector from the bot to the princess
    vectorX = princessX - botX
    vectorY = princessY - botY
    
    #Move the bot horizontally
    for i in xrange(0,abs(vectorX)):
        if vectorX < 0:
            print("LEFT")
        else:
            print("RIGHT")
    
    #move the bot vertically
    for i in xrange(0,abs(vectorY)):
        if vectorY < 0:
            print("UP")
        else:
            print("DOWN")

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
