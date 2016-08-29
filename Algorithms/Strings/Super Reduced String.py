#https://www.hackerrank.com/challenges/reduced-string

s = input()

s_list = list(s)

pair_found = True
while pair_found:
    pair_found = False
    for i in range(len(s_list)-1):
        if s_list[i] == s_list[i+1]:
            s_list.pop(i)
            s_list.pop(i)
            pair_found = True
            break

s_string = ''.join(s_list)
if len(s_string) > 0:
    print(s_string)
else:
    print("Empty String")
