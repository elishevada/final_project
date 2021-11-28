import sqlite3
import threading
import time
import webbrowser


from tkinter.ttk import Separator

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, messagebox
import tooltip
import userPass
import login
import helpClass

second_frame=0
login_flag=0
driver=1
MainFrame=0
comments=[]
commentssaved=[]
currUser=""
currPass=""
currName=""
f1=0
num_les_flag=False
pop=0


class postManager(Tk):

    def __init__(self, ws):
        global List
        global second_frame
        global MainFrame
        global currPass
        global currUser
        global currName
        global f1
        #get the user that just loged in
        currUser=userPass.getUser()
        currPass=userPass.getPass()
        currName=userPass.getName()

        print(currUser)
        print(currPass)
        print(currName)


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
        menubar.add_cascade(label = "כלים", menu = file)
        file.add_command(label ='כל השמורים', command = lambda :store_all_saved())
        file.add_command(label='שמורים עבור נושא', command=lambda :open_save_dialog())
        file.add_command(label='היסטוריית חיפושים', command=lambda: show_search_history())
        file.add_command(label='איתחול הדף', command=lambda: reset_page())
        file.add_separator()
        file.add_command(label ='יציאה', command = ws.destroy)



        # Adding Help Menu
        help_ = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='עזרה', menu = help_)
        help_.add_command(label ='הוראות שימוש', command = lambda :helpClass.help(ws))
        help_.add_command(label ='חומרי הפרויקט', command = lambda :helpClass.tutorials(ws))

        help_.add_command(label ='אודות ', command = lambda :helpClass.about(ws))
        help_.add_separator()
        help_.add_command(label ='על התוכנה', command = lambda :helpClass.info(ws))

        # Adding Edit Menu and commands
        edit = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='ערוך', menu=edit)



        f1 = Frame(second_frame, background="white", width=1000, height=250)

        f1.grid(row=0, columnspan=10, sticky="nsew")

        for i in range(10):
            second_frame.rowconfigure(i, weight=1)
            second_frame.columnconfigure(i, weight=1)



        name_user = Label(
            f1,
            text=currName,
            fg="black",
            bg="white",
            anchor="e",
            font=('Helvatical bold', 15)
        )
        name_user.place(relx=0.77, rely=0.01, relwidth=0.3,
                    relheight=0.18, anchor="n")

        # user name
        img = PhotoImage(file="images/user.png")
        userPanel = Label(f1, image=img)
        userPanel.image = img
        userPanel.place(relx=0.95, rely=0.01, relwidth=0.05,
                        relheight=0.18, anchor="n")

        loadimage = PhotoImage(file="images/poweroff.png")
        roundedbutton = Button(f1, image=loadimage,bg="white",borderwidth=0,highlightthickness = 0, bd = 0,text="Quit",
                           command=lambda :self.close_all_opened())
        roundedbutton.image=loadimage
        tooltip.CreateToolTip(roundedbutton, text = 'כיבוי')
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

        historyimage = PhotoImage(file="images/history.png")
        historybutton = Button(f1, image=historyimage, bg="white", borderwidth=0, highlightthickness=0, bd=0, text="Quit",
                               command=lambda: show_search_history())
        historybutton.image = historyimage
        tooltip.CreateToolTip(historybutton, text='היסטוריה')
        historybutton.place(relx=0.18, rely=0.25, relwidth=0.05,
                            relheight=0.15, anchor="n")




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



        button1 = Button(button1Frame, text="חפש לי", bg="lightblue",
                         command=lambda :threading.Thread(target=self.user_login, args=((int)(PostInput.get()),List.get(), currUser,currPass)).start())

        button1.place(relwidth=1, relheight=1)





        title=Label(
            f1,
            text=":מציג תוצאות עבור נושא חיפוש",
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


    def user_login(self,numOfPosts,search_topic,user,pas):

        global login_flag
        global driver

        if(login_flag==0):
            LF = login.login_facebook(user, pas)
            driver=LF.driver
            LF.login()
            if(LF.check_validation()):#to check if the password had updated
                login_flag=1
                self.store_post_information(numOfPosts,search_topic,user,pas)
            else:
                messagebox.showerror("error","you probably changed your password in facebook you need to update")
        else:
            self.store_post_information(numOfPosts, search_topic, user, pas)


    def store_post_information(self,numOfPosts,search_topic,user,pas):
        global login_flag
        global num_les_flag
        num_les_flag=False
        # check if the search topic valid
        if(valid(search_topic)==0):
            # save the search word in the topics table
            add_topic_to_records(search_topic)


            global driver

            try:#if the user closed the driver
                driver.get("https://www.facebook.com/search/posts/?q=" + search_topic)
            except:
                login_flag=0
                self.user_login(numOfPosts, search_topic, user, pas)


            time.sleep(3)



            posts = driver.find_elements_by_xpath(
                "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']")
            posts = [elem.get_attribute('href') for elem in
                     posts]
            print(len(posts))
            if(len(posts)>0):
                if(len(posts)<numOfPosts):
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    time.sleep(2)
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    posts = driver.find_elements_by_xpath(
                        "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']")
                    posts = [elem.get_attribute('href') for elem in
                             posts]

                print(len(posts))
                if (len(posts) < numOfPosts):#after we scrooled and still less
                    num_les_flag = True#f"probebly there are less {numOfPosts} than posts      "

                posts_date = []
                posts_content = []
                posts_Links = []
                posts_writers = []

                date = ""
                i = 0
                for post in posts:
                    content = " "
                    if (i < numOfPosts):
                        driver.get(post)
                        time.sleep(1)
                        posts_Links.append(driver.current_url)
                        # print(posts_Links[i])
                        time.sleep(1)
                        try:
                            dateTags = driver.find_elements_by_xpath(
                                "//span[@class='j1lvzwm4 stjgntxs ni8dbmo4 q9uorilb gpro0wi8']/b/b")
                            print(len(dateTags))
                            list_classes = []
                            for tag in dateTags:
                                list_classes.append(tag.get_attribute("class"))


                            shortest_string = find_min(list_classes)
                            print(shortest_string)
                            place_of_short_string = list_classes.index(shortest_string)
                            date = dateTags[place_of_short_string].text

                        except:
                            try:
                                date = driver.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi b1v8xokw m9osqain hzawbc8m']/span/span[2]/span")[0].text
                            except:
                                date="default"
                        posts_date.append(date)
                        print(posts_date[i])

                        allPostContent = driver.find_elements_by_xpath(
                            "//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q']/div[@dir='auto']")
                        for sentence in allPostContent:
                            content = content + sentence.text
                            content = content + " "
                        if (content == " "):#if there is no content due to a picture or video
                            content = "וידאו או תמונה"
                            print(content)
                        posts_content.append(content)
                        print(posts_content[i])
                        post_writer = driver.find_element_by_xpath("//span[@class='nc684nl6']//span")
                        class_exist = post_writer.get_attribute("class")
                        if (len(class_exist) > 0):  # there are two elements at the same path so we want the second one
                            post_writer = driver.find_elements_by_xpath("//span[@class='nc684nl6']//span")
                            post_writer = post_writer[1].text
                        else:
                            post_writer = post_writer.text
                        print(post_writer)
                        if (post_writer == ""):
                            post_writer = "פוסט ציבורי"
                            print(post_writer)
                        posts_writers.append(post_writer)
                        driver.back()
                        time.sleep(1)
                        i = i + 1
                self.insert_to_table(posts_Links, posts_content, posts_date, posts_writers, search_topic, numOfPosts)
            else:
                messagebox.showwarning("Warning",f"There are no posts to show for {search_topic}  or you did a new search     ")


        else:
            messagebox.showerror("Warning","The search topic must contain letters or numbers")


    def insert_to_table(self,posts_links,posts_contents,posts_date,posts_writer,search_topic,numOfPosts):
        num_of_posts = len(posts_links)
        # befor printing to the screen clear the grid and show in the labe the search topic and the number
        reset_page()
        setTitleForWord(f"מציג  {num_of_posts} תוצאות עבור  {search_topic}")
        global comments
        comments=[]
        save1image = PhotoImage(file="images/save1.png")

        posts_details=[posts_links,posts_writer,posts_date,posts_contents]
        for i in range(2,num_of_posts+2):

            link = Button(second_frame, text="קישור לפוסט", bg="lightgray",fg="blue", borderwidth=1, font=('Helvatical bold', 15),relief="sunken",cursor="hand2",
                            command=lambda e=i-2: callback(posts_links[e]))

            link.grid(column=0, row=i, sticky='NESW')



            set = Text(second_frame, height=6,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=1, row=i, sticky='NESW')
            set.insert(END, posts_writer[i-2])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            set = Text(second_frame, height=2,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=2, row=i, sticky='NESW')
            set.insert(END, posts_date[i-2])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            set = ScrolledText(second_frame, height=1,
                               width=30,
                               bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=3, row=i, sticky='NESW')
            set.insert(END, posts_contents[i-2])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            set = Text(second_frame, height=2,
                       width=20,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=4, row=i, sticky='NESW')
            set.tag_add("right", "1.0", "end")
            comments.append(set)#in order to save the widget of the comment for saving the post


            save1button = Button(second_frame, image=save1image, borderwidth=0,
                                 command=lambda k=i: insert_post(k,posts_details,search_topic))
            save1button.image = save1image
            save1button.grid(column=5, row=i, sticky='NESW')
            tooltip.CreateToolTip(save1button, text='לשמור פוסט')

        if(num_les_flag):
            messagebox.showwarning("Warning", f"probebly there are less {numOfPosts} than posts      ")






    def close_all_opened(self):
        global login_flag
        global  driver
        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            try:#check if driver is still open
                driver.get("https://www.facebook.com/")
                driver.close()
                ws.destroy()
            except:
                ws.destroy()


        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')

def disable_event():
    pass

ws = Tk()
ws.protocol("WM_DELETE_WINDOW",
            disable_event)  # ----------important disable the window close with x ontop so we mannage the close program

# Creating object of photoimage class
# in which script is saved
p1 = PhotoImage(file='images/facebook_icon.png')

# Setting icon of master window
ws.iconphoto(False, p1)
ws.geometry('1000x700')
ws.title('WA-ניהול פוסטים')
Start = postManager(ws)



def setTitleForWord(str):
    global f1
    title = Label(
        f1,
        text=str,
        fg="black",
        bg="white",
        font=('Helvatical bold', 15)
    )

    title.place(relx=0.5, rely=0.85, relwidth=0.6,
                relheight=0.1, anchor="n")






def valid(topic):#validation of search word
    if(topic=="" or topic=="$"): #or topic=="תכניס נושא לחיפוש"  sometimes there are post for this topic
        return 1
    return 0

def find_min(list_search):#a function to find the minimum out of a list of classes bcs the smallest strings returns the date of post

    x = "l94mrbxd.aenfhxwr.myohyog2.b6zbclly.l9j0dhe7.sdhka5h4.nw7X6Rf if you see this autput probably its a new acount"
    for i in list_search:
        if (len(i) < len(x)):#the min string frome the list
            x = i
            if (x.endswith('h4') == True):#this is for if thre are few posts at the same page so it will bring  the first
                return x
    if(x.endswith('h4')==True):#if it is the date path return because usually it shorter then the others
        return x
    else:
        for right in list_search:#if the date path is longer than the others
            if(right.endswith('h4')==True):
                return right
    return x






def insert_post(k,posts_details,search_topic):#insert the post choosen to the saved
    global comments
    global currUser
    comment_text=comments[k-2].get("1.0", "end")
    conn = sqlite3.connect('images/projectManagment.db')
    try:
        cursor = conn.execute(f"SELECT link,UserName FROM posts  WHERE link='{posts_details[0][k-2]}' AND UserName='{currUser}'");#if the post saved
        help = cursor.fetchall()[0]
        a=help[1]
        q=messagebox.askquestion("Error", "This post is already saved do you want to delete the old and save the new")
        if(q=="yes"):
            conn.execute(f"DELETE from posts WHERE link = '{posts_details[0][k-2]}' AND UserName='{currUser}'");

            conn.execute(
                "INSERT INTO posts (id,link,writer,date,content,comment,subject,username) VALUES (?,?,?,?,?,?,?,?)", (
                    None, posts_details[0][k - 2], posts_details[1][k - 2], posts_details[2][k - 2],
                    posts_details[3][k - 2],
                    comment_text, search_topic, currUser));
            conn.commit()

    except:
        conn.execute("INSERT INTO posts (id,link,writer,date,content,comment,subject,username) VALUES (?,?,?,?,?,?,?,?)", (
        None, posts_details[0][k - 2], posts_details[1][k - 2], posts_details[2][k - 2], posts_details[3][k - 2],
        comment_text, search_topic, currUser));
        conn.commit()
    conn.close()

    print(k)




def store_all_saved():
    global currUser
    reset_page()#delete all the posts from screen

    conn = sqlite3.connect('images/projectManagment.db')
    cursor = conn.execute(f"SELECT * FROM posts  WHERE UserName='{currUser}'");

    print_saved(cursor.fetchall(),"$")#print on screen
    conn.close()



def open_save_dialog():
    wordFrame = Frame(ws, bg="white", bd=1)
    wordFrame.place(relx=0.15, rely=0.01, relwidth=0.2, relheight=0.05, anchor="n")
    word = Entry(wordFrame, font=40, justify="right")
    word.insert(0, "מה תרצה לחפש?")
    word.place(relwidth=1, relheight=1)
    word.focus()

    button = Button(ws, text="הראה שמורים", bg="lightblue",
                    command=lambda: store_all_saved_for_topic(word.get()))

    button.place(relx=0.3, rely=0.01, relwidth=0.08,
                 relheight=0.03, anchor="n")

    button2 = Button(ws, text="ביטול", bg="lightblue",
                     command=lambda: remove(word, button, button2))
    button2.place(relx=0.38, rely=0.01, relwidth=0.06,
                 relheight=0.03, anchor="n")





def remove(widget1, widget2, widget3):
    widget1.place_forget()
    widget2.place_forget()
    widget3.place_forget()




def store_all_saved_for_topic(search_topic):
    s = "%"
    s += search_topic
    s += "%"
    global currUser
    reset_page()

    conn = sqlite3.connect('images/projectManagment.db')
    cursor = conn.execute(f"SELECT * FROM posts  WHERE UserName='{currUser}' AND subject LIKE '{s}'");

    # print on screen
    print_saved(cursor.fetchall(),search_topic)
    conn.close()

def delAllPosts(if_topic):
    s = "%"
    s += if_topic
    s += "%"

    MsgBox = messagebox.askquestion('Delete all',
                                    'Are you sure you want to  delete all posts')
    if(MsgBox=="yes"):
        global currUser
        conn = sqlite3.connect('images/projectManagment.db')
        if(if_topic=="$"):#delete all
            conn.execute(f"DELETE  FROM posts  WHERE UserName='{currUser}'");
        else:#delete for topic
            conn.execute(f"DELETE  FROM posts  WHERE UserName='{currUser}' AND subject LIKE '{s}'");
        conn.commit()
        conn.close()
        reset_page()


def createBuToDelAll(if_topic):
    global f1
    delimage = PhotoImage(file="images/delall.png")
    delbutton = Button(f1, image=delimage,bg="white",borderwidth=0,highlightthickness = 0, bd = 0,text="Quit",
                       command=lambda :delAllPosts(if_topic))
    delbutton.image=delimage
    tooltip.CreateToolTip(delbutton, text = 'למחוק הכל')
    delbutton.place(relx=0.92, rely=0.85, relwidth=0.3,
                 relheight=0.15, anchor="n")




def print_saved(list_saved,if_topic):

    global commentssaved
    commentssaved = []

    if(len(list_saved)!=0):
        createBuToDelAll(if_topic)
        list_saved.reverse()
        updateimage = PhotoImage(file="images/update.png")
        deleteimage = PhotoImage(file="images/delete.png")
        if (if_topic == "$"):
            setTitleForWord("מציג את כל השמורים")
        else:
            setTitleForWord(f"מציג את כל השמורים עבור{if_topic}")
        for i in range(2,2+len(list_saved)):
            link = Button(second_frame, text="קישור לפוסט", bg="lightgray", fg="blue", borderwidth=1,#link doesnt work
                          font=('Helvatical bold', 15), relief="sunken", cursor="hand2",
                          command=lambda e=list_saved[i - 2][1]: callback(e))

            link.grid(column=0, row=i, sticky='NESW')

            set = Text(second_frame, height=6,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=1, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][2])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            set = Text(second_frame, height=2,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=2, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][3])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            set = ScrolledText(second_frame, height=1,
                               width=30,
                               bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=3, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][4])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            setcom = Text(second_frame, height=2,
                       width=15,
                       bg="lightgray", wrap=WORD)
            setcom.configure(font=('Helvatical bold', 12))
            setcom.tag_configure("right", justify='right')
            setcom.grid(column=4, row=i, sticky='NESW')
            setcom.insert(END, list_saved[i - 2][5])
            setcom.tag_add("right", "1.0", "end")
            commentssaved.append(setcom)

            set = Text(second_frame, height=2,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=5, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][6])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            l0 = Label(second_frame, text="נושא הפוסט", font=('Helvatical bold', 15), borderwidth=2, relief="raised")
            l0.grid(row=1, column=5, sticky='NESW')

            updatebutton = Button(second_frame,image=updateimage, text="up", borderwidth=0,
                                 command=lambda e=i-2:updatePostComment(commentssaved[e].get("1.0", "end"),list_saved[e][1],if_topic,list_saved[e][7]))
            updatebutton.image = updateimage
            updatebutton.grid(column=6, row=i, sticky='NESW')
            tooltip.CreateToolTip(updatebutton, text='עידכון פוסט')

            deletebutton = Button(second_frame,image=deleteimage, text="del", borderwidth=0,
                                 command=lambda e=i-2 :deletePost(list_saved[e][1],if_topic,list_saved[e][7]))
            deletebutton.image = deleteimage
            deletebutton.grid(column=7, row=i, sticky='NESW')
            tooltip.CreateToolTip(deletebutton, text='מחיקת פוסט')
    else:
        if(if_topic=="$"):
            messagebox.showwarning("Warning","There are no posts to present")
        else:
            messagebox.showwarning("Warning",f"Topic ''{if_topic}'' posts don't exists      ")




def callback(url):
    webbrowser.open_new(url)



def reset_page():
    MainFrame.destroy()
    Start = postManager(ws)


# Create Function to Delete A Record
def deletePost(link,if_topic,user):
    # make sure he wants to delete it
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
    if MsgBox == "yes":

        # Create a database or connect to one
        conn = sqlite3.connect('images/projectManagment.db')
        # Create cursor
        c = conn.cursor()

        # Delete a record
        c.execute(f"DELETE from posts WHERE link = '{link}' AND UserName='{user}'");  # check if it did this AND user=user add----------------------

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        if (if_topic == "$"):
            store_all_saved()
        else:
            store_all_saved_for_topic(if_topic)




def updatePostComment(comment,link,if_topic,user):
    try:
        print(comment)
        print(link)
        # Create a database or connect to one
        conn = sqlite3.connect('images/projectManagment.db')
        # Create cursor
        c = conn.cursor()

        # update query to update comment
        c.execute(f"UPDATE posts set comment = '{comment}' where link = '{link}' AND UserName='{user}'");  # check if it did this


        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()
        if (if_topic == "$"):
            store_all_saved()
        else:
            store_all_saved_for_topic(if_topic)
    except:
        messagebox.showwarning("Warning", "Your comment contains a forbidden character (')")


def add_topic_to_records(search_topic):
    global currUser
    conn = sqlite3.connect('images/projectManagment.db')



    try:#check if topic exist if not create if yes delete the old and put the new in order to show the most recently
        curser = conn.execute(
            f"SELECT topic,UserName FROM topics  WHERE topic='{search_topic}' AND UserName='{currUser}'");
        help = curser.fetchall()[0]
        a = help[1]
        conn.execute(f"DELETE FROM topics  WHERE topic='{search_topic}' AND UserName='{currUser}'");
        conn.execute("INSERT INTO topics  VALUES (?,?,?)", (None, search_topic, currUser));
        conn.commit()
        print("try to save the same word to same user comment for me")
    except:
        conn.execute("INSERT INTO topics  VALUES (?,?,?)", (None,search_topic,currUser));
        conn.commit()
    conn.close()



def deleteTopic(topic,user):

    # Create a database or connect to one
    conn = sqlite3.connect('images/projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute(f"DELETE from topics WHERE topic = '{topic}' AND UserName='{user}'");  # check if it did this

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    pop.destroy()
    show_search_history()


def delete_all_topics():
    global currUser
    # Create a database or connect to one
    conn = sqlite3.connect('images/projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute(f"DELETE from topics WHERE UserName='{currUser}'");  # check if it did this

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    pop.destroy()
    show_search_history()




def show_search_history():#default value if the call came from top
    global currUser

    # currUser = userPass.getUser()
    # show all saved topic in a popup
    conn = sqlite3.connect('images/projectManagment.db')
    cursor = conn.execute(
        f"SELECT topic,UserName FROM topics  WHERE UserName='{currUser}' ORDER BY id DESC limit 10");  # last 10   DISTINCT
    list_res = cursor.fetchall()

    conn.close()

    print(list_res)  # show in popup
    global pop

    pop = Toplevel(ws)
    pop.iconphoto(False, p1)
    pop.geometry('400x700')
    pop.title('TopicsHistory')
    pop.configure(bg="#f8f9fa")

    for i in range(len(list_res)):#has to be 10
        loadimage = PhotoImage(file="images/search.png")
        roundedbutton = Button(pop, image=loadimage, borderwidth=0, highlightthickness=0, bd=0,bg="#f8f9fa",
                               command=lambda e=list_res[i][0]: insert_to_searchBox(e))
        roundedbutton.image = loadimage
        tooltip.CreateToolTip(roundedbutton, text='חיפוש למילה זו')
        roundedbutton.grid(column=0, row=i, sticky='NESW', pady=(15, 10),padx=(20,0))

        l = Label(pop, text=list_res[i][0], fg="black",bg="#f8f9fa",
                   font=('Helvatical bold', 15), anchor="w"
                   )

        l.grid(column=1, row=i, sticky='NESW',pady=(10, 10))


        loadimage = PhotoImage(file="images/dels.png")
        roundedbutton = Button(pop, image=loadimage, borderwidth=0, highlightthickness=0, bd=0,bg="#f8f9fa",
                               command=lambda e=i:deleteTopic(list_res[e][0],list_res[e][1]))
        roundedbutton.image = loadimage
        tooltip.CreateToolTip(roundedbutton, text='למחוק מההיסטוריה')
        roundedbutton.grid(column=2, row=i, sticky='NESW')

    if(len(list_res)>1):
        b = Button(pop, text="deleteAll", fg="black", bg="#f8f9fa", borderwidth=2,
                  font=('Helvatical bold', 15), relief="raised", cursor="hand2",
                  command=lambda :delete_all_topics())  # command=lambda e=list_saved[i - 2][2] :deletePost(e,if_topic)

        b.grid(column=1, row=11, sticky='NESW',pady=(20, 20))
    if(len(list_res)==0):
        l = Label(pop, text="אין הסטוריה של  חיפושים", fg="black", bg="#f8f9fa",
                  font=('Helvatical bold', 15), anchor="w"
                  )  # command=lambda e=list_saved[i - 2][2] :deletePost(e,if_topic)

        l.grid(column=1, row=0, sticky='NESW', pady=(50, 0),padx=(40,0))

    print("show_search_history()")

def insert_to_searchBox(word):
    global List
    global pop
    pop.destroy()
    List.delete(0, END)
    List.insert(0, word)

# def goback():
#     ws.destroy()
#     import existUser


ws.mainloop()

















