#https://www.hackerrank.com/challenges/lisa-workbook

temp = [int(i) for i in input().strip().split(' ')]
chapters = temp[0]
max_problems_per_page = temp[1]
problems = [int(i) for i in input().strip().split(' ')]

page = 1
special = 0
for i in range(1,len(problems)+1):
    for j in range(1,problems[i-1]+1):
        if j == page:
            special += 1
        if j < problems[i-1]: #if not the last problem in the chapter
            if j % max_problems_per_page == 0: #increment the page when the page is filled with problems
                page += 1
    page += 1 #increment the page after every chapter

print(special)
