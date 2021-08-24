# Password Generator
# Made by: Zuhair H. Khan
# Date: 2021-02-10
# Purpose: To generate a random password

# import statement
from random import randrange

# input statement
size = int(input('Enter the size of your password: '))

# variable declaration
pwd = "" # this is an empty string

# processing / creating the password

while len(pwd) != size:
    # generate random character
    randomChar = chr(randrange(33, 127)) #will choose a random number from [a,b)

    # check if character was used before
    if randomChar not in pwd:
        pwd += randomChar
    else:
        print('This character has been used before.')
    # enf if
# end of while

# output
print('The generated password:', pwd)
