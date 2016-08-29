number_of_cities = int(input())
roads = []
opportunity_value = []
for i in range(number_of_cities-1):
    value = [int(i) for i in input().strip().split(' ')]
    roads.append(value)
    opportunity_value.append([value[0],value[1],0])
    
number_of_tickets = int(input())
tickets = []
for i in range(number_of_tickets):
    tickets.append([int(i) for i in input().strip().split(' ')])

print(roads)
print(opportunity_value)
print(tickets)

#find the highest profit we can make between any two cities

#assign an opportunity value to each potential road
for i in range(tickets):
    ticket = tickets[i]
    #adding the values to the opportunity map from the ticket costs based on whether the ticket would use that road
    #once all ticket values are added, subtract the cost of building the road to the opportunity value
    #start building a road using the largest value road as the start