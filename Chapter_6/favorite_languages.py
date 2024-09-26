favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

individuals = ['jen', 'tahin', 'anik', 'june', 'sarah', 'edward', 'phil']


for name in individuals:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for taking the poll!")
    elif name not in favorite_languages.keys():
        print(f"{name.title()}, you should take the language poll.")

