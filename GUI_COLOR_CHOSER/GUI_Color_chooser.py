from tkinter import *
from tkinter import colorchooser

def click():
    window.config(background=colorchooser.askcolor()[1])

window = Tk()

window.geometry("400x400")
button = Button(window,
                text='click me',
                fg='green',
                bg='black',
                activebackground='black',
                activeforeground='green',
                command=click)

button.pack()
window.mainloop()