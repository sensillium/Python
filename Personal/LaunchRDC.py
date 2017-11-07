# $ Author: Richard.m $
# $ Date: $
# $ Revision: $

# allow user to choose whether or not the /multimon is used
# allow user to specify a target PC

# imports
from os import system


def main():
    mm = raw_input("Do you want to use a multimonitor client? [y/n]: ")
    name = raw_input("Do you have a target computer name: ")

    if mm.lower() != "y" and name.lower() == "":
        system("mstsc.exe")
    elif mm.lower() == "y" and name.lower() == "":
        system("mstsc.exe /multimon")
    elif mm.lower != "y" and name.lower() != "":
        system("mstsc.exe /v:{0}".format(name.lower()))
    elif mm.lower() == "y" and name.lower() != "":
        system("mstsc.exe /v:{0} /multimon".format(name.lower()))
    else:
        print "Invalid input detected, please try again."
        main()

if __name__ == "__main__":
    main()

