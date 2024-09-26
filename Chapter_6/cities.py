cities = {
    'nyc':{
        'country': 'USA',
        'population': 100,
        'fact': 'Very diverse',
    },
    'dallas':{
        'country': 'USA',
        'population': 200,
        'fact': 'Lots of Steak',
    },
    'columbus':{
        'country': 'USA',
        'population': 300,
        'fact': 'Home for Cowboy'
    },
}


for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country']},\nPopulation: {info['population']},\nFact: {info['fact']}")