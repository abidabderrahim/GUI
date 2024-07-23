from tkinter import *
from tkinter import ttk

window = Tk()
window.config(background='black')
window.geometry('300x300')

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,
             text='Tba 1')

notebook.add(tab2,
             text='Tab 2')

notebook.pack(expand=True, fill="both")

Label(tab1,text="tab number 1",
           width=50, height=25,
           background='black',
           foreground='green').pack()
Label(tab2,text="tab number 2",
           width=50, height=25,
           background='black',
           foreground='green').pack()

notebook.pack()
window.mainloop()