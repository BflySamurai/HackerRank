#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

def reverse_num(n):
    return(int(str(n)[::-1])) # Turn number into string, reverse it, turn it back into an int, and then return it
    

i, j, k = input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]

days = 0
for d in range(i, j+1):
    diff = abs(d - reverse_num(d))
    if diff % k == 0:
        days += 1

print(days)