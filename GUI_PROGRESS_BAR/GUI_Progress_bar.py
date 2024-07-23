from tkinter.ttk import *
import time
from tkinter import *


def start():
    tasks = 10
    x = 0
    while x < tasks:
        time.sleep(0.10)
        bar['value']+=10
        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        text.set(str(x) +'/'+ str(tasks)+'download completed .')
        window.update_idletasks()

window = Tk()
window.geometry("300x150")
window.config(background='black')

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=200)
bar.pack(pady=10)

percent_label = Label(window,textvariable=percent,background='black',foreground='green').pack()
task_label = Label(window,textvariable=text,background='black',foreground='green').pack()

button = Button(window,
                text='download',
                font=('Comic Sans', 15),
                fg='green',
                bg='black',
                activebackground='black',
                activeforeground='green',
                command=start).pack()

window.mainloop()