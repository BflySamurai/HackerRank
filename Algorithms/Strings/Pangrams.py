#https://www.hackerrank.com/challenges/pangrams

s = input().lower()

pangram = "pangram"
for i in range(ord("a"),ord("z")+1):
    if not chr(i) in s:
        pangram = "not pangram"
        break

print(pangram)
