#https://www.hackerrank.com/challenges/alternating-characters

N = int(input())

for n in range(N):
    s = input()
    last_letter = s[0]
    deletions = 0
    for l in range(1,len(s)):
        current_letter = s[l]
        if current_letter == last_letter:
            deletions += 1
        else:
            last_letter = current_letter
    print(deletions)
