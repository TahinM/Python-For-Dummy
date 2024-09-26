alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("You just earned 5 points!")
if 'blue' in alien_colors:
    print("You lost 5 points")

alien_look = 'red'
if alien_look == 'green':
    print("You just earned 5 points")
elif alien_look == 'yellow':
    print("You just earned 10 points")
else:
    print("You just earned 15 points")

individual_age = 64
if individual_age < 2:
    print("You are a baby!")
elif (individual_age >= 2) and (individual_age < 4):
    print("You are a toddler")
elif (individual_age >= 4) and (individual_age < 13):
    print("You are a kid")
elif (individual_age >= 13) and(individual_age < 20):
    print("You are a teenager")
elif (individual_age >= 20,) and (individual_age < 65):
    print("You are an adult")
else: 
    print("You are an elder.")

favorite_fruits = ['banana', 'watermelon', 'blueberries', 'strawberries', 'mangoes']
if 'banana' in favorite_fruits:
    print("HMMMM IM JAVANCE AND I LIKE BANANAS")
if 'watermelon' in favorite_fruits:
    print("l like watermelon")
if 'blueberries' in favorite_fruits:
    print(f"{favorite_fruits[2].title()}, is also good")
if 'strawberries' in favorite_fruits:
    print(f"{favorite_fruits[3].title()}, is also good")  
if 'mangoes' in favorite_fruits:
    print("Mangoes are the best")