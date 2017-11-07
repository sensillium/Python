#!/usr/local/bin/python
import sys
import string

def julian_leap(y=2000):
    if (y%4) ==0:
        return 1
    return 0

def gregorian_leap(y=2000):
    if (y%400)==0:
        return 1
    elif (y%100)==0:
        return 0
    elif (y%4)==0:
        return 1
    return 0

years=[1999,2000,2001,1900]
print (julian_leap())
print (gregorian_leap())

if julian_leap():
    print ("Julian 2000 yes")
if gregorian_leap():
    print("Gregorian 2000 yes")

for x in years:
    if julian_leap(x):
        print ("Julian", x, "is leap")
    else:
        print ("Julian", x, "is not leap")
    if gregorian_leap(x):
        print ("Gregorian", x, "is leap")
    else:
        print ("Gregorian", x, "is not leap")