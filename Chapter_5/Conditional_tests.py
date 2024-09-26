car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
'''
This is testing for simply true or false, i messed around and also noticed things about nested loops. 
pho is not in food so it skipped and when to beef, beef is in food so it printed out the print statement 
but since there was a nested loop it contiued the if statement and tested the loop statement and it printed out
the next print statement because noodles was in food, otherwise it would have ended the if statement at beef. 
'''
food = ['chicken', 'beef', 'shrimp', 'noodles']
if 'pho' in food:
    print("I love chicken so much!")
elif 'beef' in food:
    print("i only want chicken.")
    if 'noodles' in food:
        print("I can probably do noodles as well")
else:
    print("im not hungry anymore.")

'''
this is checking for inequality
'''
places_tovisit = ['canada', 'cali', 'tokyo']
if places_tovisit != 'NYC':
    print("\n")
    print("That is not a place I want to go")

'''
this is checking for equality
'''
car = 'BMW'
print("\n")
print(f"the car is: ",car.lower()== 'bmw')


"numerical values using greater than, less than signs"
age_0 = 25
age_1 = 26
age_0 > 30
age_1 < 30
print(age_0 > 30, age_1 < 30)

age_0 = 25
age_1 = 26
print(age_0 >= 30, age_1 <= 30)


weather = 'sunny'
temperature = 'chilly'
if (weather =='sunny') and (temperature == 'chilly'):
    print("Today is a beautiful day")
elif weather == 'sunny' and temperature == 'cold':
    print("I dont like today")


def check_in_boat(choices):
    if choices in boats:
        print (f"yes we do have {choices}")
    else:
        print(f"sorry {choices} is not avaiable")

boats = ['steering wheel', 'roof', 'cabin', 'leather']
check_in_boat('leather')
check_in_boat('cabin')


boats = ['steering wheel', 'roof', 'cabin', 'leather', 'lights']
print('lights' in boats)
print('bed' not in boats)


