#https://www.hackerrank.com/challenges/red-john-is-back

# There is a wall of size 4xN. There is an infinite supply of bricks of size 4x1 and 1x4. The wall has to be completely covered using the bricks. What is the total number of ways (M) in which the bricks can be arranged for any given N. Find the number of primes in M.

def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return(factorial)

def find_primes(n):
    if n < 2:
        primes = []
        return(primes)
    if n == 2:
        primes = [2]
        return(primes)
    primes = [2,3]
    for i in range(4,n+1):
        for j in range(len(primes)):
            if primes[j] > pow(i,0.5): #don't check numbers higher than the square root
                primes.append(i) #if it does get to this point and hasn't found any factors, add the number to the primes list
                break
            elif i % primes[j] == 0:
                break

    return(primes)

lines = int(input())
numbers = []
for i in range(lines):
    n = int(input())
    horizontal_blocks = n//4
    
    #calculate how many ways we can fit a given number of blocks in a given number of places
    combinations = 1 #starts at one to count having all of the blocks vertial
    for blocks in range(1,horizontal_blocks+1): #Go through all the combinations with different amounts of horizontal blocks
        #convert each block of 4 into one block. To do this, we would subtract blocks*4 from n, however, we would need to also add back blocks to n since are only converting those 4 blocks into one slot instead of taking them out. Instead, we'll just do n - blocks*3
        places = n - blocks*3 #number of places we can put blocks
        if places == 0:
            combinations += 1 #if the entire grid is horizontal blocks
        else:
            combinations += int(factorial(places)/(factorial(blocks)*factorial(places-blocks)))
        
    primes = find_primes(combinations)
    print(len(primes))