#https://www.hackerrank.com/challenges/botcleanr

#!/usr/bin/python

# Head ends here
def next_move(row, col, dirty):
    if ((row, col)) in dirty:
        print("CLEAN")
    else:
        target = find_closest_dirty(row, col, dirty)

        if row < target[0]:
            print("DOWN")
        elif row > target[0]:
            print("UP")
        elif col < target[1]:
            print("RIGHT")
        elif col > target[1]:
            print("LEFT")

def get_dirty_tiles(board):
    dirty_tiles = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "d":
                dirty_tiles.append((row, col))
    return dirty_tiles

def find_closest_dirty(row, col, dirty):
    shortest_distance = -1
    for i in range(len(dirty)):
        tile = dirty[i]
        tilerow = tile[0]
        tilecol = tile[1]
        distance = abs(row-tilerow) + abs(col-tilecol)
        if shortest_distance == -1:
            closest = tile
            shortest_distance = distance
        elif distance < shortest_distance:
            closest = tile
            shortest_distance = distance
    return closest

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    dirty = get_dirty_tiles(board)
    next_move(pos[0], pos[1], dirty)
