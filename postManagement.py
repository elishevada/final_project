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

# import click as click


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)



root = Tk()
root.geometry("1000x700")
# MainFrame = Frame(root)
# MainFrame.place(relwidth=1, relheight=1)


#########scrolld frame
# create mainframe
MainFrame = Frame(root)
MainFrame.pack(fill=BOTH, expand=1)

canvas = Canvas(MainFrame)
canvas.pack(side=LEFT,fill=BOTH, expand=1)

my_scrool=ttk.Scrollbar(MainFrame,orient=VERTICAL,command=canvas.yview)
my_scrool.pack(side=RIGHT,fill=Y)


canvas.configure(yscrollcommand=my_scrool.set)
canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

second_frame=Frame(canvas)

canvas.create_window((0,0),window=second_frame,anchor="nw")
##########


# for i in range(100):
#     Button(second_frame,text="gdyhg").grid(row=i)



# Creating menubar
menubar = Menu(second_frame)
root.config(menu=menubar)

# Adding file menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Run', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)#--------------------------------------------------------------------------

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
# f2 = Frame(root, background="pink", width=1000, height=500)

f1.grid(row=0, columnspan=10, sticky="nsew")
# f2.grid(row=1, column=0, sticky="nsew")

for i in range(10):
    second_frame.rowconfigure(i, weight=1)
    second_frame.columnconfigure(i, weight=1)

loadimage = PhotoImage(file="poweroff.png")
roundedbutton = Button(f1, image=loadimage,bg="white",borderwidth=0,highlightthickness = 0, bd = 0,text="Quit",
                   command= root.destroy)
CreateToolTip(roundedbutton, text = 'Power Off')
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
                   command=root.destroy)

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
                   bg="lightgray", wrap=WORD )
    set.configure(font=('Helvatical bold',12))
    set.tag_configure("right", justify='right')
    set.grid(column=4, row=i, sticky='NESW')
    set.tag_add("right", "1.0", "end")

    save1image = PhotoImage(file="save1.png")
    save1button = Button(second_frame, image=save1image,bg="#f0f0f0",borderwidth=0,highlightthickness = 0, bd = 0,text="Quit",
                       )
    CreateToolTip(save1button, text = 'Save post for later')
    save1button.grid(column=5, row=i, sticky='NESW')
    # # Here binding click method with mouse
    # save1button.bind("<Button-1>", click(save1button))


def click(event):
    # Here retrieving the size of the parent
    # widget relative to master widget
    x = event.x_root - second_frame.winfo_rootx()
    y = event.y_root - second_frame.winfo_rooty()

    # Here grid_location() method is used to
    # retrieve the relative position on the
    # parent widget
    z = second_frame.grid_location(x, y)

    # printing position
    print(z)



def callback(url):
    webbrowser.open_new(url)


root.mainloop()








