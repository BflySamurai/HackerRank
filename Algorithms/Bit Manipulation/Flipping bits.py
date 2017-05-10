#https://www.hackerrank.com/challenges/flipping-bits

list_size = int(input())

for n in range(list_size):
    base_ten_number = int(input())
    binary_number = bin(base_ten_number)[2:].zfill(32) # Coverts to a binary string that is 32 bits
    flipped_binary_number = ""
    for digit in binary_number:
        flipped_binary_number += str(1-int(digit))
    flipped_base_ten_number = int(flipped_binary_number, 2)
    print(flipped_base_ten_number)