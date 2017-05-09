#https://www.hackerrank.com/challenges/counting-valleys

n = int(input())
hike = input()

elevation = 0
valleys = 0
for l in hike:
    if l == "U":
        elevation += 1
    else: # If l == "D"
        if elevation == 0: # If he is at sea level and heading down, this is the start of a valley
            valleys += 1
        elevation -= 1

print(valleys)