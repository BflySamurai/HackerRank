#https://www.hackerrank.com/challenges/acm-icpc-team

#!/bin/python3

import sys


n,topics = input().strip().split(' ')
n,topics = [int(n),int(topics)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(int(topic_t, 2))

maximum = 0
teams = 0
length = len(topic)
for i in range(length-1):
    for j in range(i+1,length):
        bits = topic[i] | topic[j]
        count = bin(bits).count("1")
        if count > maximum:
            maximum = count
            teams = 1
        elif count == maximum:
            teams += 1

print(maximum)
print(teams)
