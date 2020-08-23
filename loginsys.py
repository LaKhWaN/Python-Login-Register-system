# Login and Register System:

import random

passlen = 3  # This will make more harder to crack the code.


# Register System :

def register():
    print("You aren't registered!")
    file = open("users.txt", "a")
    user = input("Please enter your username here: ")
    file.write("\n" + user)
    file.close()
    file2 = open("C:/Users/LaKhWaN/Documents/My Project/Database/" + user + ".txt", "w")
    while True:
        password = input("Please enter your desired password here: ")
        if len(password) < 3:
            print("Password is too short please try again!")
        elif len(password) > 26:
            print("Password is too long please try again!")
        else:
            break
    choice = "abcdefghijklmnopqrstuvwxy1234567890!@~#$%^&*()-_=+"
    list1 = list(password)
    length = len(list1)
    new_pass = ""
    for i in range(length):
        new_pass += list1[i]
        for h in range(passlen):
            new_pass += random.choice(choice)
    file2.write("Password: " + new_pass)
    print("You have been registered successfully!")


# Login system:

def login():
    print("You are already registered!")
    file = open("C:/Users/LaKhWaN/Documents/My Project/Database/" + user + ".txt", "r")
    data = file.readline()
    data2 = data.split()
    unhash_pass = ""
    list3 = list(data2[1])
    length1 = len(list3)
    for i in range(0, length1, passlen + 1):
        unhash_pass += list3[i]
    while True:
        password = input("Please enter your password here: ")
        if password == unhash_pass:
            print("You have been logged in successfully!")
            break
        else:
            print("You have entered wrong password!")


# Starter Code:

print("Welcome to LaKhWaN's Project")
user = input("Please enter your username here: ")
file = open("users.txt", "r")
data = file.read()
if user in data:
    login()
else:
    register()
