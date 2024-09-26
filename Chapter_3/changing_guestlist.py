names = ['june', 'anik', 'javance']

message = "Hey you are invited to the party"
print(message, names[0].title())
print(message, names[1].title())
print(message, names[2].title())

popped_names = names.pop(2).title()

print(f"{popped_names} cannot make it to the party")

names.insert(0, "ullah")
print(f"{names[0].title()} is invited to the party now!")
len(names)

names.insert(2, 'navi')
names.insert(3, 'yosuf')
names.append('happy')
print(names)
print(message, names[2].title())
print(message, names[3].title())
print(message, names[4].title())


print("I can only invite two people for the party thats it, sorry!")
popped_names = names.pop(5)
popped_names = names.pop(4)
popped_names = names.pop(3)
popped_names = names.pop(2)
print(names)

message = "You guys are still invited!"
print(message, names[0].title(),"and", names[1].title(),'.')

del names[0]
#del names[1]
print(names)


