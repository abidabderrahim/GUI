from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("you take : ", end="")
    for index in food:
        print(f"{index} ", end="")
    print()

def add():
    listbox.insert(listbox.size(),entry_box.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()
window.config(background='black')
listbox = Listbox(window,
                  fg='green',
                  bg='black',
                  font=('Arial', 20),
                  width=15,
                  selectmode=MULTIPLE
                  )
listbox.pack()

entry_box = Entry(window, bg='black',fg='green')
entry_box.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"garlic")
listbox.insert(3,"soup")
listbox.insert(4,"salad")
listbox.config(height=listbox.size())
submit_button = Button(window,
                       text='Submit',
                       bg='black',
                       fg='green',
                       activebackground='black',
                       activeforeground='green',
                       command=submit)
add_button = Button(window,
                    text='add', 
                    command=add,
                    bg='black',
                    fg='green',
                    activebackground='black',
                    activeforeground='green',)
delete_button = Button(window,
                    text='delete', 
                    command=delete,
                    bg='black',
                    fg='green',
                    activebackground='black',
                    activeforeground='green',)
submit_button.pack()
add_button.pack()
delete_button.pack()
window.mainloop()