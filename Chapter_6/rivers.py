rivers = {'nile': 'egypt', 'amazon': 'peru', 'euphrates': 'turkey'}
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}")
print('\n')
for river in rivers.keys():
    print(river.title())
print('\n')
for country in rivers.values():
    print(country.title())