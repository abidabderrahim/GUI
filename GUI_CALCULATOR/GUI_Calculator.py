from tkinter import *

def button_press(num):
    global op_text
    op_text = op_text + str(num)
    op_label.set(op_text)

def equal():
    global op_text
    try:
      total = str(eval(op_text))
      op_label.set(total)
      op_text = total
    except SyntaxError:
        op_label.set("...")
    except ZeroDivisionError:
        op_label.set("Null")

def clear():
    global op_text
    op_label.set("")
    op_text = ""

window = Tk()

window.title('Calculator')
window.geometry('500x500')
window.config(background='black')
op_text = ""

op_label = StringVar()

label = Label(window,
              textvariable=op_label,
              font=('Arial', 20),
              background='black',
              foreground='green',
              width=24,
              height=2)
label.pack()

frame = Frame(window, background='black')
frame.pack()

button1 = Button(frame, 
                 text=1, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(1))
button1.grid(row=0,column=0)
button2 = Button(frame, 
                 text=2, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(2))
button2.grid(row=0,column=1)
button3 = Button(frame, 
                 text=3, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(3))
button3.grid(row=0,column=2)
button4 = Button(frame, 
                 text=4, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(4))
button4.grid(row=1,column=0)
button5 = Button(frame, 
                 text=5, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(5))
button5.grid(row=1,column=1)
button6 = Button(frame, 
                 text=6, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(6))
button6.grid(row=1,column=2)
button7 = Button(frame, 
                 text=7, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(7))
button7.grid(row=2,column=0)
button8 = Button(frame, 
                 text=8, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(8))
button8.grid(row=2,column=1)
button9 = Button(frame, 
                 text=9, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(9))
button9.grid(row=2,column=2)
button0 = Button(frame, 
                 text=0, 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press(0))
button0.grid(row=3,column=0)
plus = Button(frame, 
                 text='+', 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press('+'))
plus.grid(row=0,column=4)
sub = Button(frame, 
                 text='-', 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press('-'))
sub.grid(row=1,column=4)
mult = Button(frame, 
                 text='x', 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press('*'))
mult.grid(row=2,column=4)
div = Button(frame, 
                 text='/', 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press('/'))
div.grid(row=3,column=4)
equal = Button(frame, 
                 text='=', 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=equal)
equal.grid(row=3,column=1)
point = Button(frame, 
                 text='.', 
                 height=3, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=lambda: button_press('.'))
point.grid(row=3,column=2)
clear = Button(window, 
                 text='C', 
                 height=2, 
                 width=4,
                 font=20,
                 background='black',
                 foreground='green',
                 activebackground='black',
                 activeforeground='green',
                 command=clear)
clear.pack()

window.mainloop()