from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='this is info message box',message='hello world')
    
    #while (True):
        #messagebox.showwarning(title='this is warning message box',message='you have a virus!!!')
    
    #messagebox.showerror(title='this is error message',message='you have an error !!!')
    
    #if messagebox.askokcancel(title='ask ok cancel',message='do you mant to do it ?'):
    #    print("you do it !")
    #else:
    #   print("you not do it !")
    
    #if messagebox.askretrycancel(title='ask ok cancel',      message='do you want retry the thing ?'):
    #    print("you retried a thing !")
    #else:
    #    print("you canceled a thing !")
    
    #if messagebox.askyesno(title='ask yes or no',message='star run the code ?'):
    #    print("code start !")
    #else:
    #    print("starting code stop !")

    #answer = messagebox.askquestion(title='ask question', message='do want to start program')
    #if answer == 'yes':
    #    print("program start !")
    #else:
    #    print("program stop !")

    answer = messagebox.askyesnocancel(title='yes no cancel', message='do you wnat to run the program ?',icon='info')
    if answer == True:
        print('program start !')
    elif answer == False:
        print("program stop !")
    else:
        print("process stop !")

window = Tk()

button = Button(window, 
                text='click me',
                fg='green',
                bg='black',
                activebackground='black',
                activeforeground='green',
                command=click)

button.pack()
window.mainloop() 