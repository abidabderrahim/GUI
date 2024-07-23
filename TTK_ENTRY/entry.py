from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

def text():
    label.config(text=f"you typed : {entry.get()} .")

window = tb.Window(themename='cyborg')
window.title('TTK')
window.geometry('500x500')

entry = tb.Entry(window, bootstyle='success', foreground='green', show="-")
entry.pack(pady=50)

button = tb.Button(window,
                   text='Click Me',
                   bootstyle='success, outline',
                   command=text)
button.pack(pady=20)

label = tb.Label(window, text='', foreground='green')
label.pack(pady=20)

window.mainloop()