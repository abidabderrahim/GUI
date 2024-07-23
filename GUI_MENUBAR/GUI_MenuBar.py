from tkinter import *

def openfile():
    print("you open some file .")

def savefile():
    print("file saved .")

def editfile():
    print("open file for edit .")

def cutfile():
    print("cut text from file .")

def copyfile():
    print("copy text from file .")

window = Tk()
window.config(background='black')
window.geometry('400x400')

menubar = Menu(window, 
               background='black',
               foreground='green')
               
window.config(menu=menubar)

photo = PhotoImage(file='4518857_python_icon.png')

filemenu = Menu(menubar, 
                tearoff=0, 
                background='black')
menubar.add_cascade(label='file',
                    menu=filemenu)
filemenu.add_command(label="Open", 
                     background='black',
                     command=openfile,
                     image=photo,
                     compound='left')
filemenu.add_command(label="Save", 
                     background='black',
                     command=savefile,
                     image=photo,
                     compound='left')
filemenu.add_command(label="Exit",
                     background='black',
                     command=quit,
                     image=photo,
                     compound='left')

editmenu = Menu(menubar, tearoff=0, background='black')
menubar.add_cascade(label='Edit',
                    menu=editmenu)
editmenu.add_command(label='Edit', 
                     background='black',
                     command=editfile)
editmenu.add_command(label='Cut', 
                     background='black',
                     command=cutfile) 
editmenu.add_command(label='Copy', 
                     background='black',
                     command=copyfile)                

filemenu.add_separator()
window.mainloop()