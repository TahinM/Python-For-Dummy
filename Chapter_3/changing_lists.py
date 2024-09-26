motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
'''
the motorcycle[0] basically replaces the first index with the new value. it would replace honda with ducati
'''
motorcycles[0] = 'ducati' 
print(motorcycles)

'''
the .append function adds something to the list at the end so its adding r35 to the end of the list of mortorcycles
'''
motorcycles.append('r35') 
print(motorcycles)

'''
this is a empty list that you add things too by using append. i added lambo gs300 and r35 to the empty list.
'''
cars = []
cars.append('lambo')
cars.append('gs300')
cars.append('r35')
print(cars)

'''
the insert function adds something new to the list that is already created. the 0 indicates the index which currently is lambo. 
lambo is then moved to the next index which is 1 and altima is put into index 0
'''
cars = ['lambo', 'gs300', 'r35']
cars.insert(0, 'altima') 
print(cars)

'''
the del function deletes an item from the list depending on the index that you input so i put 3 so it deleted r35
'''
del cars[3]
print(cars)

'''
the pop function is used to remove a item from the end of the list but it does delete it completely, you can still use 
the item that was removed. and to pop a specific item from the list and still use it you would specify what index 
'''
cars = ['lambo', 'gs300', 'r35', "chevy", "bmw"]
print(cars)
saved_cars = cars.pop()
print(cars)
print(saved_cars)

'''
the remove function removes a value if you do not know where it is in the list. bascially if you dont know the index number
so you remove it by the value
'''
cars = ['lambo', 'gs300', 'r35', "chevy", "bmw"]
too_expensive = "bmw"
car.remove = too_expensive
print(f"The {too_expensive} is out of my budget for me to own.")



