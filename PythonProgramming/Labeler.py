'''
Created on 28 Feb 2014

@author: richard.m
'''
# Labeller

from Tkinter import *

# create the root window
root=Tk()
root.title("Labeller")
root.geometry("200x50")

# create a frame window to hold other widgets
app=Frame(root)

app.grid()

# create a label in the frame
lbl=Label(app, test="I'm a label!")

lbl.grid()

# kick off the window's event loop
root.mainloop()