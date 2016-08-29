#https://www.hackerrank.com/challenges/restaurant

def greatest_common_divisor(n1,n2):
    if n1 < n2:
        smallest = n1
    else:
        smallest = n2
    for i in range(smallest):
        n = smallest-i
        if n1%n == 0 and n2%n == 0:
            return(n)
        
        

n = int(input())
arr = [[int(i) for i in input().strip().split(' ')] for j in range(n)]

for i in range(n):
    length = arr[i][0]
    height = arr[i][1]
    gcd = (greatest_common_divisor(length,height))
    square = gcd*gcd
    rectangle = length*height
    square_count = int(rectangle/square)
    print(square_count)