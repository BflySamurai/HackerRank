#https://www.hackerrank.com/challenges/lonely-integer

#!/usr/bin/py
# Head ends here
def lonelyinteger(n,arr):
    dict_numbers = {}
    for i in range(n):
        number = arr[i]
        if number in dict_numbers:
            dict_numbers[number] += 1
        else:
            dict_numbers[number] = 1
    
    for key in dict_numbers:
        if dict_numbers[key] == 1:
            return key
    
# Tail starts here
if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().strip().split(' ')]
    print(lonelyinteger(n,arr))
