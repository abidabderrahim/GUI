from tkinter import *

def submit():
    username = entry.get()
    if username != "":
        print("hello ", username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

photo = PhotoImage('4518857_python_icon.png')
entry = Entry(window,
              font=('Arial', 40),
              bg='black',
              fg='green',
              show='*')
submit_button = Button(window,
                       text='Submit',
                       font=('Arial', 20),
                       bg='black',
                       fg='green',
                       activebackground='black',
                       activeforeground='green',
                       command=submit)
delete_button = Button(window,
                       text='delete',
                       font=('Arial', 20),
                       bg='black',
                       fg='green',
                       activebackground='black',
                       activeforeground='green',
                       command=delete)
backspace_button = Button(window,
                       text='backspace',
                       font=('Arial', 20),
                       bg='black',
                       fg='green',
                       activebackground='black',
                       activeforeground='green',
                       command=backspace)
entry.pack(side=LEFT)
submit_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
backspace_button.pack(side=RIGHT)
window.mainloop()