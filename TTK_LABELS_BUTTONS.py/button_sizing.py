from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


window = tb.Window(themename='cyborg')
window.title('TTK Button')
window.geometry('500x500')

"""
style : for text ...
width , height : for button .
"""
my_style = tb.Style()
my_style.configure('success.TButton', font=('Helvetica', 18))
button = tb.Button(text='Click Me',
                  bootstyle='success',
                  style='success.Outline.TButton',
                  width=15)
button.pack(pady=20)

window.mainloop()