from tkinter import *

Window = Tk()

canvas = Canvas(Window, 
                width=500, 
                height=500, 
                background='white')
#line1 = canvas.create_line(0,0,500,500,fill='blue',width=5) 
#line2 = canvas.create_line(0,500,500,0,fill='blue',width=5)
# (x,y:start , x,y:end)
#canvas.create_rectangle(50,50,250,250,fill='red',width=5)
#canvas.create_polygon(250,0,500,500,0,500,fill='red',outline='black',width=5)
#canvas.create_arc(0,0,500,500, fill='green', style=PIESLICE,start=90,extent=180)

canvas.create_arc(10,10,490,490,fill='red',extent=180,width=5)
canvas.create_arc(10,10,490,490,fill='white',extent=180,width=5,start=180)
canvas.create_oval(190,190,310,310, fill='red', width=5, outline='red')
canvas.create_oval(220,220,280,280, fill='white', width=5,outline='white')
canvas.pack()

Window.mainloop()