import random

print("welcome to password generator")


char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

number = int(input("enter the number of passwords to be generated : "))

length = int(input("enter password length : "))

print("here are your passwords:")

for pwd in range(number):

    passwords= " "

    for c in range(length):

        passwords += random.choice(char)

    
    print(passwords)
