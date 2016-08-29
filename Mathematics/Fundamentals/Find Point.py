#https://www.hackerrank.com/challenges/find-point

n = int(input())
arr = [[int(i) for i in input().strip().split(' ')] for j in range(n)]

for i in range(n):
    points = arr[i]
    px = points[0]
    py = points[1]
    qx = points[2]
    qy = points[3]
    xdiff = qx - px
    ydiff = qy - py
    sx = qx + xdiff
    sy = qy + ydiff
    print(sx,sy)