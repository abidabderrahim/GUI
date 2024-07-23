from tkinter import *

data  = ["A", "B", "C", "D"]
def order():
    if x.get() == 0:
        print("you take A")
    elif x.get() == 1:
        print("you take B")
    elif x.get() == 2:
        print("you take C")
    else:
        print("you take D")

window = Tk()
photo = PhotoImage(file='4518857_python_icon.png')
photos = [photo,photo,photo,photo]
x = IntVar()
for index in range(len(data)):
    radiobutton = Radiobutton(window, 
                              text=data[index],
                              variable=x,
                              value=index,
                              padx=20,
                              pady=20,
                              font=('Arial', 20),
                              image=photos[index],
                              compound='left',
                              indicatoron=0, # change to button .
                              width=300,
                              command=order) 
    radiobutton.pack(anchor=W)

window.mainloop()