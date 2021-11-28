import sqlite3

from tkinter import *

from tkinter import messagebox
from tkinter.ttk import Separator

import helpClass


import webbrowser



import tooltip
import userPass

cameback=False


class ExistUserStart(Tk):

    def __init__(self,ws):
        global cameback

        menubar = Menu(ws)
        ws.config(menu=menubar)

        # Adding file menu and commands
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="כלים", menu=file)
        file.add_command(label='מחק משתמש', command=lambda :delete_update_user(0))
        file.add_command(label='עדכן סיסמא', command=lambda: delete_update_user(1))
        file.add_separator()
        file.add_command(label='יציאה', command=lambda :ws.destroy)

        # Adding Help Menu
        help_ = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='עזרה', menu=help_)
        help_.add_command(label='הוראות שימוש', command=lambda :helpClass.help(ws))
        help_.add_command(label='חומרי הפרויקט', command=lambda :helpClass.tutorials(ws))

        help_.add_command(label='אודות ', command=lambda :helpClass.about(ws))
        help_.add_separator()
        help_.add_command(label='על התוכנה', command=lambda :helpClass.info(ws))


        ws.title('WA-משתמש קיים')
        canvas = Canvas(ws, height=700, width=1000)
        canvas.pack()

        MainFrame = Frame(ws, bg="white")
        MainFrame.place(relwidth=1, relheight=1)

        title=Label(
            ws,
            text="Post-Save ברוכים הבאים ל ",
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

        if(cameback==False):#if the user came back from the new user page disable this because it runs from import
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
        label.place(relx = 0.47, rely = 0.93, anchor = "n")

        img = PhotoImage(file="images/git.png")
        linkGit = Button(ws, image=img, bg="white", borderwidth=0,
                         command=lambda: webbrowser.open_new("https://github.com/elishevada/final_project"))
        linkGit.image = img
        tooltip.CreateToolTip(linkGit, text='GitHub')
        linkGit.place(relx=0.627, rely=0.915, anchor="n")









def delete_update_user(flag):
    passFrame=0
    Password=0
    if(flag==0):
        textIn="שם משתמש למחיקה"
        textB="מחק"
    else:
        textIn = "שם משתמש לעידכון"
        textB="עדכן"

        passFrame = Frame(ws, bg="white", bd=1)
        passFrame.place(relx=0.15, rely=0.08, relwidth=0.3, relheight=0.05, anchor="n")
        Password = Entry(passFrame,show="*", font=40, justify="right")
        Password.insert(0, "סיסמא לעידכון")
        Password.place(relwidth=1, relheight=1)

        Password.focus()


    UsernameFrame = Frame(ws, bg="white", bd=1)
    UsernameFrame.place(relx=0.15, rely=0.01,relwidth=0.3, relheight=0.05, anchor="n")
    Username = Entry(UsernameFrame, font=40, justify="right")
    Username.insert(0, textIn)
    Username.place(relwidth=1, relheight=1)

    Username.focus()

    button = Button(ws, text=textB, bg="lightblue",
                    command=lambda: deleteUpdateFor(Username.get(),Username,button,button2,flag,Password,Password))

    button.place(relx=0.36, rely=0.01, relwidth=0.1,
                 relheight=0.05, anchor="n")

    button2 = Button(ws, text="ביטול", bg="lightblue",
                     command=lambda: remove(flag,Username, button, button2,Password))
    button2.place(relx=0.469, rely=0.01, relwidth=0.1,
                     relheight=0.05, anchor="n")

def deleteUpdateFor(userToDeleteOrUpdate, w1, w2, w3, flag,UpdatePass,w4Update):
    if(flag==0):
        MsgBox = messagebox.askquestion('Delete user', 'Are you sure you want to be deleted warning:all the history will deleted too')
        if MsgBox == "yes":
            try:
                conn = sqlite3.connect('images/projectManagment.db')
                conn.execute("PRAGMA foreign_keys = 1")
                cur = conn.cursor()
                cursur=cur.execute(f"SELECT * FROM users  WHERE UserName='{userToDeleteOrUpdate}'");#for checking bcs the delete doesnt returns error if not exist
                cursur.fetchone()[0]
                cur.execute(f"DELETE from users WHERE UserName = '{userToDeleteOrUpdate}'");

                conn.commit()
                conn.close()
                remove(flag,w1, w2, w3,w4Update)

            except:
                messagebox.showwarning("this user doesnt exist for delete")
    else:
        MsgBox = messagebox.askquestion('update pass',
                                        'Are you sure you want to update?')
        if MsgBox == "yes":
            try:
                conn = sqlite3.connect('images/projectManagment.db')
                conn.execute("PRAGMA foreign_keys = 1")
                cur = conn.cursor()
                cursur = cur.execute(
                    f"SELECT * FROM users  WHERE UserName='{userToDeleteOrUpdate}'");  # for checking bcs the delete doesnt returns error if not exist
                cursur.fetchone()[0]
                cur.execute(f"UPDATE users SET Password='{UpdatePass.get()}' WHERE UserName = '{userToDeleteOrUpdate}'");

                conn.commit()
                conn.close()
                remove(flag,w1, w2, w3,w4Update)

            except:
                messagebox.showwarning("this user doesnt exist for update")



def remove(flag,widget1, widget2,widget3,widget4):
    widget1.place_forget()
    widget2.place_forget()
    widget3.place_forget()
    if(flag==1):
        widget4.place_forget()

def GoToPosts(user):

    try:
        conn = sqlite3.connect('images/projectManagment.db')
        cursor=conn.execute(f"SELECT Password,Name FROM users  WHERE UserName='{user}'");
        userInfo=cursor.fetchall()[0]
        userPass.setName(userInfo[1])
        userPass.setPass(userInfo[0])
        userPass.setUser(user)
        conn.close()
        ws.destroy()
        import postManagement
    except:
        messagebox.showwarning("Error","this user is not exist for select")





def nextPageNewUser():
    ws.destroy()
    import newUser

def disable_event():
    pass




if __name__ == "__main__":


    print("Run from main")
    conn = sqlite3.connect('images/projectManagment.db')
    # conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()
    # cur.execute('''CREATE TABLE users
    #                      (UserName TEXT PRIMARY KEY ,
    #                      Password           TEXT,
    #                      Name TEXT);''')
    # cur.execute('''CREATE TABLE topics
    #                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                  topic   TEXT  ,
    #                  UserName TEXT,
    #                  FOREIGN KEY (UserName) REFERENCES users (UserName)
    #                         ON UPDATE CASCADE
    #                         ON DELETE CASCADE
    #                   );''')
    # cur.execute('''CREATE TABLE posts
    #                  (
    #                  id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                  link        TEXT ,
    #                  writer         TEXT,
    #                  date TEXT ,
    #                  content TEXT,
    #                  comment TEXT,
    #                  subject            TEXT     NOT NULL,
    #                  UserName TEXT,
    #                  FOREIGN KEY (UserName) REFERENCES users (UserName)
    #                         ON UPDATE CASCADE
    #                         ON DELETE CASCADE);''')
    #
    # cur.execute("INSERT INTO users (UserName,Password,Name) VALUES (?,?,?)",(us,ps,"jj"));
    # for i in range(20):
    #     cur.execute("INSERT INTO topics  VALUES (?,?,?)",(None,i,us));
    # cur.execute("INSERT INTO posts  VALUES (?,?,?,?,?,?,?,?)", (None,"0link","1writer","2date","3content","4comment", "נושא5",us));
    # cur.execute("DELETE FROM users  WHERE UserName='5555'");
    # conn.commit()
    cursor = cur.execute("SELECT * from topics")
    print(cursor.fetchall())
    cursor = cur.execute("SELECT * from users")
    print(cursor.fetchall())
    cursor = cur.execute("SELECT * from posts")
    print(cursor.fetchall())
    conn.close()

    ws=Tk()
    # ws.protocol("WM_DELETE_WINDOW", disable_event)#----------important disable the window close with x ontop so we mannage the close program
    p1 = PhotoImage(file='images/facebook_icon.png')

    # Setting icon of master window
    ws.iconphoto(False, p1)
    Start = ExistUserStart(ws)
    ws.mainloop()
else:

    cameback=True
    print("Run from import")
    ws = Tk()
    p1 = PhotoImage(file='images/facebook_icon.png')

    # Setting icon of master window
    ws.iconphoto(False, p1)
    Start = ExistUserStart(ws)
    ws.mainloop()