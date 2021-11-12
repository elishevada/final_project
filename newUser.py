import sqlite3
import threading
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import login
import tooltip
import userPass




class NewUserStart(Tk):

    def __init__(self,ws):
        # ws = Tk()
        # ws.geometry('400x300')
        ws.title('WA-newUser')

        canvas = Canvas(ws, height=700, width=1000)
        canvas.pack()

        MainFrame = Frame(ws, bg="white")
        MainFrame.place(relwidth=1, relheight=1)


        loadimage = PhotoImage(file="arrow.png")
        roundedbutton = Button(ws, image=loadimage, bg="white", borderwidth=0, bd=0, text="back",
                               command=lambda: ws.destroy)
        tooltip.CreateToolTip(roundedbutton, text='Go back')
        roundedbutton.place(relx=0.01, rely=0.02, relwidth=0.06,
                            relheight=0.09,anchor="n")

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
                           command=lambda :threading.Thread(target=GoToPosts,args=(Username.get(), Password.get())).start())

        button.place(relx=0.5, rely=0.4, relwidth=0.6,
                     relheight=0.085, anchor="n")

        button.config(font=('Helvatical bold',20))




        button = Button(MainFrame, text="סגור",bg="white",
                           command= lambda: ws.destroy())

        button.place(relx=0.5, rely=0.55, relwidth=0.2,
                     relheight=0.05, anchor="n")

        label = Label(ws, text = "Created by elishevada © 2021", font = 13, bg = "white", fg = "black")
        label.place(relx = 0.5, rely = 0.93, anchor = "n")



def GoToPosts(username,password):
    FS = login.store_post_information(username, password)
    # FS = login.store_post_information("0504380777", "judge444")
    FS.login()
    if(FS.check_validation()):
        #insert to database the username and password
        try:
            conn = sqlite3.connect('postManagment.db')
            conn.execute("INSERT INTO users (UserName,Password) VALUES (?,?)",(username,password));
            conn.commit()
            conn.close()
            userPass.setPass(password)
            userPass.setUser(username)
            FS.closeBrowser()
            lablePopup(">נרשמת למערכת בהצלחה ,לכניסה "  ,"foward")

        except:
            FS.closeBrowser()
            messagebox.showwarning("this user already exists pls go to  exist user")
            lablePopup("המשתמש קיים חזור לעמוד קודם ","back")



    else:
        FS.closeBrowser()
        messagebox.showerror("Error", "password or username are wrong try again")



def lablePopup(text,type):

    subFrame = Frame(ws, bg="white")
    subFrame.place(relwidth=1, relheight=1)

    if (type == "foward"):
        button = Button(subFrame, text=text, bg="white", borderwidth=0,
                    font=('Helvatical bold', 15), fg="blue",
                    command=lambda: nextlable())
    if (type == "back"):
        button = Button(subFrame, text=text, bg="white", borderwidth=0,
                    font=('Helvatical bold', 15), fg="blue",
                    command=lambda: backPageExistUser())

    button.place(relx=0.5, rely=0.5, relwidth=0.8,
                 relheight=0.05, anchor="n")



def backPageExistUser():
    ws.destroy()
    import existUser

def nextlable():
    ws.destroy()
    import postManagement

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

    # conn.execute('''CREATE TABLE users
    #                  (UserName TEXT PRIMARY KEY ,
    #                  Password           TEXT );''')


    # conn = sqlite3.connect('test2.db')
    #
    # # conn.execute('''CREATE TABLE COMPANY
    # #          (ID INT PRIMARY KEY     NOT NULL,
    # #          NAME           TEXT    NOT NULL,
    # #          AGE            INT     NOT NULL,
    # #          ADDRESS        CHAR(50),
    # #          SALARY         REAL);''')
    # # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    # #       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    # # conn.commit()
    # cursor = conn.execute("SELECT * from COMPANY")
    # print(cursor.fetchall())
    # # for row in cursor:
    # #     print("id= ",row[0])
    # #     print("name= " ,row[1])
    # #     print("add= " ,row[2])
    # #     print("sal= ",row[3])
    #
    #


    ws=Tk()
    Start = NewUserStart(ws)

    ws.mainloop()
else:
    print("Run from import")
    conn = sqlite3.connect('postManagment.db')
    cursor = conn.execute("SELECT * from users")
    print(cursor.fetchall())
    conn.close()

    ws = Tk()
    Start = NewUserStart(ws)

    ws.mainloop()
