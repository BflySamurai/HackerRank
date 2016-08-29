def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return(factorial)

s = input()

dict_letters = {}
for i in range(len(s)):
    letter = s[i]
    if letter in dict_letters:
        dict_letters[letter] += 1
    else:
        dict_letters[letter] = 1

places = 0
for key in dict_letters:
    if dict_letters[key] > 1:
        places += dict_letters[key]

blocks = 4
#places choose blocks
tuples = int(factorial(places)/(factorial(blocks)*factorial(places-blocks)))

print(tuples % (pow(10,9)+7))

'''First version:
s = input()

tuples = 0
length = len(s)
for a in range(length-3):
    for b in range(a+1,length-2):
        for c in range(b+1,length-1):
            if s[b] == s[c]:
                for d in range(c+1,length):
                    if s[a] == s[d]:
                        tuples += 1

print(tuples)
'''
