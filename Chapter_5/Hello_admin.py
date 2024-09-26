usernames = ['june', 'anik', 'admin', 'tahin', 'ullah']
for names in usernames:
    if names == 'admin':
        print(f"Hello {names.title()} would you like to see your status today?")
    else:
        print(f"Hey!{names.title()} Thanks for logging in again today.")

users = []
if users:
    print("We finally have people!")
else:    
    print("We need to find some users")

current_usernames = ['June', 'Anik', 'javance', 'ullah', 'navi']
new_users = ['june', 'anik', 'tahin', 'bob', 'nick']
current_usernames_lower = [name.lower() for name in current_usernames]

for new_name in new_users:
    if new_name.lower() in current_usernames_lower:
        print(f"Sorry you cannot use, {new_name}")
    else:
        print("You can use that username")


ordinal_numbers = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]

for num in ordinal_numbers:
    if(num == 1):
        print(f"{num}" + 'st')
    elif(num == 2):
        print(str(num) + 'nd')
    elif(num == 3):
        print(f"{num}" + 'rd')
    else:
        print(f"{num}" + 'th')


    
  
       
