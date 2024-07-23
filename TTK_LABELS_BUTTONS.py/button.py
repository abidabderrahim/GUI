from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import random



def change():
    mode = ['defualt', 'primary', 'success', 'info', 'secondry', 'light', 'warning', 'dark', 'danger']
    count = random.randint(0,8)
    button.config(bootstyle=f'{mode[count]}')


window = tb.Window(themename='cyborg')
window.title('TTK Button')
window.geometry('500x500')

"""
colors : default , primary , secondary , success , info , 
warning , danger , light , dark .
"""
"""
buttons : link , outline .
"""
button = tb.Button(text='Click Me',
                  bootstyle='success',
                  command=change)
button.pack(pady=20)

window.mainloop()