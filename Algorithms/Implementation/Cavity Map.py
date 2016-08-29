#https://www.hackerrank.com/challenges/cavity-map

#!/bin/python3

import sys


n = int(input().strip())

grid = []
cavity_map = []
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(list(grid_t))
    cavity_map.append(list(grid_t))

for i in range(1,len(grid)-1):
    for j in range(1,n-1):
        if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
            cavity_map[i][j] = "X"

for i in range(len(cavity_map)):
    print("".join(cavity_map[i]))
