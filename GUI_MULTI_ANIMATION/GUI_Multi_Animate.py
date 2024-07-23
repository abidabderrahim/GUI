from tkinter import *
import time

class Ball:
    def __init__(self, canvas, x, y, diameter, xvelocity, yvelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
    
    def move(self):
        cordinates = self.canvas.coords(self.image)
        if cordinates[2]>=(self.canvas.winfo_width()) or cordinates[0] < 0:
            self.xvelocity = -self.xvelocity
        if cordinates[3]>=(self.canvas.winfo_height()) or cordinates[1] < 0:
            self.yvelocity = -self.yvelocity
        self.canvas.move(self.image, self.xvelocity, self.yvelocity)


window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, 
                width=WIDTH, 
                height=HEIGHT, 
                background='black')
canvas.pack()

ball1 = Ball(canvas, 0,0,100,2,1,'red')
ball2 = Ball(canvas, 0,0,50,4,3,'green')
ball3 = Ball(canvas, 0,0,80,5,2,'white')


while True: 
    ball1.move()
    ball2.move()
    ball3.move()
    window.update()
    time.sleep(0.01)

window.mainloop()