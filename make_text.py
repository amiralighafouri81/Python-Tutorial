import os
name = input("Enter a name: ")
filepath = os.path.join(os.getcwd(), "text.txt")
with open(filepath, 'w') as file:
    file.write(name)