#https://www.hackerrank.com/challenges/non-divisible-subset

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
arr = [int(a_temp) for a_temp in input().strip().split(' ')]

#Create a list of numbers equal to the remainder (i/k) for each value (i) in the original number list
remainders = []
remainder_list = []
for i in range(n):
    a = arr[i]
    remainders.append(a%k)
    if not a%k in remainder_list:
        remainder_list.append(a%k)

size = 0
for i in range(len(remainder_list)):
    subset_remainders = [remainder_list[i]] #goes through all of the different remainders one by one to make sure we find the biggest subset
    subset_size = 1
    for j in range(len(remainders)):
        if not i == j: #skip the one we already added
            if remainders[j] in subset_remainders: #if this remainder is already in the remainder list
                subset_size += 1 #increase the subset size, because that remainder is compatible
            else:
                compatible = True
                for ii in range(len(remainder_list)): #if this remainder doesn't work with any of the remainders in the list
                    if remainders[j] + remainder_list[ii] == k:
                        compatible = False
                if compatible:
                    subset_size += 1
                    subset_remainders.append(remainders[j])
    if subset_size > size:
        size = subset_size

print(size)
