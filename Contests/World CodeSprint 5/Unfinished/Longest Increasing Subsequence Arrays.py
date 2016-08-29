def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return(factorial)

def choose(places,blocks):
    return(int(factorial(places)/(factorial(blocks)*factorial(places-blocks))))

p = int(input())

for i in range(p):
    m,n = input().strip().split(' ')
    m,n = [int(m),int(n)]
    #print(m,n)
    
    #unique ways of arranging the numbers up to n in the spaces m
    x = pow(n,m)
    
    #out of those arrangements, how many match one of the subsets
    a = choose(m,n)
    
    print(a,x)