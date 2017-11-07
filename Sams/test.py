#!/usr/local/bin/python3.0
import sys

def testing(name, age):
    print("this one auto indented and everything")
    if name == 'richard':
        print ("you are awesome")
        if age >= 30:
            print ("good job")
        else:
            print ("snooze")
    else:
        print ("you are mediocre")

name = input('Enter your name: ')
age = int(input('Enter your age: '))

testing(name, age)