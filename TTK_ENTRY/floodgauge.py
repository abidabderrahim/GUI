from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

def start():
    fgauge.start()

def stop():
    fgauge.stop()
    label.config(text=f'Position: {fgauge.variable.get()}')

def inc():
    fgauge.step(5)
    

window = tb.Window(themename='cyborg')
window.title('TTK')
window.geometry('500x500')

fgauge = tb.Floodgauge(window,
                      bootstyle='success',
                      font=('Helvetica', 18),
                      mask="Pos: {}%",
                      maximum=100,
                      orient=HORIZONTAL,
                      value=0,
                      mode=INDETERMINATE)
fgauge.pack(pady=50, fill=X, padx=30)

button_start = tb.Button(window,
                        text='Start',
                        bootstyle='success outline',
                        command=start)
button_start.pack(pady=25)

button_stop = tb.Button(window,
                        text='Stop',
                        bootstyle='danger outline',
                        command=stop)
button_stop.pack(pady=25)

button_inc = tb.Button(window,
                        text='Increment',
                        bootstyle='warning  outline',
                        command=inc)
button_inc.pack(pady=25)

label = tb.Label(window,
                text='Position : ',
                foreground='green'
                )
label.pack(pady=20)

window.mainloop() 