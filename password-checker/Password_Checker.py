#!/usr/bin/env python3

username = input("Enter your username: ")
password = input("Enter your password: ")

while True:
    # password length should not be less than 8 chars
    if len(password) < 8:
        print("Password is too short!\n")
    # password should not contain username
    elif username in password:
        print("Password contains username!\n")
    else:
        print("Password for user {} set successfully".format(username))
        break
    password = input("Enter password once again: ")
