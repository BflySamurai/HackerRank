#https://www.hackerrank.com/challenges/maximizing-xor

#!/usr/bin/python3
def maxXor(l, r):
    largest = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            xor = i ^ j
            if xor > largest:
                largest = xor
    return(largest)

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))