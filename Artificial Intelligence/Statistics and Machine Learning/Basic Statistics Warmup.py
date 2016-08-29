#https://www.hackerrank.com/challenges/from-paragraphs-to-sentences

def mean(n,arr):
    mean = sum(arr)/n
    return(mean)
    
def median(n,arr):
    if n%2 == 0: #if even number of elements
        middle = int(n/2)
        median = (arr[middle-1] + arr[middle])/2 #get the average of the middle elements
    else: #if odd number of elements
        middle = (n/2) - 1
        median = arr[middle]
    return(median)

def mode(n,arr):
    dict_numbers = {}
    for i in range(n):
        number = arr[i]
        if number in dict_numbers:
            dict_numbers[number] += 1
        else:
            dict_numbers[number] = 1

    mode = 0
    frequency = 0
    for number in dict_numbers:
        if dict_numbers[number] == frequency: #collect the lowest number for each frequency
            if number < mode:
                mode = number
                frequency = dict_numbers[number]
        elif dict_numbers[number] > frequency: #otherwise, only look for numbers of higher frequency
            mode = number
            frequency = dict_numbers[number]
    return(mode)

def stdev(n,arr):
    m = mean(n,arr)
    sd = 0
    for i in range(n):
        sd += pow(arr[i]-m,2)
    sd = pow(sd/n,0.5)
    return(sd)

def conf_int(n,arr):
    m = mean(n,arr)
    std = stdev(n,arr)
    conf_int_low = m - (1.96 * std/pow(n,0.5))
    conf_int_high = m + (1.96 * std/pow(n,0.5))
    conf_int = [conf_int_low,conf_int_high]
    return(conf_int)

n = int(input())
arr = [int(i) for i in input().strip().split(' ')]
arr.sort()

print(mean(n,arr))
print(median(n,arr))
print(mode(n,arr))
print(stdev(n,arr))
conf_int = conf_int(n,arr)
print(conf_int[0],conf_int[1])