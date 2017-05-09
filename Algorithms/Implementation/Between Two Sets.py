#https://www.hackerrank.com/challenges/between-two-sets

def prime_factorization(n):
    i = 2
    factors = []
    nn = n
    while i <= n:
        while nn%i == 0: # If we can divide nn by this number
            nn = nn / i # Divide nn by this number
            factors.append(i) # Add the factor to the list
        if nn == 1:
            break
        i = i+1
    return(factors)

# http://www.math.com/school/subject1/lessons/S1U3L3DP.html
def least_common_multiple(arr):
    factor_map = {}
    for i in arr:
        factors = prime_factorization(i)
        
        # Build factor map for this number
        this_factor_map = {}
        for f in factors:
            if f in this_factor_map:
                this_factor_map[f] += 1
            else:
                this_factor_map[f] = 1
        
        # Add this factor map to the main factor map (only keep highest count for each factor)
        for key in this_factor_map:
            if key in factor_map:
                if this_factor_map[key] > factor_map[key]:
                    factor_map[key] = this_factor_map[key]
            else: # If it isn't yet in the factor map
                factor_map[key] = this_factor_map[key]
        
    # Build the least common multiple
    lcm = 1
    for key in factor_map:
        lcm *= pow(key, factor_map[key]) # Key is the number; factor_map[key] is the number of times it appears
    return(lcm)

def greatest_common_divisor(arr):
    arr.sort()
    divisible = False
    n = arr[0]
    divisor = n
    i = 1
    while not divisible:
        if n % i == 0:
            divisor = int(n/i)
            divisible = True
            for nn in arr:
                if nn % divisor != 0:
                    divisible = False
                    break
        else:
            divisible = False
        i += 1
        
    return(divisor)

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]


lcm = least_common_multiple(a)
gcd = greatest_common_divisor(b)

# Count the muliples of lcm that evenly divide into the gcd
check_range = int(gcd//lcm)
count = 0
for i in range(1,check_range+1):
    if gcd % (lcm*i) == 0:
        count += 1
        
print(count)