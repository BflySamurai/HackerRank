#https://www.hackerrank.com/challenges/making-anagrams

s1 = input()
s2 = input()

s1_dict = {}
for l in s1:
    if l in s1_dict:
        s1_dict[l] += 1
    else:
        s1_dict[l] = 1

s2_dict = {}
for l in s2:
    if l in s2_dict:
        s2_dict[l] += 1
    else:
        s2_dict[l] = 1

changes = 0
for key in s1_dict:
    if key in s2_dict:
        changes += abs(s1_dict[key] -s2_dict[key]) #get the differences of shared letters
    else:
        changes += s1_dict[key] #get the number of unique letters in the first string
for key in s2_dict:
    if not key in s1_dict:
        changes += s2_dict[key] #get the number of unique letters in the second string

print(changes)
