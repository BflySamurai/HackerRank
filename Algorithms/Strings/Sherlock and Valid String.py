#https://www.hackerrank.com/challenges/sherlock-and-valid-string

s = input()

letter_count = {}
for l in s:
    if l in letter_count:
        letter_count[l] += 1
    else:
        letter_count[l] = 1

letter_frequency = {}
for key in letter_count:
    frequency = letter_count[key]
    if frequency in letter_frequency:
        letter_frequency[frequency] += 1
    else:
        letter_frequency[frequency] = 1

length = len(letter_frequency)
if length > 2:
    print("NO")
elif length == 2:
    answer = "NO"
    for key in letter_frequency:
        if letter_frequency[key] == 1:
            answer = "YES"
    print(answer)
elif length == 1:
    print("YES")
