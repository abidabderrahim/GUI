from tkinter import *

window = Tk()

photo = PhotoImage(file='4518857_python_icon.png')
label = Label(window,text="hello world!", font=('Arial', 40,'bold'),fg='red',bg='black', relief=RAISED, bd=10, padx=10, pady=10, image=photo, compound='bottom') 
# we add text, font-style , font-size, font-weight , #front-ground color , backgrund color , border , 
# padding x and y , image with compound relative . 
#label.place(x=55, y=75)
label.pack() # for display the label in window .
window.mainloop()