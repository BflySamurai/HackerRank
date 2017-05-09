#https://www.hackerrank.com/challenges/mini-max-sum

numbers = [int(i) for i in input().strip().split(' ')]

total_sum = sum(numbers)
largest_number = max(numbers)
smallest_number = min(numbers)

largest_sum = total_sum - smallest_number
smallest_sum = total_sum - largest_number

print(smallest_sum, largest_sum)