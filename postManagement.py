import time
import webbrowser
# from doctest import master
from tkinter import *
# from tkinter.ttk import Separator

# ws = Tk()
# ws.title('WA-existUser')
#
# ws.geometry('{}x{}'.format(1000, 700))
from tkinter.ttk import Separator

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import tooltip
import userPass

second_frame=0

class postManager(Tk):

    def __init__(self, ws):
        global second_frame


        print(userPass.getUser())
        print(userPass.getPass())


        #########scrolld frame

        # create mainframe
        MainFrame = Frame(ws)
        MainFrame.pack(fill=BOTH, expand=1)

        canvas = Canvas(MainFrame)
        canvas.pack(side=LEFT,fill=BOTH, expand=1)

        my_scroll=ttk.Scrollbar(MainFrame,orient=VERTICAL,command=canvas.yview)
        my_scroll.pack(side=RIGHT,fill=Y)


        canvas.configure(yscrollcommand=my_scroll.set)
        canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

        second_frame=Frame(canvas)

        canvas.create_window((0,0),window=second_frame,anchor="nw")



        # Creating menubar
        menubar = Menu(second_frame)
        ws.config(menu=menubar)

        # Adding file menu and commands
        file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = file)
        file.add_command(label ='New File', command = None)
        file.add_command(label ='Run', command = None)
        file.add_command(label ='Save', command = None)
        file.add_separator()
        file.add_command(label ='Exit', command = ws.destroy)

        # Adding Edit Menu and commands
        edit = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Edit', menu = edit)
        edit.add_command(label ='Cut', command = None)
        edit.add_command(label ='Copy', command = None)
        edit.add_command(label ='Paste', command = None)
        edit.add_command(label ='Select All', command = None)
        edit.add_separator()
        edit.add_command(label ='Find...', command = None)
        edit.add_command(label ='Find again', command = None)

        # Adding Help Menu
        help_ = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Help', menu = help_)
        help_.add_command(label ='Help', command = None)
        help_.add_command(label ='Tutorials', command = None)
        help_.add_separator()
        help_.add_command(label ='About WA', command = None)
        help_.add_command(label ='Information', command = None)






        f1 = Frame(second_frame, background="white", width=1000, height=250)

        f1.grid(row=0, columnspan=10, sticky="nsew")

        for i in range(10):
            second_frame.rowconfigure(i, weight=1)
            second_frame.columnconfigure(i, weight=1)

        loadimage = PhotoImage(file="poweroff.png")
        roundedbutton = Button(f1, image=loadimage,bg="white",borderwidth=0,highlightthickness = 0, bd = 0,text="Quit",
                           command=ws.destroy)
        tooltip.CreateToolTip(roundedbutton, text = 'Power Off')
        roundedbutton.place(relx=0.03, rely=0.01, relwidth=0.05,
                     relheight=0.15, anchor="n")

        title=Label(
            f1,
            text=":)מה תרצה/י למצוא",
            fg="black",
            bg="white",
            font=('Helvatical bold',20)
        )

        title.place(relx=0.5, rely=0.1, relwidth=0.4,
                                    relheight=0.1, anchor="n")


        ListFrame = Frame(f1, bg="lightgrey", bd=3)
        ListFrame.place(relx=0.4, rely=0.25, relwidth=0.4,
                        relheight=0.15, anchor="n")
        List = Entry(ListFrame, font=40,justify="right")
        List.insert(0, "תכניס נושא חיפוש")
        List.place(relwidth=1, relheight=1)

        title=Label(
            f1,
            text=":כמות הפוסטים",
            fg="black",
            bg="white",
            font=('Helvatical bold',15)
        )

        title.place(relx=0.75, rely=0.25, relwidth=0.3,
                                    relheight=0.15, anchor="n")


        PostInput = Spinbox(f1, from_= 1, to = 10, font = 13)
        PostInput.place(relx=0.65, rely=0.25, relwidth=0.05,
                     relheight=0.15, anchor = "n")



        button1Frame = Frame(f1,bg="lightgray", bd=3)
        button1Frame.place(relx=0.5, rely=0.45, relwidth=0.4,
                        relheight=0.15, anchor="n")




        button1 = Button(button1Frame, text="חפש לי",bg="lightblue",
                           command=ws.destroy)

        button1.place(relwidth=1, relheight=1)





        title=Label(
            f1,
            text=":מציג תוצאות עבור מילת חיפוש",
            fg="black",
            bg="white",
            font=('Helvatical bold',15)
        )

        title.place(relx=0.5, rely=0.85, relwidth=0.3,
                                    relheight=0.1, anchor="n")


        l3 = Label(second_frame,text="קישור לפוסט",height=1,font=('Helvatical bold',15),borderwidth = 2,relief="raised")
        l3.grid(row=1, column=0, sticky='NESW')
        l2 = Label(second_frame,text="כותב",font=('Helvatical bold',15),borderwidth = 2,relief="raised")
        l2.grid(row=1, column=1, sticky='NESW')
        l4 = Label(second_frame,text="תאריך פרסום",font=('Helvatical bold',15),borderwidth = 2,relief="raised")
        l4.grid(row=1, column=2, sticky='NESW')
        l1 = Label(second_frame,text="תוכן",font=('Helvatical bold',15),borderwidth = 2,relief="raised")
        l1.grid(row=1, column=3, sticky='NESW')
        l0 = Label(second_frame,text="הערות לפוסט",font=('Helvatical bold',15),borderwidth = 2,relief="raised")
        l0.grid(row=1, column=4, sticky='NESW')



ws = Tk()
ws.geometry('1000x700')
ws.title('WA-newUser')
Start = postManager(ws)


save1image = PhotoImage(file="save1.png")

for i in range(2,10):
    set3 =Label(second_frame, text="קישור לפוסט", fg="blue",borderwidth = 1,relief="sunken", cursor="hand2",bg="lightgray")
    set3.configure(font='fangsongti')
    set3.grid(column=0, row=i, sticky='NESW')

    set3.bind("<Button-1>", lambda e: callback("https://www.facebook.com"))

    set = Text(second_frame, height=6,
                   width=10,
                   bg="lightgray" , wrap=WORD)
    set.configure(font=('Helvatical bold',12))
    set.tag_configure("right", justify='right')
    set.grid(column=1, row=i, sticky='NESW')
    set.insert(END,"יידידיידידידיידידיידיד")
    set.tag_add("right", "1.0", "end")
    set.configure(state='disabled')

    set = Text(second_frame, height=2,
                   width=10,
                   bg="lightgray", wrap=WORD )
    set.configure(font=('Helvatical bold',12))
    set.tag_configure("right", justify='right')
    set.grid(column=2, row=i, sticky='NESW')
    set.insert(END,"יידידיידידידיידידיידיד")
    set.tag_add("right", "1.0", "end")
    set.configure(state='disabled')

    set = ScrolledText(second_frame, height=1,
                   width=30,
                   bg="lightgray" , wrap=WORD)
    set.configure(font=('Helvatical bold',12))
    set.tag_configure("right", justify='right')
    set.grid(column=3, row=i, sticky='NESW')
    set.insert(END,"היי.."\
"שולחן מעץ אורן 90% ממוחזר." \
"מחפש המלצה לטיפול לתנאי פנים. יש פה ושם מעט תיקונים קטנים עם שפכטל עץ. בגדול מעדיף מראה כמה שיותר קרוב לצבע המקורי אבל מניח שיהיה שינוי, אז מחפש משהו פחות צהוב. יהיה נחמד גם קצת ברק לא מאוד מוגזם. יש לי ניירות שיוף עד 400 כרגע"\
" תודהרבה ")
    set.tag_add("right", "1.0", "end")
    set.configure(state='disabled')


    set = Text(second_frame, height=2,
                   width=20,
                   bg="lightgray", wrap=WORD)
    set.configure(font=('Helvatical bold',12))
    set.tag_configure("right", justify='right')
    set.grid(column=4, row=i, sticky='NESW')
    set.tag_add("right", "1.0", "end")



    save1button = Button(second_frame,image=save1image,borderwidth=0,
                       command=lambda k = i: button_index(k))
    save1button.grid(column=5, row=i, sticky='NESW')
    tooltip.CreateToolTip(save1button, text = 'Save post for later')





def button_index(k):
    print(k)


def callback(url):
    webbrowser.open_new(url)


ws.mainloop()









