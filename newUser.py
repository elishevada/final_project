from tkinter import *

ws = Tk()
# ws.geometry('400x300')
ws.title('WA-newUser')



def GoToPosts():
    ws.destroy()
    import postManagement


canvas = Canvas(ws, height=700, width=1000)
canvas.pack()

MainFrame = Frame(ws, bg="white")
MainFrame.place(relwidth=1, relheight=1)

title=Label(
    ws,
    text="''WA-ברוכים הבאים לאתר''",
    fg="black",
    bg="white",
    font=40
)

title.place(relx=0.5, rely=0.02, relwidth=0.60,
                            relheight=0.1, anchor="n")

title.config(font=('Helvatical bold',20))

Border = 3
UsernameFrame = Frame(ws, bg="lightgrey", bd=Border)
UsernameFrame.place(relx=0.5, rely=0.135, relwidth=0.60,
                            relheight=0.1, anchor="n")


Username = Entry(UsernameFrame, font=40, justify="right")
Username.insert(0, "שם משתמש")
Username.place(relwidth=1, relheight=1)
Username.focus()
PasswordFrame = Frame(ws, bg="lightgrey", bd=Border)
PasswordFrame.place(relx=0.5, rely=0.26, relwidth=0.60,
                    relheight=0.1, anchor="n")

Password = Entry(PasswordFrame, show="*",  font=40, justify="right")
Password.insert(0, "סיסמא")
Password.place(relwidth=1, relheight=1)

button = Button(MainFrame, text="התחברות",bg="lightblue",
                   command=GoToPosts)

button.place(relx=0.5, rely=0.4, relwidth=0.6,
             relheight=0.085, anchor="n")

button.config(font=('Helvatical bold',20))




button = Button(MainFrame, text="סגור",bg="white",
                   command= ws.destroy)

button.place(relx=0.5, rely=0.55, relwidth=0.2,
             relheight=0.05, anchor="n")

label = Label(ws, text = "Created by elishevada © 2021", font = 13, bg = "white", fg = "black")
label.place(relx = 0.5, rely = 0.93, anchor = "n")


ws.mainloop()