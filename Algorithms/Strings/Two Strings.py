#https://www.hackerrank.com/challenges/two-strings

test_cases = int(input())

for t in range(test_cases):
    a = input()
    b = input()
    found_pair = "NO"
    for l in a:
        if l in b:
            found_pair = "YES"
            break
        if found_pair == "YES":
            break
    print(found_pair)
