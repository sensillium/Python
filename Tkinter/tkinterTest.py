import tkinter

window = tkinter.Tk()

window.title("Colours")

colours = ['red', 'yellow', 'pink', 'green', 'orange', 'purple', 'blue']

for c in colours:
    b = tkinter.Button(text=c, bg=c)
    b.pack(fill=tkinter.X)

window.mainloop()