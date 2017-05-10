#https://www.hackerrank.com/challenges/luck-balance

contests,max_lost = input().strip().split(' ')
contests,max_lost = [int(contests),int(max_lost)]

important_contests = []
unimportant_contests = []
for n in range(contests):
    luck,important = input().strip().split(' ')
    luck,important = [int(luck),int(important)]
    if important: # If the contest is important
        important_contests.append(luck)
    else: # If the contest is not important
        unimportant_contests.append(luck)

important_contests.sort(reverse = True) # Sort so that we can remove the maximum number of important contests (max_lost)
important_contests_won = important_contests[max_lost:]
important_contests_lost = important_contests[:max_lost]

max_luck = sum(important_contests_lost) + sum(unimportant_contests) - sum(important_contests_won)
print(max_luck)