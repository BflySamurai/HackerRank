#https://www.hackerrank.com/contests/projecteuler/challenges/euler001

def fastSum(n):
    if n%2 == 0:
        return(int((n+1)*(n//2)))
    else:
        return((n+1)*(n//2)+int((n+1)/2))

test_cases = int(input())

for t in range(test_cases):
    n = int(input())
    m3 = (n-1)//3 # Has to be less than n
    m5 = (n-1)//5 # Has to be less than n
    m15 = (n-1)//15
    sum3 = fastSum(m3) * 3
    sum5 = fastSum(m5) * 5
    sum15 = fastSum(m15) * 15
    ans = sum3 + sum5 - sum15 # sum15 is to remove duplicates that we added for both sum3 and sum5
    print(ans)