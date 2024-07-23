from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(initialdir="/home/november/Desktop/START/PROJECTS-POINT",
                                    defaultextension=".txt",
                                    filetypes=[("text file", "*.txt"),
                                    ("Python file", "*.py")])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    # filetext = str(input("enter some text : "))
    # so we can use console .
    file.write(filetext)
    file.close()

window = Tk()

window.config(background='black')
window.title("Save Files")

text = Text(window,
            bg='light yellow',
            fg='black',
            width=30,
            height=16,
            padx=20,
            pady=20)
button = Button(window,
                text='Save',
                bg='black',
                fg='green',
                activebackground='black',
                activeforeground='green',
                command=savefile)
text.pack()
button.pack()
window.mainloop()