from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap import Querybox

def get_date():
    label.config(text=f'You Picked : {date.entry.get()}')

def get_c():
    cale = Querybox()
    label.config(text=f'You Picked : {cale.get_date()}')

window = tb.Window(themename='cyborg')
window.title('TTK')
window.geometry('500x500')

date = tb.DateEntry(window,
                   bootstyle='danger',
                   startdate=date(2023, 11, 21),
                   firstweekday=0)
date.pack(pady=50)

button = tb.Button(window,
                   text='Get date',
                   bootstyle='danger outline',
                   command=get_date)
button.pack(pady=25)
button2 = tb.Button(window,
                   text='Get Calender',
                   bootstyle='warning outline',
                   command=get_c)
button2.pack(pady=25)

label = tb.Label(window,
                text='',
                bootstyle='danger')
label.pack(pady=25)

window.mainloop()