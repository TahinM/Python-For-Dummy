cities = ["nyc", "cali", "miami", "chicago", "dallas"]
len(cities)
cities.sort

message = "I would like to visit,"
print(f"{message}",cities[0].title(),cities[1].title(),cities[2].title(),cities[3].title(),cities[4].title())

print("But my favorite city is", cities[0].title())

cities.insert(0, 'columbus')
cities.append('tampa')
print(cities)
boring_cities = cities.pop(5)
print(boring_cities)
print(cities)

print("I also dont like",cities[2].title(),"so I won't go there.")
del cities[2]
print(cities)

print("I was already at", cities[2].title(), "so I will go somewhere else instead.")
cities.remove("miami")
print(cities)