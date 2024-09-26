pizzas = ["chesse pie", "chicken pizza", "veggie pizza"]
friends_pizza = pizzas[:]
pizzas.append("beef pizza")
friends_pizza.insert(0,"pineapple pizza")

print("My favorite pizzas are:")
for my_favorite in pizzas:
    print(my_favorite)

print("My friends favorite pizzas are:")
for friends_favorite in friends_pizza:
    print(friends_favorite)

my_foods = ['pizza', 'falafel', 'carrot cake'] 
for my_choices in my_foods:
    print(my_choices)
friend_foods = my_foods[:]
for my_friend in friend_foods:
    print(my_friend)
