#!/usr/bin/python3

travel_log = [
{
    "country": "france",
    "visits": 12,
    "cities": ["Paris", "lille", "dijon"]
},

{
    "country": "germany",
    "visits": 5,
    "cities": ["berlin", "hamburg", "stuttgart"]
},
]

def add_new_country(country_visited, no_of_visits, cities_visited):
    new_country = {}

    new_country["country"] = country_visited
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities_visited
    
    travel_log.append(new_country)

add_new_country("russia", 2, ["moscow", "saint peterburg"])
print(travel_log)
