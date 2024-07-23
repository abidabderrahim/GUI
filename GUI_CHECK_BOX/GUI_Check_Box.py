from tkinter import *

def display():
    if(x.get() == 1):
        print("you agree !")
    else:
        print("you not !")

Window = Tk()

photo = PhotoImage(file="4518857_python_icon.png")
x = IntVar()
check_button = Checkbutton(Window,
                           text='I agree.',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='green',
                           bg='black',
                           activebackground='black',
                           activeforeground='green',
                           padx=25,
                           pady=25,
                           image=photo,
                           compound='left')

check_button.pack()
Window.mainloop()