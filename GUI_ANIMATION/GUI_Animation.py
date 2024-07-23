from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window, 
                width=WIDTH, 
                height=HEIGHT,
                background='black')
canvas.pack()

photo = PhotoImage(file='4518857_python_icon.png')
myimage = canvas.create_image(0,0, image=photo, anchor=NW)

image_width = photo.width()
image_height = photo.height()

while True:
    cordinates = canvas.coords(myimage)
    if cordinates[0] >= (WIDTH - image_width) or cordinates[0] < 0:
        xVelocity = -xVelocity
    if cordinates[1] >= (HEIGHT - image_height) or cordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(myimage, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()