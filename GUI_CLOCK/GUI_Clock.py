from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    date_string = strftime("%B-%d-%Y")
    date_label.config(text=date_string)
    window.after(1000, update)

window = Tk()
window.config(background='black')
window.geometry('400x200')

time_label = Label(window,
                   font=('Arial', 50),
                   fg='green',
                   background='black')
date_label = Label(window,
                   font=('Arial', 20),
                   fg='green',
                   background='black')

time_label.pack()
date_label.pack()
update()

window.mainloop()