riders = input("What is your age? ")
age = int(riders)

if age <= 3:
    print("You're ticket is free!")
elif age >= 3 and age <= 12:
    print("You ticket price is $10.")
else:
    print("You're ticket price is $15.")
