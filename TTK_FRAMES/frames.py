from tkinter import *
import ttkbootstrap as tb

def click():
    if entry.get() != "":
        label.config(text=f"You Typed : {entry.get()}")
    else:
        label.config(text="...")


window = tb.Window(themename='cyborg')

window.title('TTK')
window.geometry('500x500')

frame = tb.Frame(window,
                bootstyle='dark')
frame.pack(pady=40)

entry = tb.Entry(frame, 
                font=('Helvetica', 18), 
                bootstyle='success')
entry.pack(pady=20, padx=20)

button = tb.Button(frame, 
                  text='Click', 
                  bootstyle='success outline',
                  command=click)
button.pack(pady=20, padx=20)

label = tb.Label(window, text='...', 
                font=('Helvetica', 18),
                bootstyle='success',
                )
label.pack(pady=20)

window.mainloop()