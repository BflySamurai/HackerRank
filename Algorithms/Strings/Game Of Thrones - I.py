#https://www.hackerrank.com/challenges/game-of-thrones

s = input()

even = False
if len(s)%2 == 0:
    even = True

#create dictionary counting the number of occurences of each letter
s_dict = {}
for i in range(len(s)):
    if s[i] in s_dict:
        s_dict[s[i]] += 1
    else:
        s_dict[s[i]] = 1

odd_letters = 0
for key in s_dict:
    if not s_dict[key]%2 == 0:
        odd_letters += 1

if even:
    if odd_letters <= 0:
        print("YES")
    else:
        print("NO")
else:
    if odd_letters <= 1:
        print("YES")
    else:
        print("NO")
