import sqlite3
import threading
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
from tkinter import ttk, messagebox
import tooltip
import userPass
import login

second_frame=0
login_flag=0
driver=1
MainFrame=0
comments=[]
commentssaved=[]

class postManager(Tk):

    def __init__(self, ws):
        i=0
        global second_frame
        global MainFrame
        currUser=userPass.getUser()
        currPass=userPass.getPass()

        print(currUser)
        print(currPass)


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
        file.add_command(label ='show saved', command = lambda :store_all_saved())
        file.add_command(label='show saved for', command=lambda :open_save_dialog())
        file.add_command(label='search history', command=lambda: show_search_history())
        file.add_command(label='Reset page', command=lambda: reset_page())
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
                           command=lambda :self.close_all_opened())
        roundedbutton.image=loadimage
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



        button1 = Button(button1Frame, text="חפש לי", bg="lightblue",
                         command=lambda :threading.Thread(target=self.user_login, args=((int)(PostInput.get()),List.get(), currUser,currPass)).start())

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


    def user_login(self,numOfPosts,search_topic,user,pas):

        global login_flag
        global driver

        if(login_flag==0):
            LF = login.login_facebook(user, pas)
            driver=LF.driver
            LF.login()
            login_flag=1
        self.store_post_information(numOfPosts,search_topic,user,pas)




    def store_post_information(self,numOfPosts,search_topic,user,pas):
        # check if search topic validate english and different of what placeholder
        if(valid(search_topic)==0):
            # save the search word in the topics table
            add_topic_to_records(search_topic)
            # befor printing to the screen clear the grid and show in the labe the search topic and the number
            reset_page()
            self.setTitleForWord(search_topic, numOfPosts)

            global driver
            driver.get("https://www.facebook.com/search/posts/?q=" + search_topic)
            time.sleep(3)

            # try:

            posts = driver.find_elements_by_xpath(
                "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']")
            posts = [elem.get_attribute('href') for elem in
                     posts]
            print(len(posts))
            if(len(posts)!=0):
                if(len(posts)<numOfPosts):#still a problem giving less than 10 posts
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    time.sleep(4)
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    posts = driver.find_elements_by_xpath(
                        "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']")
                    posts = [elem.get_attribute('href') for elem in
                             posts]

                print(len(posts))
                if (len(posts) < numOfPosts):#after we scrooled and still less
                    print(f"probebly there are less {numOfPosts} than posts")
            else:
                messagebox.showwarning("Warning",f"There are no posts to show for {search_topic}      ")



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
                    dateTags = driver.find_elements_by_xpath(
                        "//span[@class='j1lvzwm4 stjgntxs ni8dbmo4 q9uorilb gpro0wi8']/b/b")#"j1lvzwm4 stjgntxs ni8dbmo4 q9uorilb gpro0wi8"
                    print(len(dateTags))
                    list_classes = []#"l94mrbxd aenfhxwr myohyog2 b6zbclly l9j0dhe7 sdhka5h4" "l94mrbxd aenfhxwr myohyog2 b6zbclly l9j0dhe7 sdhka5h4"
                    for tag in dateTags:#"l94mrbxd aenfhxwr myohyog2 b6zbclly l9j0dhe7 sdhka5h4 kw7X6Rc" class="l94mrbxd aenfhxwr myohyog2 b6zbclly l9j0dhe7 sdhka5h4 kw7X6Rc"
                        list_classes.append(tag.get_attribute("class"))

                    # shortest_string = min(list_classes)#can make a problem need to check by myself
                    shortest_string=find_min(list_classes)
                    print(shortest_string)
                    place_of_short_string = list_classes.index(shortest_string)
                    try:
                        date = dateTags[place_of_short_string].text
                    except:
                        print("date date is not in this path")
                    posts_date.append(date)
                    print(posts_date[i])

                    allPostContent = driver.find_elements_by_xpath(
                        "//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q']/div[@dir='auto']")
                    for sentence in allPostContent:
                        content = content + sentence.text
                        content = content + " "
                    posts_content.append(content)
                    print(posts_content[i])
                    post_writer = driver.find_element_by_xpath("//span[@class='nc684nl6']//span")
                    class_exist = post_writer.get_attribute("class")
                    if (len(class_exist) > 0):  # thay are two elements at the same path so we want the second one
                        post_writer = driver.find_elements_by_xpath("//span[@class='nc684nl6']//span")
                        post_writer = post_writer[1].text
                    else:
                        post_writer = post_writer.text
                    # print("--------------------------------------------------------------")
                    print(post_writer)
                    if (post_writer == ""):
                        post_writer = "פוסט ציבורי"
                        print(post_writer)
                    posts_writers.append(post_writer)
                    driver.back()
                    time.sleep(1)
                    i = i + 1

            # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            # print(posts_Links[0] + "\n" + posts_content[0] + "\n" + posts_date[0] + "\n"+posts_writers[0])

            # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            # print(posts_Links[1] + "\n" + posts_content[1] + "\n" + posts_date[
            #     1] + "\n")  # + posts_picture[0]+","+posts_date[0]+","

            # except Exception:
            #     messagebox.showwarning("Error", "we couldnd click the post")77
            self.insert_to_table(posts_Links, posts_content, posts_date, posts_writers,search_topic)
        else:
            messagebox.showerror("Warning","The search topic must contain letters or numbers")


    def insert_to_table(self,posts_links,posts_contents,posts_date,posts_writer,search_topic):
        global comments
        comments=[]
        save1image = PhotoImage(file="save1.png")
        num_of_posts=len(posts_links)
        posts_details=[posts_links,posts_writer,posts_date,posts_contents]
        for i in range(2,num_of_posts+2):
            # set3 = Label(second_frame, text="קישור לפוסט", fg="blue", borderwidth=1, relief="sunken", cursor="hand2",
            #              bg="lightgray")
            # set3.configure(font='fangsongti')
            # set3.grid(column=0, row=i, sticky='NESW')
            #
            # set3.bind("<Button-1>", lambda e=i-2: self.callback(posts_links[e])) #list indices must be integers or slices, not Event

            link = Button(second_frame, text="קישור לפוסט", bg="lightgray",fg="blue", borderwidth=1, font=('Helvatical bold', 15),relief="sunken",cursor="hand2",
                            command=lambda e=i-2: self.callback(posts_links[e]))

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
            comments.append(set)


            save1button = Button(second_frame, image=save1image, borderwidth=0,
                                 command=lambda k=i: button_index(k,posts_details,search_topic))
            save1button.image = save1image
            save1button.grid(column=5, row=i, sticky='NESW')
            tooltip.CreateToolTip(save1button, text='Save post for later')

    def setTitleForWord(self,search_word,num_post):
        title = Label(
            second_frame,
            text=f"מציג  {num_post} תוצאות עבור  {search_word}",
            fg="black",
            bg="white",
            font=('Helvatical bold', 15)
        )

        title.place(relx=0.5, rely=0.75, relwidth=0.6,
                    relheight=0.1, anchor="n")


    def callback(self,url):
        webbrowser.open_new(url)



    def close_all_opened(self):
        global  driver
        if(type(driver)!=int):
            driver.close()
        ws.destroy()


ws = Tk()
# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved
p1 = PhotoImage(file='facebook_icon.png')

# Setting icon of master window
ws.iconphoto(False, p1)
ws.geometry('1000x700')
ws.title('WA-newUser')
Start = postManager(ws)



def add_topic_to_records(search_topic):
    currUser = userPass.getUser()
    conn = sqlite3.connect('projectManagment.db')
    conn.execute("INSERT INTO topics (UserName,topic) VALUES (?,?)", (currUser, search_topic));
    conn.commit()
    conn.close()

def valid(topic):
    # sume=0
    # leng=len(topic)
    if(topic==""):
        return 1
    # for i in topic:
    #     if(i==" "):
    #         topic=topic.replace(" ","$")
    #         sume+=1
    # if(leng==sum):
    #     return 1
    return 0

def find_min(list_search):
    x = "l94mrbxd.aenfhxwr.myohyog2.b6zbclly.l9j0dhe7.sdhka5h4.nw7X6Rf hiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
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
    print("doesn need to get here fine min")
    return x






def button_index(k,posts_details,search_topic):
    global comments
    comment_text=comments[k-2].get("1.0", "end")
    currUser = userPass.getUser()

    try:
        conn = sqlite3.connect('projectManagment.db')

        conn.execute("INSERT INTO posts (username,subject,link,writer,date,content,comment) VALUES (?,?,?,?,?,?,?)", (currUser, search_topic,posts_details[0][k-2],posts_details[1][k-2],posts_details[2][k-2],posts_details[3][k-2],comment_text));
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("Error","This post is already saved")
    print(k)

def store_all_saved():
    reset_page()#delete all the posts from screen
    currUser = userPass.getUser()
    conn = sqlite3.connect('projectManagment.db')
    cursor = conn.execute(f"SELECT * FROM posts  WHERE UserName='{currUser}'");
    # print(cursor.fetchall())
    print_saved(cursor.fetchall(),"0")#print on screen



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

    # label = Label(ws, text="show saved for:", font=13, bg="white", fg="black")
    # label.place(relx=0.1, rely=0.008, anchor="n")
    #
    # wordFrame = Frame(ws, bg="lightgrey", bd=1)
    # wordFrame.place(relx=0.3, rely=0.01, relwidth=0.2, relheight=0.03, anchor="n")
    # word = Entry(wordFrame, font=40, justify="right")
    # word.place(relwidth=1, relheight=1)
    # word.focus()
    #
    # button = Button(ws, text="הראה", bg="lightblue",
    #                 command=lambda: store_all_saved_for_topic(word.get()))
    #
    # button.place(relx=0.4, rely=0.01, relwidth=0.1,
    #              relheight=0.03, anchor="n")



def remove(widget1, widget2, widget3):
    widget1.place_forget()
    widget2.place_forget()
    widget3.place_forget()




def store_all_saved_for_topic(search_topic):
    reset_page()

    currUser = userPass.getUser()
    conn = sqlite3.connect('projectManagment.db')
    cursor = conn.execute(f"SELECT * FROM posts  WHERE UserName='{currUser}' AND subject='{search_topic}'");
    # print on screen
    print_saved(cursor.fetchall(),search_topic)


def print_saved(list_saved,if_topic):
    global commentssaved
    commentssaved = []
    updateimage = PhotoImage(file="update.png")
    deleteimage = PhotoImage(file="delete.png")
    if(len(list_saved)!=0):
        for i in range(2,2+len(list_saved)):
            link = Button(second_frame, text="קישור לפוסט", bg="lightgray", fg="blue", borderwidth=1,#link doesnt work
                          font=('Helvatical bold', 15), relief="sunken", cursor="hand2",
                          command=lambda e=list_saved[i - 2][2]: callback2(e))

            link.grid(column=0, row=i, sticky='NESW')

            set = Text(second_frame, height=6,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=1, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][3])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            set = Text(second_frame, height=2,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=2, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][4])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            set = ScrolledText(second_frame, height=1,
                               width=30,
                               bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=3, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][5])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            setcom = Text(second_frame, height=2,
                       width=15,
                       bg="lightgray", wrap=WORD)
            setcom.configure(font=('Helvatical bold', 12))
            setcom.tag_configure("right", justify='right')
            setcom.grid(column=4, row=i, sticky='NESW')
            setcom.insert(END, list_saved[i - 2][6])
            setcom.tag_add("right", "1.0", "end")
            commentssaved.append(setcom)

            set = Text(second_frame, height=2,
                       width=10,
                       bg="lightgray", wrap=WORD)
            set.configure(font=('Helvatical bold', 12))
            set.tag_configure("right", justify='right')
            set.grid(column=5, row=i, sticky='NESW')
            set.insert(END, list_saved[i - 2][1])
            set.tag_add("right", "1.0", "end")
            set.configure(state='disabled')

            l0 = Label(second_frame, text="נושא הפוסט", font=('Helvatical bold', 15), borderwidth=2, relief="raised")
            l0.grid(row=1, column=5, sticky='NESW')

            updatebutton = Button(second_frame,image=updateimage, text="up", borderwidth=0,
                                 command=lambda e=i-2:updatePostComment(commentssaved[e].get("1.0", "end"),list_saved[e][2],if_topic))
            updatebutton.image = updateimage
            updatebutton.grid(column=6, row=i, sticky='NESW')
            tooltip.CreateToolTip(updatebutton, text='update post')

            deletebutton = Button(second_frame,image=deleteimage, text="del", borderwidth=0,
                                 command=lambda e=list_saved[i - 2][2] :deletePost(e,if_topic))
            deletebutton.image = deleteimage
            deletebutton.grid(column=7, row=i, sticky='NESW')
            tooltip.CreateToolTip(deletebutton, text='delete post')
    else:
        if(if_topic=="0"):
            messagebox.showwarning("Warning","There are no posts to present")
        else:
            messagebox.showwarning("Warning",f"Topic ''{if_topic}'' posts don't exists      ")

def callback2(url):
    webbrowser.open_new(url)


def reset_page():
    MainFrame.destroy()
    Start = postManager(ws)


# Create Function to Delete A Record
def deletePost(link,if_topic):
    # Create a database or connect to one
    conn = sqlite3.connect('projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute(f"DELETE from posts WHERE link = '{link}'");#check if it did this

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    if(if_topic=="0"):
        store_all_saved()
    else:
        store_all_saved_for_topic(if_topic)

def updatePostComment(comment,link,if_topic):
    print(comment)
    print(link)
    # Create a database or connect to one
    conn = sqlite3.connect('projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # update query to update ADDRESS
    c.execute(f"UPDATE posts set comment = '{comment}' where link = '{link}'");#check if it did this

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    if (if_topic == "0"):
        store_all_saved()
    else:
        store_all_saved_for_topic(if_topic)


def show_search_history():
    currUser = userPass.getUser()
    #show all saved topic in a popup
    conn = sqlite3.connect('projectManagment.db')
    cursor = conn.execute(f"SELECT topic FROM topics  WHERE UserName='{currUser}' limit 10");#top 10
    list_res=cursor.fetchall()
    conn.close()
    print(list_res)#show in popup
    #global pop#dont have to
    pop=Toplevel(ws)
    pop.iconphoto(False, p1)
    pop.geometry('100x600')
    pop.title('Topics')
    for i in range(len(list_res)):
        b = Button(pop, text=list_res[i][0], bg="lightgray", fg="blue", borderwidth=1,
                      font=('Helvatical bold', 15), relief="sunken", cursor="hand2",
                      command=lambda :pop.destroy())
        b.grid(column=0, row=i, sticky='NESW')

    print("show_search_history()")

# def closepop(pop):
#     pop.destroy()

ws.mainloop()


# save1image = PhotoImage(file="save1.png")
#
# for i in range(2,10):
#     set3 =Label(second_frame, text="קישור לפוסט", fg="blue",borderwidth = 1,relief="sunken", cursor="hand2",bg="lightgray")
#     set3.configure(font='fangsongti')
#     set3.grid(column=0, row=i, sticky='NESW')
#
#     set3.bind("<Button-1>", lambda e: callback("https://www.facebook.com"))
#
#     set = Text(second_frame, height=6,
#                    width=10,
#                    bg="lightgray" , wrap=WORD)
#     set.configure(font=('Helvatical bold',12))
#     set.tag_configure("right", justify='right')
#     set.grid(column=1, row=i, sticky='NESW')
#     set.insert(END,"יידידיידידידיידידיידיד")
#     set.tag_add("right", "1.0", "end")
#     set.configure(state='disabled')
#
#     set = Text(second_frame, height=2,
#                    width=10,
#                    bg="lightgray", wrap=WORD )
#     set.configure(font=('Helvatical bold',12))
#     set.tag_configure("right", justify='right')
#     set.grid(column=2, row=i, sticky='NESW')
#     set.insert(END,"יידידיידידידיידידיידיד")
#     set.tag_add("right", "1.0", "end")
#     set.configure(state='disabled')
#
#     set = ScrolledText(second_frame, height=1,
#                    width=30,
#                    bg="lightgray" , wrap=WORD)
#     set.configure(font=('Helvatical bold',12))
#     set.tag_configure("right", justify='right')
#     set.grid(column=3, row=i, sticky='NESW')
#     set.insert(END,"היי.."\
# "שולחן מעץ אורן 90% ממוחזר." \
# "מחפש המלצה לטיפול לתנאי פנים. יש פה ושם מעט תיקונים קטנים עם שפכטל עץ. בגדול מעדיף מראה כמה שיותר קרוב לצבע המקורי אבל מניח שיהיה שינוי, אז מחפש משהו פחות צהוב. יהיה נחמד גם קצת ברק לא מאוד מוגזם. יש לי ניירות שיוף עד 400 כרגע"\
# " תודהרבה ")
#     set.tag_add("right", "1.0", "end")
#     set.configure(state='disabled')
#
#
#     set = Text(second_frame, height=2,
#                    width=20,
#                    bg="lightgray", wrap=WORD)
#     set.configure(font=('Helvatical bold',12))
#     set.tag_configure("right", justify='right')
#     set.grid(column=4, row=i, sticky='NESW')
#     set.tag_add("right", "1.0", "end")
#
#
#
#     save1button = Button(second_frame,image=save1image,borderwidth=0,
#                        command=lambda k = i: button_index(k))
#     save1button.grid(column=5, row=i, sticky='NESW')
#     tooltip.CreateToolTip(save1button, text = 'Save post for later')















