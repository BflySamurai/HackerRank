initial_state = [int(i) for i in input().strip().split()]
target_state = [int(i) for i in input().strip().split()]

total_moves = 0
for n in range(len(initial_state)):
    i = initial_state[n]
    t = target_state[n]
    move_1 = abs(i-t)
    move_2 = abs(i - (t+10))
    move_3 = abs(i - (t-10))
    total_moves += min([move_1, move_2, move_3])

print(total_moves)
