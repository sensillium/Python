#!usr/local/bin/python
import time
import now
import roman

class Today(roman.Roman, now.Now):
    def __init__(self, y=1970):
        now.Now.__init__(self)
        roman.Roman.__init__(self, y)
    def update(self,tt):
        if len(tt)<9:
            raise TypeError
        if tt[0] < 1970 or tt[0]>2038:
            raise OverflowError
        self.t=time.mktime(tt)
        self(self.t)
        roman.Roman.__init__(self, self.year)
if __name__=="__main__":
    n=Today()
    print "The year is", n.year
    print(n)
    x=Today()
    s=str(x)
    print(s)
    tt=(1999,7,16,12,59,59,0,0,-1)
    x.update(tt)
    print x, x.t
    print "Roman", x.ryear()
    st=`x`
    print (st)
    