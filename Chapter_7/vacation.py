'''
Dream Vacation: Write a program that polls users about their dream vaca- tion. Write a prompt similar to If you 
could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
'''

prompt = "If you had a place in mind to go and visit,"
print(prompt)
destinations = []

fun = True
while True:
    
    #ask the individual the question
    area = input("What place would you go?: ")
    destinations.append(area)
   
    #ask them is there any other places they would want to go?
    second_place = input("\nIs there any other place you would like to go? (yes/no) ")
    if second_place != 'yes':
        break
   

for places in destinations:
    print(f"You would like to visit: {places}")


    

