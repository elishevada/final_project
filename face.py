import threading
from tkinter import *
import time
from tkinter import messagebox
from tkinter.ttk import Separator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from tkHyperLinkManager import HyperlinkManager
import webbrowser
# from functools import partial
from getpass import getpass
from mysql.connector import connect, Error

import mysql.connector
import sqlite3




class StartPage(Tk):

    # Load application
    def __init__(self, root):
        self.had_loged=False

        # root = Tk()
        # root.wm_attributes("-topmost", 1)

        # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # root.geometry("%dx%d+0+0" % (w, h))
        root.title(" automation ")


        for i in range(20):
            root.rowconfigure(i, weight=1)
            root.columnconfigure(i, weight=1)

        lfirst = Label(text="running into facebook")
        lfirst.grid(row=0, column=0, columnspan=10, sticky='NESW')

        l = Label(text="username")
        l.grid(row=1, column=0, columnspan=10, sticky='NESW')
        inputtxt = Text(root, height=3,
                        width=100,
                        bg="light yellow")
        inputtxt.grid(row=2, column=0, columnspan=10, sticky='NESW')
        inputtxt.insert(END, "0504380777")
        l1 = Label(text="password")
        l1.grid(row=3, column=0, columnspan=10, sticky='NESW')
        # inputtxt1 = Text(root, height=3,
        #                 width=100,
        #                 bg="light yellow")
        inputtxt1 = Entry(root, show="*", width=15)
        inputtxt1.grid(row=4, column=0, columnspan=10, sticky='NESW')
        inputtxt1.insert(END, "judge444")
        l2 = Label(text="what do you looking for?")
        l2.grid(row=5, column=0, columnspan=10, sticky='NESW')
        inputtxt2 = Text(root, height=3,
                         width=100,
                         bg="light yellow")
        inputtxt2.grid(row=6, column=0, columnspan=10, sticky='NESW')

        # Output = Text(root, height=50,
        #               width=100,
        #               bg="light cyan")
        # Output.configure(font='fangsongti')
        # Output.tag_configure("right", justify='right')

        # Display = Button(root, height=2,
        #                  width=20,
        #                  text="Show",
        #                  command=lambda: self.start_thread())
        # Display.grid(row=7, column=0, columnspan=10, sticky='NESW')
        l3 = Label(text="תוכן פוסט")
        l3.grid(row=8, column=0, sticky='NESW')

        # separator1 = Separator(root, orient='vertical')
        # separator1.grid(row=8, column=1, sticky='NESW')

        l4 = Label(text="תאריך פוסט")
        l4.grid(row=8, column=1, sticky='NESW')

        # separator2 = Separator(root, orient='vertical')
        # separator2.grid(row=8, column=3, sticky='NESW')

        l5 = Label(text="כותב הפוסט")
        l5.grid(row=8, column=2, sticky='NESW')

        # separator3 =Separator(root, orient='vertical')
        # separator3.grid(row=8, column=5, sticky='NESW')

        l6 = Label(text="הערות לפוסט")
        l6.grid(row=8, column=3, sticky='NESW')

        # separator4 =Separator(root, orient='vertical')
        # separator4.grid(row=8, column=7, sticky='NESW')

        # save_comment = Button(root, height=2,
        #                       width=20,
        #                       text="save",
        #                       command=lambda: print_hi())
        # save_comment.grid(row=8, column=4, sticky='NESW')

        # widget.pack()
        # lfirst.pack()
        # l.pack()
        # inputtxt.pack()
        # l1.pack()
        # inputtxt1.pack()
        # l2.pack()
        # inputtxt2.pack()
        # Display.pack()
        # Output.pack()
        # user_name = inputtxt.get("1.0", "end")
        # password = inputtxt1.get("1.0", "end")
        # hashtag = inputtxt2.get("1.0", "end")

        x = threading.Thread(target=GetUserInfo, args=("0504380777", "judge444", "מטפחות", 3,had_loged))

        Display = Button(root, height=2,
                         width=20,
                         text="Show",
                         command=lambda: self.start_thread(x))
        Display.grid(row=7, column=0, columnspan=10, sticky='NESW')



    def start_thread(self,x):
        # if(x.isAlive()==True):
        #     x.join()
        #     print("thread still alive")
        # else:
        x.start()

    # @property
    # def had_loged(self):
    #     """I'm the 'x' property."""
    #     print("getter of x called")
    #     return self.had_loged
    #
    # @had_loged.setter
    # def had_loged(self, value):
    #     print("setter of x called")
    #     self.had_loged = value


class store_post_information(Tk):

    # Run page
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        print("Running into facebook")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.facebook.com")
        time.sleep(2)
        usernameEl = driver.find_element_by_xpath("//input[@id='email']")
        usernameEl.clear()
        usernameEl.send_keys(self.username)
        passwordEl = driver.find_element_by_id("pass")
        passwordEl.clear()
        passwordEl.send_keys(self.password)

        passwordEl.send_keys(Keys.RETURN)
        time.sleep(3)

    def store_post(self, search_topic):

        driver = self.driver
        driver.get("https://www.facebook.com/search/posts/?q=" + search_topic)
        time.sleep(3)

        # try:
        posts = driver.find_elements_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']")
        posts=[elem.get_attribute('href') for elem in
                                      posts]
        # driver.get(posts[3])
        # posts=driver.find_elements_by_xpath("//div[@class='ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi opwvks06 hop1g133 linmgsc8 t63ysoy8 i09qtzwb rm7oo3ik n7fi1qx3 kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x pmk7jnqg j9ispegn kr520xx4']")
        # except Exception:
        #     messagebox.showwarning("Error", "we didnt find the class of post")
        # posts[0].click()
        # print(posts[0])
        # print("hihihihi")
        # try:
        posts_date = []
        posts_content = []
        posts_picture = []
        posts_Links = []
        posts_writers=[]

        date=""
        i = 0
        for post in posts:
            content = " "
            if (i < 3):
                # post.click()
                driver.get(post)
                time.sleep(1)
                posts_Links.append(driver.current_url)
                print(posts_Links[i])
                # posts_links_of_pic = driver.find_elements_by_tag_name('img')
                # print(len(posts_links_of_pic))
                # posts_links_of_pic = [elem.get_attribute('src') for elem in
                #                       posts_links_of_pic]  # get the list of all the link for the images in a post
                # posts_picture.append(posts_links_of_pic)
                # print(posts_picture[i])
                time.sleep(1)
                dateTags=driver.find_elements_by_xpath("//span[@class='j1lvzwm4 stjgntxs ni8dbmo4 q9uorilb gpro0wi8']/b/b")
                print(len(dateTags))
                # print(dateTags.get_attribute("class"))
                # dateTags=[elem.get_attribute('class') for elem in dateTags
                #         if "gw7WN7S" not in elem.get_attribute("class")]
                # print(len(dateTags))
                # print(dateTags)
                # print(a)
                list_classes=[]
                for tag in dateTags:
                    list_classes.append(tag.get_attribute("class"))


                shortest_string=min(list_classes)
                print(shortest_string)
                place_of_short_string=list_classes.index(shortest_string)
                date=dateTags[place_of_short_string].text
                # for tag in dateTags:
                #     # print(tag.get_attribute("class"))
                #     if "gw7WN7S" not in tag.get_attribute("class"):
                #         date=tag.text
                #         break
                posts_date.append(date)
                print(posts_date[i])

                allPostContent=driver.find_elements_by_xpath("//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q']/div[@dir='auto']")
                for sentence in allPostContent:
                    content=content+sentence.text
                    content=content+" "
                posts_content.append(content)
                print(posts_content[i])
                post_writer=driver.find_element_by_xpath("//span[@class='nc684nl6']//span")
                class_exist=post_writer.get_attribute("class")
                print(class_exist+"fooooooo")
                if(len(class_exist)>0):#thay are two elements at the same path so we want the second one
                    post_writer = driver.find_elements_by_xpath("//span[@class='nc684nl6']//span")
                    post_writer=post_writer[1].text
                else:
                    post_writer=post_writer.text
                print("--------------------------------------------------------------")
                print(post_writer)
                if(post_writer==""):
                    post_writer="פוסט ציבורי"
                    print(post_writer)
                posts_writers.append(post_writer)
                driver.back()
                time.sleep(1)
                i = i + 1

        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(posts_Links[0]+"\n"+posts_content[0]+"\n"+posts_date[0]+"\n")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(posts_Links[1]+"\n"+posts_content[1]+"\n"+posts_date[1]+"\n")#+ posts_picture[0]+","+posts_date[0]+","
        # except Exception:
        #     messagebox.showwarning("Error", "we couldnd click the post")
        self.insert_to_table(posts_Links,posts_content,posts_date,posts_writers)


    def insert_to_table(self,posts_links,posts_contents,posts_date,posts_writer):
        num_of_posts=len(posts_links)
        posts_details=[posts_links,posts_writer,posts_date,posts_contents]
        colum=0
        for i in range(9,num_of_posts+9):

            while(colum<4):
                set = Text(root, height=5,
                           width=20,
                           bg="light cyan")

                set.configure(font='fangsongti')
                set.tag_configure("right", justify='right')
                set.grid(column=colum, row=i, sticky='NESW')
                set.insert(END, posts_details[colum][i-9])
                colum+=1
            colum = 0


    def callback(self,url):
        webbrowser.open_new(url)

    def closeBrowser(self):
        self.driver.close()
        print("Browser quit")

had_loged=False

def GetUserInfo(username, password, search_topic_recieved, numberofpost,had_loged):
    if password and username and search_topic_recieved:
        if username != "Username" and password != "Password" and search_topic_recieved != "what do you looking for":
            # try:
            if int(numberofpost) != 0:
                if messagebox.askokcancel('Application','Application is running, press OK to continue') == True:
                    username = username
                    password = password
                    # try:
                    print(search_topic_recieved)
                    FB = store_post_information(username, password)
                    FB.login()
                    FB.store_post(search_topic_recieved)

                    # except:
                    #     messagebox.showerror("Could not execute task. Please try again.")

                else:
                    SystemExit()
            else:
                messagebox.showwarning("Error", "Please enter a valid number of posts to like")
                print("Please enter a valid number of posts")
            # except Exception:
            #     messagebox.showwarning("Error", "Please enter a valid number of posts to like")
            #     print("Please enter a valid number of posts to like")
        else:
            messagebox.showwarning("Error", "Please enter suitable data")
            print("Please enter suitable data")
    else:
        messagebox.showwarning('Error', 'Please enter a username or password')  #shows warning message
        print("Please enter a username and password")




if __name__ == "__main__":
    print("Run from main")
    

    root = Tk()
    Start = StartPage(root)
    root.mainloop()
else:
    print("Run from import")








