from tkinter import *
from tkinter import messagebox
import smtplib

def send():
    sender = sender_name_entry.get()
    receiver = receiver_entry.get()
    password = password_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", END)
    message = f"""
    From: {sender}
    To: {receiver}
    Subject: {subject}\n
    {body}
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        messagebox.showinfo("Success", "Logged in successfully!")
        server.sendmail(sender, receiver, message)
        messagebox.showinfo("Success", "Email sent successfully.")
        server.quit()
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Unable to sign in.")

window = Tk()
window.geometry("500x500")
window.config(background='black')

title_label = Label(window,
                    text="Enter your info",
                    font=("Arial", 25),
                    background='black',
                    foreground='green').grid(row=0, column=0, columnspan=2)

sender_name = Label(window,
                    text="Sender: ",
                    background='black',
                    foreground='green',
                    width=15).grid(row=1, column=0)
sender_name_entry = Entry(window,
                          background='green',
                          fg='black',
                          width=25)
sender_name_entry.grid(row=1, column=1)

receiver_name = Label(window,
                      text="Receiver: ",
                      background='black',
                      foreground='green').grid(row=2, column=0)
receiver_entry = Entry(window,
                       background='green',
                       fg='black',
                       width=25)
receiver_entry.grid(row=2, column=1)

password_label = Label(window,
                       text="Password: ",
                       background='black',
                       foreground='green').grid(row=3, column=0)
password_entry = Entry(window,
                       show='*',
                       background='green',
                       fg='black',
                       width=25)
password_entry.grid(row=3, column=1)

subject_label = Label(window,
                      text="Subject: ",
                      background='black',
                      foreground='green').grid(row=4, column=0)
subject_entry = Entry(window,
                      background='green',
                      fg='black',
                      width=40)
subject_entry.grid(row=4, column=1)

body_label = Label(window,
                   text="Body: ",
                   background='black',
                   foreground='green').grid(row=5, column=0)
body_text = Text(window,
                 bg='black',
                 fg='green',
                 font=('Ink Free', 10),
                 height=8,
                 width=18,
                 padx=20,
                 pady=20)
body_text.grid(row=5, column=1)

submit_button = Button(window,
                       text='Send',
                       background='black',
                       foreground='green',
                       activebackground='black',
                       activeforeground='green',
                       command=send).grid(row=6, column=1, columnspan=1)

window.mainloop()