import webbrowser
from tkinter import *



def image():
    # Creating object of photoimage class
    # in which script is saved
    p1 = PhotoImage(file='images/facebook_icon.png')
    return p1





def help(ws):
    top = Toplevel(ws)
    top.iconphoto(False, image())
    top.title('help')
    top.geometry("800x800")
    img = PhotoImage(file="images/intructions.png")
    userPanel = Label(top, image=img)
    userPanel.image = img
    userPanel.place(relx=0.5, rely=0, relwidth=1,
                    relheight=1, anchor="n")


def about(ws):
    top = Toplevel(ws)
    top.iconphoto(False, image())
    top.title('about')
    top.geometry("500x200")
    img = PhotoImage(file="images/about.png")
    userPanel = Label(top, image=img)
    userPanel.image = img
    userPanel.place(relx=0.5, rely=0, relwidth=1,
                    relheight=1, anchor="n")

def info(ws):
    top = Toplevel(ws)
    top.iconphoto(False, image())
    top.title('info')
    top.geometry("450x300")
    img = PhotoImage(file="images/info.png")
    userPanel = Label(top, image=img)
    userPanel.image = img
    userPanel.place(relx=0.5, rely=0, relwidth=1,
                    relheight=1, anchor="n")

def callback(url):
    webbrowser.open_new(url)

def tutorials(ws):
    top = Toplevel(ws)
    top.iconphoto(False, image())
    top.geometry('400x300')
    top.title('Tutorials')
    top.configure(bg="#FFF")



    title = Label(
        top,
        text="Tutorials",
        fg="black",
        bg="white",
        font=40
    )

    title.place(relx=0.5, rely=0.05, relwidth=0.6,
                relheight=0.1, anchor="n")

    title.config(font=('Helvatical bold', 20))

    title = Label(
        top,
        text="Python: ",
        fg="black",
        bg="white",
        font=40
    )

    title.place(relx=0.15, rely=0.3, relwidth=0.2,
                relheight=0.08, anchor="n")

    title.config(font=('Helvatical bold', 15))

    set3 = Label(top, text="python Tutorial", fg="blue", cursor="hand2", bg="white")
    set3.configure(font='fangsongti')

    set3.place(relx=0.4, rely=0.3, relwidth=0.35,
               relheight=0.08, anchor="n")
    set3.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/tutorial/"))

    title = Label(
        top,
        text="Selenium: ",
        fg="black",
        bg="white",
        font=40
    )

    title.place(relx=0.17, rely=0.4, relwidth=0.25,
                relheight=0.08, anchor="n")

    title.config(font=('Helvatical bold', 15))

    set3 = Label(top, text="Selenium Tutorial", fg="blue", cursor="hand2", bg="white")
    set3.configure(font='fangsongti')

    set3.place(relx=0.45, rely=0.4, relwidth=0.4,
               relheight=0.08, anchor="n")
    set3.bind("<Button-1>", lambda e: callback("https://selenium-python.readthedocs.io/"))

    title = Label(
        top,
        text="Sqlite: ",
        fg="black",
        bg="white",
        font=40
    )

    title.place(relx=0.15, rely=0.5, relwidth=0.2,
                relheight=0.08, anchor="n")

    title.config(font=('Helvatical bold', 15))

    set3 = Label(top, text="Sqlite Tutorial", fg="blue", cursor="hand2", bg="white")
    set3.configure(font='fangsongti')

    set3.place(relx=0.4, rely=0.5, relwidth=0.35,
               relheight=0.08, anchor="n")
    set3.bind("<Button-1>", lambda e: callback("https://www.sqlitetutorial.net/sqlite-python/"))

    title = Label(
        top,
        text="Threading: ",
        fg="black",
        bg="white",
        font=40
    )

    title.place(relx=0.17, rely=0.6, relwidth=0.27,
                relheight=0.08, anchor="n")

    title.config(font=('Helvatical bold', 15))

    set3 = Label(top, text="Threading Tutorial", fg="blue", cursor="hand2", bg="white")
    set3.configure(font='fangsongti')

    set3.place(relx=0.48, rely=0.6, relwidth=0.4,
               relheight=0.08, anchor="n")

    set3.bind("<Button-1>", lambda e: callback("https://www.geeksforgeeks.org/multithreading-python-set-1/"))

    title = Label(
        top,
        text="Tkinter: ",
        fg="black",
        bg="white",
        font=40
    )

    title.place(relx=0.15, rely=0.7, relwidth=0.2,
                relheight=0.08, anchor="n")

    title.config(font=('Helvatical bold', 15))

    set3 = Label(top, text="Tkinter Tutorial", fg="blue", cursor="hand2", bg="white")
    set3.configure(font='fangsongti')

    set3.place(relx=0.4, rely=0.7, relwidth=0.35,
               relheight=0.08, anchor="n")
    set3.bind("<Button-1>", lambda e: callback("https://www.geeksforgeeks.org/python-tkinter-tutorial/"))

    title = Label(
        top,
        text="GoodLuck!!",
        fg="black",
        bg="white",
        font=40
    )

    title.place(relx=0.5, rely=0.9, relwidth=0.6,
                relheight=0.1, anchor="n")

    title.config(font=('Helvatical bold', 15))























