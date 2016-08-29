#!/usr/bin/python
import math

pi = 3.14159265

def degrees2radians(degree):
    return(degree*pi/180)

def distance_between(point1_lat, point1_lon, point2_lat, point2_lon):
    EARTH_RADIUS = 6371 #in km
    point1_lat_in_radians = degrees2radians(point1_lat)
    point2_lat_in_radians = degrees2radians(point2_lat)
    point1_long_in_radians = degrees2radians(point1_lon)
    point2_long_in_radians = degrees2radians(point2_lon)

    return (math.acos( math.sin( point1_lat_in_radians ) * math.sin( point2_lat_in_radians ) +
                 math.cos( point1_lat_in_radians ) * math.cos( point2_lat_in_radians ) *
                 math.cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS)


guest_count = int(input())
guests = []
for g in range(guest_count):
    guest = input().split(" ")
    guests.append(guest)

destination_count = int(input())
destinations = []
for d in range(destination_count):
    destination = input().split(" ")
    destinations.append(destination)


print(distance_between(0,0,0,400))

print(guests)
print(destinations)
