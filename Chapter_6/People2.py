
people = [{'first_name': 'ullah', 'last_name': 'mo', 'age': 21 , 'city': 'Columbus'},
{'first_name': 'tahin', 'last_name': 'middin', 'age': 22 , 'city': 'NYC'},
{'first_name': 'anik', 'last_name': 'dawud', 'age': 22 , 'city': 'dallas'},
]
for individuals in people:
    full_name = f"\n{individuals['first_name'].title()} {individuals['last_name'].title()}"
    age = individuals['age']
    location = individuals['city'].title()
    print(f"{full_name} {age}, \n{location}")

