from tkinter import *

def submit():
    print(f"the Python Level is: {str(scale.get())}%")

window = Tk()

photo = PhotoImage(file='4518857_python_icon.png')
label = Label(image=photo)
label.pack()

window.config(background='black')
scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,
              font=('Consolas', 10),
              tickinterval=10,
              showvalue=1,
              background='black',
              foreground='green',
              troughcolor='green')
scale.set(50)
button = Button(window, 
                text='submit', 
                command=submit,
                font=('Arial', 20),
                fg="green",
                bg='black',
                activebackground='black',
                activeforeground='green')
scale.pack()
photo_tow = PhotoImage(file='4518857_python_icon.png')
label_two = Label(image=photo_tow)
label_two.pack()
button.pack()
window.mainloop()