from tkinter import *

def move_up(event):
    canvas.move(myimage, 0,-10)

def move_down(event):
    canvas.move(myimage, 0,+10)

def move_left(event):
    canvas.move(myimage, -10, 0)

def move_right(event):
    canvas.move(myimage, +10, 0)

window = Tk()
window.geometry('400x400')

window.bind('<w>',move_up)
window.bind('<s>',move_down)
window.bind('<a>',move_left)
window.bind('<d>',move_right)

window.bind('<Up>',move_up)
window.bind('<Down>',move_down)
window.bind('<Left>',move_left)
window.bind('<Right>',move_right)

photo = PhotoImage(file='4518857_python_icon.png')
canvas = Canvas(window, 
                width=400,
                height=400, 
                background='black')
myimage = canvas.create_image(0,0,image=photo, anchor=NW)
canvas.pack()

window.mainloop()