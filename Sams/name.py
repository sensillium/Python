#!usr/local/bin/python
import sys
import string
import leap2

if __name__=="__main__":
    if len(sys.argv)<2:
        print ("Usage:", sys.argv[0], "year year year...")
        sys.exit(1)
    else:
        for i in sys.argv[1:]:
            y=int(i)
            j=leap2.julian_leap(y)
            g=leap2.gregorian_leap(y)
            if j != 0:
                print (i, "is a leap year in the Julian calendar")
            else:
                print (i, "is not a leap year in the Julian calendar")
            if g != 0:
                print (i, "is a leap year in the Gregorian calendar")
            else:
                print (i, "is not a leap year in the Gregorian calendar")