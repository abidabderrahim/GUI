from tkinter import *

window = Tk()

window.geometry("300x300")
frame = Frame(window,bg='black',bd=5,relief=RAISED)
#frame.pack(side=BOTTOM)
frame.place(x=0,y=0) # fix in x and y .

button = Button(frame,
                text="W",
                font=('Consolas', 25),
                width=3).pack(side=TOP)
button = Button(frame,
                text="A",
                font=('Consolas', 25),
                width=3).pack(side=LEFT)
button = Button(frame,
                text="S",
                font=('Consolas', 25),
                width=3).pack(side=LEFT)
button = Button(frame,
                text="D",
                font=('Consolas', 25),
                width=3).pack(side=LEFT)              

window.mainloop()