
person_1 = {'animal': 'dog', 'owner': 'ullah'}
person_2 = {'animal': 'cat', 'owner': 'tahin'}
person_3 = {'animal': 'bird', 'owner': 'anik'}

pets = [person_1, person_2, person_3]
for people in pets:
    if people == person_1:
        print (f"{people['animal']+"s"}, are playful")
    elif people == person_2:
        print (f"{people['animal']+"s"}, are calm")
    elif people == person_3:
        print((f"{people['animal']+"s"}, can fly"))
