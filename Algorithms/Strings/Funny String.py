#https://www.hackerrank.com/challenges/funny-string

n = int(input())

for a in range(n):
    s = input()
    r = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(r[i])-ord(r[i-1])):
            print("Not Funny")
            break
        elif i == len(s)-1:
            print("Funny")
