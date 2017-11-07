#!usr/local/bin/python
import time

class Now:
    def __init__(self):
        self.t=time.time()
        self.storetime()
    def storetime(self):
        self.year, \
        self.month, \
        self.day, \
        self.hour, \
        self.minute, \
        self.second, \
        self.dow, \
        self.doy, \
        self.dst=time.localtime(self.t)
    def __str__(self):
        return time.ctime(self.t)
    def __repr__(self):
        return time.ctime(self.t)
    def __call__(self,t=-1.0):
        if t<0.0:
            self.t=time.time()
        else:
            self.t=t
        self.storetime()

if __name__=="__main__":
    n=Now()
    print("The year is", n.year)
    print(n)
    x=Now()
    s=str(x)
    print(s)