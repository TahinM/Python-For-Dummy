'''
 Deli: Make a list called sandwich_orders and fill it with the names of vari- ous sandwiches. 
 Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders 
 and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
 move it to the list of finished sandwiches. 
 After all the sandwiches have been made, print a message listing each sandwich that was made.
'''

sandwich_orders = ['Egg Sandwich', 'Seafood Sandwich', 'Roast Beef Sandwich', 'Grilled Cheese', 'Ham Sandwich',]
finished_sandwiches = []

for food in sandwich_orders:
    print(f"I have made your {food}.")
    finished_sandwiches.append(food)
print('\n')
print("Here are all the finished sandwiches:", *finished_sandwiches, sep= ',')






    




    
