from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

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
button = Button(window,
                text='submit',
                fg='green',
                bg='black',
                activebackground='black',
                activeforeground='green',
                command=submit)
text.pack()
button.pack()
window.mainloop()