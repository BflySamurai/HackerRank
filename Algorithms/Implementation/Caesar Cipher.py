#https://www.hackerrank.com/challenges/caesar-cipher-1

#!/bin/python3

import sys


n = int(input().strip())
string = input().strip()
key = int(input().strip())

arr = list(string)

encrypted_arr = []
A = ord("A")
Z = ord("Z")
a = ord("a")
z = ord("z")

for i in range(len(arr)):
    char = arr[i]
    if A <= ord(char) <= Z: #if character is upper case letter
        new_char = chr(((ord(char) - A + key)%26)+A)
        encrypted_arr.append(new_char)
    elif a <= ord(char) <= z: #if character is lower case letter
        new_char = chr(((ord(char) - a + key)%26)+a)
        encrypted_arr.append(new_char)
    else: #if character is not a letter
        encrypted_arr.append(char)


encrypted_string = ''.join(encrypted_arr)
print(encrypted_string)
