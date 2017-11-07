'''
Created on 13 Feb 2014

@author: richard.m
'''

# Games
# Demostrates module creation

class Player(object):
    """A player for a game"""
    def __init__(self, name, score=0):
        self.name=name
        self.score=score
    
    def __str__(self):
        rep=self.name+":\t"+str(self.score)
        return rep
    
def ask_yes_no(question):
    """Ask a yes or no"""
    response=None
    while response not in ("y","n"):
        response=raw_input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number in a range"""
    response=None
    while response not in range(low, high):
        response=int(input(question))
    return response

if __name__=="__main__":
    print"You ran this module directly."
    raw_input("\n\nPress the enter key to exit")