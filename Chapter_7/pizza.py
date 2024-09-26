toppings = []
while True:
    pizza = input("\nWhat toppings would you like on your pizza? Enter 'quit' when you are done.")
    if pizza == "quit":
        break  
    print('\n',pizza)
    toppings.append(pizza)

print("You're pizza with the", *toppings, "toppings will be made shortly!")