import os
n = int(input("Enter a number: "))
for i in range(n):
    os.mkdir(str(i+1))