from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()
window.geometry('400x400')
window.config(background='black')

window.bind('<w>',move_up)
window.bind('<s>',move_down)
window.bind('<a>',move_left)
window.bind('<d>',move_right)

window.bind('<Up>',move_up)
window.bind('<Down>',move_down)
window.bind('<Left>',move_left)
window.bind('<Right>',move_right)

photo = PhotoImage(file='4518857_python_icon.png')
label = Label(window,
              foreground='green',
              background='black',
              image=photo)
label.place(x=0,y=0)

window.mainloop()