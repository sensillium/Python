import tkinter
import random

window = tkinter.Tk()

window.title('')

door_to_guess = random.randint(0, 2)


def check_door(number):
    global door_to_guess
    if number == door_to_guess:
        lbl.configure(text='Yes')
    else:
        lbl.configure(text='No')


lbl = tkinter.Label(window, text='Which door contains the prize?')
lbl.pack()

for i in range(3):
    btn = tkinter.Button(text='Door ' + str(i), command=lambda door_no=i: check_door(door_no))
    btn.pack(side=tkinter.LEFT)

window.mainloop()