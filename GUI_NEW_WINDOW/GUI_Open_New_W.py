from tkinter import *

def open_w():
    new_window = Toplevel()
    #window.destroy() # close main window .
    new_window.config(background='black')
    new_window.geometry('300x300')
    button = Button(new_window,
                    text='just Button',
                    background='black',
                    foreground='green',
                    activebackground='black',
                    activeforeground='green').pack()

window = Tk()
window.config(background='black')
window.title('Opne New Windows')
window.geometry("300x300")

button = Button(window, 
                text='opne window',
                command=open_w,
                background='black',
                foreground='green',
                activebackground='black',
                activeforeground='green').place(x=90,y=110)

window.mainloop()