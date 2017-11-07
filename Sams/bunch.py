#!usr/local/bin/python
class bunch:
    def __init__(self):
        pass
    if __name__=="__main__":
        b=[]
        for i in range(0,25):
            b.append(bunch())
        print(b)