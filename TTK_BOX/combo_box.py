from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

def click():
    label.config(text=f"you clicked on {my_combo.get()}")

def bind_f(event):
    label.config(text=f"you clicked on {my_combo.get()}")

window = tb.Window(themename='cyborg')
window.title('TTK Button')
window.geometry('500x500')

label = tb.Label(window,
                text='Take Some Option',
                font=('Helvetica', 18))
label.pack(pady=30)

chars = ["A", "B", "C", "D", "E", "F"]

my_combo = tb.Combobox(window,
                       bootstyle='success',
                       values=chars)
my_combo.pack(pady=20)
my_combo.current(0)

button = tb.Button(window,
                   text='click me',
                   command=click,
                   bootstyle='success')
button.pack(pady=25)

my_combo.bind("<<ComboboxSelected>>", bind_f)

window.mainloop()