from tkinter import *

def dosomething(event):
    print("you do thing .")
    # str(event.x) str(event.y) : cordinates of mous click .

window = Tk()

# Button-1 : left .
# Button-2 : left and right .
# Button-3 : right .
# ButtonRelease .
# Enter .
# Leave .
# Motion .
window.bind("<Button-1>",dosomething)

window.mainloop()