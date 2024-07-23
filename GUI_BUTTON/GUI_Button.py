from tkinter.ttk import *
from tkinter import *

count = 0
def click():
    global count
    count +=1
    print(count)

window = Tk()
photo = PhotoImage(file='4518857_python_icon.png')
button = Button(window, 
                text='Click-Hear', 
                command=click,
                font=('Comic Sans', 30),
                fg='green',
                bg='black',
                activebackground='black',
                activeforeground='green',
                state=ACTIVE,
                image=photo,
                compound='left')
button.pack()

window.mainloop()