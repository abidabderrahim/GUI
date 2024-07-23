from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import random

def change():
    mode = ['defualt', 'primary', 'success', 'info', 'secondry', 'light', 'warning', 'dark', 'danger']
    count = random.randint(0,8)
    button.config(bootstyle=f'{mode[count]}')
    label.config(bootstyle=f'{mode[count]}')
    

window = tb.Window(themename='cyborg')
window.title('TTK')
window.geometry('500x500')

"""
colors : default , primary , secondary , success , info , 
warning , dange , light , dark .
"""
label = tb.Label(text='hello world',
                font=('Helvetic', 28),
                bootstyle='success')
label.pack(pady=50)

button = tb.Button(text='Click Me',
                  bootstyle='success',
                  command=change)
button.pack(pady=25)

window.mainloop()