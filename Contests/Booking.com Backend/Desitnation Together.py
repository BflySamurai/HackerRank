def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return(fact)


n,m,c = input().strip().split(' ')
n,m,c = [int(n),int(m),int(c)]

unique_john = n-c
unique_zizi = m-c
lviv = 1
cities = unique_john + unique_zizi + c - lviv
combinations = factorial(cities)
print(combinations)
