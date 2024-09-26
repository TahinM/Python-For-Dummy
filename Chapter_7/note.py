'''

finished_sandwiches.append(question) 
    print("\nYou're sandwiches are: ")
    print(*finished_sandwiches, sep= ',')
    while True:
        if question_2 == 'yes':
           continue
        elif question_2 != 'yes':
            print("We have finished making your" *finished_sandwiches)
            print("\nEnjoy you meal!")
        else:
            False
'''

'''
print(f"Here are the sandwiches avaiable:", *sandwich_orders, sep= ', ')
question = input("What sandwich would you like?: ")


question_3 = input("Would you want one more? yes/no: ")

sandwich_orders = True
while True:
    if question_3 == 'yes':
        print(question)
        
    elif question_3 != 'yes':
        print("We have finished making your", *finished_sandwiches)
        
    else:
        False

'''