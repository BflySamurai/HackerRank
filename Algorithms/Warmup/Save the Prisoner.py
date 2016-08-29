#https://www.hackerrank.com/challenges/save-the-prisoner

n = int(input())
for i in range(n):
    arr = [int(i) for i in input().strip().split(' ')]
    prisoners = arr[0]
    sweets = arr[1]
    id_start = arr[2]-1 #we do id_start-1 to give the first sweet to the id of the prisoner we're already on

    mod = sweets % prisoners
    if mod == 0:
        if sweets == id_start + sweets:
            poison = prisoners
        else:
            poison = id_start
    else:
        poison = id_start + mod 
        if poison > prisoners:
            poison -= prisoners

    print(poison)