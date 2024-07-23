from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

def check():
    if var1.get() == 1:
        label.config(text='checked !!!')
    elif var1.get() == 0:
        label.config(text='Click the CheckBox')

window = tb.Window(themename='superhero')
window.title('TTK')
window.geometry('500x500')

label = tb.Label(text='Click the CheckBox',
                font=('Helvetica', 18))
label.pack(pady=(40,10))

var1 = IntVar()
check = tb.Checkbutton(bootstyle='info',
                      text='Click Me',
                      variable=var1,
                      onvalue=1,
                      offvalue=0,
                      command=check)
check.pack(pady=10)

window.mainloop()