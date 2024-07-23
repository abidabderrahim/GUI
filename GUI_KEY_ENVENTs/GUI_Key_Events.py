from tkinter import *

def dodomething(event):
    label.config(text=event.keysym)


window = Tk()
window.geometry("300x300")
window.config(background="black")

window.bind("<Key>",dodomething)
label = Label(window,
              font=("Helvetica", 20),
              background='black',
              foreground='green')
label.pack()

window.mainloop()