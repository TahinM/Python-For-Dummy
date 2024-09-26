dinner_group = input("How can individuals are in your group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print("Sorry you are going to have a wait for a bit.")
elif dinner_group <= 8:
    print("Ok we have seatings for you guys!")

