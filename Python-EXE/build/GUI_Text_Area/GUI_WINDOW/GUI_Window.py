from tkinter import *

window = Tk()

window.geometry("500x500") # window szie x and y .
window.title("first_GUI-window") # window title name .
icon = PhotoImage(file='4518857_python_icon.png')
window.iconphoto(True, icon) # window icon .
window.config(background='white') # background window .

window.mainloop()