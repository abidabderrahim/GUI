from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(initialdir='/home/november/Desktop/START/PROJECTS-POINT',title='open file .',filetypes=(("text files", "*.txt"),
    ("python files", "*.py*")))
    file = open(file_path, 'r')
    print(file.read())
    file.close()

window = Tk()
window.config(background='black')
window.title('FILE OPEN')

button = Button(window, 
                text="OPEN",
                font=('Arial', 20),
                bg='black',
                fg='green',
                activebackground='black',
                activeforeground='green',
                command=open_file)

button.pack()
window.mainloop()
