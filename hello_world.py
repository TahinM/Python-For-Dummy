print("Hello World!")

def add(a, b):
    return a + b

a = 5
b = 20000000
print(add(a,b))






'''
the "f" in front of the brackets symblozies that it is a f- string. F stands for formant 
so python automatically formats the string of any variable with its recepected values. 
So first name would be changed to tahin and last name would be changed ot middin
the full_name.title() just made it that it prints out professionally and it looks good. 
'''
first_name = "tahin"
last_name = "middin"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

'''
the \t is used to adding a space so when it prints its already spaced or indented out
'''
print("\tPython")

'''
the \n is used to add a new line and print everything out on the new line below.
'''
print("Languages:\n\tPython\n\tC\n\tJavaScript")
