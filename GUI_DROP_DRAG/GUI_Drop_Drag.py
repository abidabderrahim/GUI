from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()
window.geometry('300x300')
window.config(background='black')

label0 = Label(window,
              text="A",
              background='black',
              foreground='green',
              font=('Arial', 20))
label0.place(x=0, y=0)

label1 = Label(window,
              text="B",
              background='black',
              foreground='green',
              font=('Arial', 20))
label1.place(x=50, y=50)

label0.bind("<Button-1>",drag_start)
label0.bind("<B1-Motion>",drag_motion)

label1.bind("<Button-1>",drag_start)
label1.bind("<B1-Motion>",drag_motion)

window.mainloop()