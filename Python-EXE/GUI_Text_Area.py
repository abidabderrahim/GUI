from tkinter import *


window = Tk()
window.config(bg='black')
window.title('Text Area')

text = Text(window,
            bg='light yellow',
            fg='black',
            font=('Ink Free', 20),
            height=8,
            width=20,
            padx=20,
            pady=20)
text.pack()
window.mainloop()