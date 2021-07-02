
# Make strong password

import string
import random


while True:
    length = int(input("Enter your preferred password length: "))
    char = string.ascii_letters + string.digits + "!@#$%^&()_=-*/+"
    password = ''.join([random.choice(char) for i in range(length)])
    print(password)

    while True:
        answer = input("Do you want another password: (Y/N) ")
        if(answer.lower() == "y" or answer.lower() == "n"):
            break
    if (answer.lower() == "y"):
        break
