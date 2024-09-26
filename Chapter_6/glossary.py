glossary = { 
    'in': "'In' is used in a list to see if the value is in the list or not\n",
    'get': "'Get' is used to retrieve a value in a dictionary if the value is not there. \nYou specify the key as the first argument then you specify the value as the second argument.\n",
    'insert': "'Insert' is used to put a value in a list. You specify its index as well\n",
    'append': "'Append' is used to add a value to the end of the list\n",
    'if statements': "'If statments' is used as conditional tests to see if something is true or false\n",
    'set': "'Set' is a collection whihc are unique, there will be no repetitions\n",
    'tuple': "'Tuple' is like a list but it cant be changed at all. You use parenthese to define tuples\n",
    'slice': "'Slice' is used to only get a specific segment of a list. Not the whole list.\n",
    'range': "'Range' is used in a for loop and you can define a set of range from 1-6. But it will\nonly print out numbers 1-5.\n",
    'variables': "'Variables' are like containers that hold the value.\n",
    }
for terms, value in glossary.items():
    print(f"\n{terms.title()}- {value}")


print("these are the terms:")
for terms in glossary.keys():
    print(terms.title())
print("\n")
print("these are the values:")
for value in glossary.values():
    print(value)





