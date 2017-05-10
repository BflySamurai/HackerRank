#https://www.hackerrank.com/challenges/icecream-parlor

trips = int(input())

for t in range(trips):
    money = int(input())
    n = int(input())
    flavors = [int(i) for i in input().strip().split(' ')]
    
    answer = ""
    for i in range(n):
        if answer != "":
            break
        for j in range(i+1, n):
            if flavors[i] + flavors[j] == money:
                answer = str(i+1) + " " + str(j+1)
                break
    print(answer)