#https://www.hackerrank.com/challenges/append-and-delete

s = input().strip()
t = input().strip()
k = int(input().strip())


len_s = len(s)
len_t = len(t)
max_len = max(len_s, len_t)

to_remove = 0
for i in range(len_s):
    # Get the character in the starting word
    ss = s[i]    
    # Get the character in the target word if there is any
    tt = None
    if i < len_t:
        tt = t[i]
    # Compare the characters
    if ss != tt:
        to_remove = max_len - i # All letters at and beyond this point will need to be removed
        break

to_add = len_t - (len_s - to_remove)

remainder = k - (to_remove + to_add)
if remainder == 0:
    print("Yes")
elif remainder > 0:
    if remainder%2 == 0: # If it's even, we can just append X characters and remove the same X characters
        print("Yes")
    else: # If there's an odd number as the remainder
        # If we can just delete the entire word and build it up,
        # then we can add as many extra deletes as we want before
        # building the new word. But this means that K must be
        # larger than the length of both words
        if k > len_s + len_t:
            print("Yes")
        else:
            print("No")
elif remainder < 0:
    print("No")