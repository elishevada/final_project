import sqlite3
import threading
import time
import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import login
import tooltip
import userPass
import data_base_function as db




class NewUserStart(Tk):

    def __init__(self,ws):
        # ws = Tk()
        # ws.geometry('400x300')
        ws.title('WA-משתמש חדש')

        canvas = Canvas(ws, height=700, width=1000)
        canvas.pack()

        MainFrame = Frame(ws, bg="white")
        MainFrame.place(relwidth=1, relheight=1)


        loadimage = PhotoImage(file="images/arrow.png")
        roundedbutton = Button(ws, image=loadimage, bg="white", borderwidth=0, bd=0, text="back",
                               command=lambda: backPageExistUser())
        roundedbutton.image=loadimage
        tooltip.CreateToolTip(roundedbutton, text='חזור')
        roundedbutton.place(relx=0.03, rely=0.02, relwidth=0.07,
                            relheight=0.09,anchor="n")

        title=Label(
            ws,
            text="Post-Save ברוכים הבאים ל ",
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
        label.place(relx = 0.47, rely = 0.93, anchor = "n")

        img = PhotoImage(file="images/git.png")
        linkGit = Button(ws, image=img, bg="white", borderwidth=0,
                      command=lambda :webbrowser.open_new("https://github.com/elishevada/final_project"))
        linkGit.image = img
        tooltip.CreateToolTip(linkGit, text='GitHub')
        linkGit.place(relx = 0.627, rely = 0.915, anchor="n")



def GoToPosts(username,password):
    try:#try to insert to table if yes so its doesnt exist so  we delete because we need to  check in facebook if valid
        db.insert_user_try(username,password)
        # conn = sqlite3.connect('images/projectManagment.db')
        # conn.execute("INSERT INTO users (UserName,Password,Name) VALUES (?,?,?)", (username, password, "try"));
        # conn.commit()
        #
        # conn.execute(f"DELETE from users WHERE UserName = '{username}'");
        # conn.commit()
        #
        # conn.close()
    except:
        messagebox.showwarning("this user already exists pls go to  exist user")
        lablePopup("המשתמש קיים חזור לעמוד קודם ", "back")
        return




    FS = login.login_facebook(username, password)

    FS.login()
    if(FS.check_validation()):#if its a right user
        #get the name with selenium
        name=FS.getName()
        #insert to database the username and password
        try:
            db.insert_user(username, password, name)
            # conn = sqlite3.connect('images/projectManagment.db')
            # conn.execute("INSERT INTO users (UserName,Password,Name) VALUES (?,?,?)",(username,password,name));
            # conn.commit()
            # conn.close()
            userPass.setPass(password)
            userPass.setUser(username)
            userPass.setName(name)
            FS.closeBrowser()
            lablePopup(">נרשמת למערכת בהצלחה ,לכניסה "  ,"foward")

        except:# ValueError as e print(e)
            FS.closeBrowser()
            messagebox.showwarning("error","problem to insert user")
            # lablePopup("המשתמש קיים חזור לעמוד קודם ","back")

    else:
        FS.closeBrowser()
        messagebox.showerror("Error", "password or username are wrong try again")#or forbidden



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

print("Run from main")

ws=Tk()
p1 = PhotoImage(file='images/facebook_icon.png')
#
# # Setting icon of master window
ws.iconphoto(False, p1)
Start = NewUserStart(ws)

ws.mainloop()

