from tkinter import *


window = Tk()
window.geometry("300x300")
window.config(background='black')

title_label = Label(window,
                    text="enter your info",
                    font=("Arial", 25),
                    background='black',
                    foreground='green').grid(row=0,column=0,columnspan=2)

first_name = Label(window,
                   text="first name : ",
                   background='black',
                   foreground='green',
                   width=15).grid(row=1, column=0)
first_name_entry = Entry(window,
                        background='green',
                        fg='black').grid(row=1,column=1)
last_name = Label(window,
                   text="last name : ",
                   background='black',
                   foreground='green').grid(row=2, column=0)
last_name_entry = Entry(window,
                        background='green',
                        fg='black').grid(row=2,column=1)
email = Label(window,
                   text="email : ",
                   background='black',
                   foreground='green').grid(row=3, column=0)
email = Entry(window,
                        background='green',
                        fg='black').grid(row=3,column=1)
submit_button = Button(window,
                       text='Submit',
                       background='black',
                       foreground='green',
                       activebackground='black',
                       activeforeground='green').grid(row=4,column=1,columnspan=1)

window.mainloop()