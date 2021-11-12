import sqlite3
import threading
import time
from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox
from tkinter.ttk import Separator
import login

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from tkHyperLinkManager import HyperlinkManager
import webbrowser

from selenium.webdriver.common.keys import Keys
import userPass


class ExistUserStart(Tk):

    def __init__(self,ws):

        menubar = Menu(ws)
        ws.config(menu=menubar)

        # Adding file menu and commands
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file)
        file.add_command(label='Delete user', command=lambda :delete_user())
        file.add_separator()
        file.add_command(label='Exit', command=ws.destroy)


        ws.title('WA-existUser')
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

        title.place(relx=0.5, rely=0.15, relwidth=0.60,
                                    relheight=0.1, anchor="n")

        title.config(font=('Helvatical bold',20))

        Border = 3
        UsernameFrame = Frame(ws, bg="lightgrey", bd=Border)
        UsernameFrame.place(relx=0.5, rely=0.259, relwidth=0.60,
                                     relheight=0.1, anchor="n")



        Username = Entry(UsernameFrame, font=40, justify="right")
        Username.insert(0, "שם משתמש")
        Username.place(relwidth=1, relheight=1)
        Username.focus()



        button = Button(MainFrame, text="התחברות",bg="lightblue",
                               command=lambda:GoToPosts(Username.get()))

        button.place(relx=0.5, rely=0.4, relwidth=0.6,
                     relheight=0.085, anchor="n")

        button.config(font=('Helvatical bold',20))

        button = Button(MainFrame, text="משתמש חדש",bg="white",borderwidth=0,font=('Helvatical bold',15),fg="blue",
                           command= nextPageNewUser)

        button.place(relx=0.5, rely=0.51, relwidth=0.2,
                     relheight=0.05, anchor="n")


        separator1 = Separator(ws, orient='horizontal')
        separator1.place(relx=0.5, rely=0.6, relwidth=0.6,
                     relheight=0.000001, anchor="n")

        button = Button(MainFrame, text="סגור",bg="white",
                           command= ws.destroy)

        button.place(relx=0.5, rely=0.65, relwidth=0.2,
                     relheight=0.05, anchor="n")

        label = Label(ws, text = "Created by elishevada © 2021", font = 13, bg = "white", fg = "black")
        label.place(relx = 0.5, rely = 0.93, anchor = "n")

def delete_user():
    label = Label(ws, text="delete for:", font=13, bg="white", fg="black")
    label.place(relx=0.1, rely=0.01, anchor="n")

    UsernameFrame = Frame(ws, bg="lightgrey", bd=1)
    UsernameFrame.place(relx=0.3, rely=0.01,relwidth=0.3, relheight=0.05, anchor="n")
    Username = Entry(UsernameFrame, font=40, justify="right")
    Username.place(relwidth=1, relheight=1)
    Username.focus()

    button = Button(ws, text="מחק", bg="lightblue",
                    command=lambda: deleteFor(Username.get()))

    button.place(relx=0.5, rely=0.01, relwidth=0.1,
                 relheight=0.05, anchor="n")


def deleteFor(userToDelete):
    try:
        conn = sqlite3.connect('postManagment.db')
        cursor=conn.execute(f"SELECT * FROM users  WHERE UserName='{userToDelete}'");#for checking bcs the delete doesnt returns error if not exist
        cursor.fetchone()[0]
        conn.execute(f"DELETE from users WHERE UserName = '{userToDelete}'");

        conn.commit()
        conn.close()
        Start = ExistUserStart(ws)
    except:
        messagebox.showwarning("this user doesnt exist for delete")




def GoToPosts(user):

    try:
        conn = sqlite3.connect('postManagment.db')
        cursor=conn.execute(f"SELECT Password FROM users  WHERE UserName='{user}'");
        userPass.setPass(user)
        userPass.setUser(cursor.fetchone()[0])
        ws.destroy()
        import postManagement
    except:
        messagebox.showwarning("this user is not exist for select")





def nextPageNewUser():
    ws.destroy()
    import newUser



if __name__ == "__main__":
    print("Run from main")
    conn = sqlite3.connect('postManagment.db')
    # conn.execute("INSERT INTO users (UserName,Password) VALUES (?,?)",(user,r));
    # conn.execute("DELETE FROM users  WHERE UserName='050438000777'");
    # conn.commit()
    # conn = sqlite3.connect('postManagment.db')
    cursor = conn.execute("SELECT * from users")
    print(cursor.fetchall())

    conn.close()

    ws=Tk()
    Start = ExistUserStart(ws)
    ws.mainloop()
else:
    print("Run from import")
    ws = Tk()
    Start = ExistUserStart(ws)
    ws.mainloop()