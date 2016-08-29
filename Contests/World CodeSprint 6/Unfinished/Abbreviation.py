queries = int(input())

for q in range(queries):
    a = input()
    b  = input()

    if a == b:
        print("YES")
    else:
        place = 0
        for c in a:
            if c.upper() == b[place]:
                place += 1
            if place == len(b):
                break
        if place == len(b):
            print("YES")
        else:
            print("NO")

#############
#Other Attempt

queries = int(input())

for q in range(queries):
    a = input()
    b  = input()

    if a == b:
        print("YES")
    else:
        a_dict = {}
        for c in a:
            c = c.upper()
            if c in a_dict:
                a_dict[c] += 1
            else:
                a_dict[c] = 1
        b_dict = {}
        for c in b:
            if c in b_dict:
                b_dict[c] += 1
            else:
                b_dict[c] = 1

        answer = "YES"
        for key in b_dict:
            if b_dict[key] > a_dict[key]:
                answer = "NO"
                break
        print(answer)
