'''
Created on 11 Feb 2014

@author: richard.m
'''

# Alien Blaster
# Demonstrates object interaction

class Player(object):
    """A player in a shooter game"""
    def blast(self, enemy):
        print "The player blasts an enemy.\n"
        enemy.die()
        
class Alien(object):
    """An alien in a shooter game"""
    def die(self):
        print"The alien dies, a horrible horrible death, possibly involving a skidoo.\n"

# main
print "\t\tDeath of an Aldien"

hero=Player()
invader=Alien()
hero.blast(invader)

raw_input("\n\nPress the Enter key to quit")        