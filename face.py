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


class StartPage(Tk):

    # Load application
    def __init__(self, root):
        # root = Tk()
        # root.wm_attributes("-topmost", 1)

        # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # root.geometry("%dx%d+0+0" % (w, h))
        root.title(" automation ")


        for i in range(10):
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
        x = threading.Thread(target=GetUserInfo, args=("0504380777", "judge444", "שולחן", 3))
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
                dateTags=driver.find_elements_by_xpath("//b[@class='b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4 ']/b")
                print(len(dateTags))
                for tag in dateTags:
                    if "nw7WN7Z" not in tag.get_attribute("class"):
                        date=tag.text
                        break
                posts_date.append(date)
                print(posts_date[0])

                allPostContent=driver.find_elements_by_xpath("//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q']/div[@dir='auto']")
                for sentence in allPostContent:
                    content=content+sentence.text
                    content=content+" "
                posts_content.append(content)
                print(posts_content[i])
                driver.back()
                time.sleep(1)
                i = i + 1

        # print(posts_Links[0]+","+posts_content[0])#+ posts_picture[0]+","+posts_date[0]+","
        # except Exception:
        #     messagebox.showwarning("Error", "we couldnd click the post")

    def callback(self,url):
        webbrowser.open_new(url)

    def closeBrowser(self):
        self.driver.close()
        print("Browser quit")

def GetUserInfo(username, password, search_topic_recieved, numberofpost):
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
                print("Please enter a valid number of posts to like")
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


# root = Tk()
# # root.wm_attributes("-topmost", 1)
#
# # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# # root.geometry("%dx%d+0+0" % (w, h))
# root.title(" automation ")
#
# def callback(url):
#     webbrowser.open_new(url)


# def Take_input():
    # user_name = inputtxt1.get("1.0", "end-1c")
    # password = inputtxt2.get("1.0", "end-1c")
    # str = inputtxt3.get("1.0", "end-1c")



    # url="https://www.facebook.com"
    #
    #
    # driver =webdriver.Chrome(ChromeDriverManager().install())
    # driver.maximize_window()
    # driver.get(url)
    #
    # print("Running into facebook")
    # url="https://www.facebook.com"



    # user_name = inputtxt.get("1.0", "end-1c")
    # password = inputtxt1.get()
    # str = inputtxt2.get("1.0", "end-1c")






        # # errors
        # st1="privacy"
        # st2="login_attempt"
        # if (st1 in driver.current_url or st2 in driver.current_url):
        #     element=driver.find_element_by_class_name("_9ay7")
        #     # Output.delete("1.0",END)
        #     # Output.insert(END, element.text)
        #     # Output.tag_add("right", "1.0", "end")
        #     driver.quit()
        #
        #
        # print(driver.current_url)
        #
        # element = driver.find_element_by_xpath("//input[@placeholder='חפשי בפייסבוק']")
        # element.clear()
        #
        #
        # element.send_keys(str)
        # time.sleep(1)
        # element.send_keys(Keys.ENTER)
        # time.sleep(1)
        #
        # time.sleep(5)
        #
        #
        # webdriver.ActionChains(driver).double_click(driver.find_element_by_partial_link_text("פוסטים")).perform()
        #
        #
        # time.sleep(10)





# class ="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l"


        # str=""
        # liststr=[]
        # listdate=[]
        # j=0
        # element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
        # for el in element:
        #     if (len(el.text)>20):
        #         el.click()
        #         time.sleep(2)
        #         postLink=driver.current_url
        #         driver.back()
        #         print(postLink)
        #         # print((el.text))
        #         # for let in el.text:
        #
        #         # el.text=el.text.replace('\','')
        #         liststr.append(el.text)
        #         break
        #
        # print(liststr)
        # date = ""
        # # for el in liststr:
        # for i in range(len(liststr)):
        #     for letter in liststr[i]:
        #         if (letter == '\n'):
        #             print(date)
        #             listdate.append(date)
        #             liststr[i] = liststr[i].replace(date, "")
        #             # print(el)
        #             break
        #         date = date + letter
        #     for let in liststr[i]:
        #         if (let.isnumeric() == False and let.isdigit() == False and let.isalpha() == False and let != ' '):
        #             # print(letter)
        #             liststr[i] = liststr[i].replace(let, '_')
        #
        #     # print(el)
        # print(liststr[0])
        #
        # set = Text(root, height=5,
        #            width=20,
        #            bg="light cyan")
        #
        # set.configure(font='fangsongti')
        # set.tag_configure("right", justify='right')
        # set.grid(column=0, row=9, sticky='NESW')
        # set.insert(END, liststr[0])
        #
        # set2 = Text(root, height=5,
        #             width=20,
        #             bg="light cyan")
        #
        # set2.configure(font='fangsongti')
        # set2.tag_configure("right", justify='right')
        # set2.grid(column=1, row=9, sticky='NESW')
        # set2.insert(END, listdate[0])
        #
        # set3 =Label(root, text="link to post", fg="blue", cursor="hand2")
        #
        # set3.configure(font='fangsongti')
        # # set3.tag_configure("right", justify='right')
        # set3.grid(column=2, row=9, sticky='NESW')
        # set3.bind("<Button-1>", lambda e: callback(postLink))



         # sb = Scrollbar(
        #     root,
        #     orient=VERTICAL
        # )
        #
        # sb.grid(row=8, column=1, sticky=NS)
        #
        # set.config(yscrollcommand=sb.set)
        # sb.config(command=set.yview)





        # time.sleep(2)
        # element = driver.find_elements_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p dkezsu63']/span")
        # print(element[0].text)
        #
        # set4 = Text(root, height=5,
        #             width=5,
        #             bg="light cyan")
        #
        # set4.configure(font='fangsongti')
        # set4.tag_configure("right", justify='right')
        # set4.grid(column=3, row=9, sticky='NESW')
        # set4.insert(END, element[0].text)
        #
        # comments = Text(root, height=10,
        #                  width=10,
        #                  bg="light yellow")
        # comments.grid(row=9, column=4, sticky='NESW')

            # if str in el.text:
            #     print(el.text)
            #     Output.insert(END, el.text)
            #     Output.tag_add("right", "1.0", "end")
        # Output.insert(END, element[1].text)

        # actions = webdriver.ActionChains(driver)
        # for i in range(1):#53 down
        #     actions.send_keys(Keys.PAGE_DOWN).perform()
        #     time.sleep(1)
        #
        # element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
        # for el in element:
        #     if str in el.text:
        #         print(el.text)
        #         Output.insert(END, el.text)
        #         Output.tag_add("right", "1.0", "end")


# def print_hi():
#     print("hi")
#
# x = threading.Thread(target=Take_input)
# for i in range(10):
#     root.rowconfigure(i, weight=1)
#     root.columnconfigure(i, weight=1)
#
# lfirst = Label(text="running into facebook")
# lfirst.grid(row=0, column=0, columnspan=10, sticky='NESW')
#
#
# l = Label(text="username")
# l.grid(row=1, column=0, columnspan=10, sticky='NESW')
# inputtxt = Text(root, height=3,
#                 width=100,
#                 bg="light yellow")
# inputtxt.grid(row=2, column=0, columnspan=10, sticky='NESW')
# inputtxt.insert(END,"0504380777")
# l1 = Label(text="password")
# l1.grid(row=3, column=0, columnspan=10, sticky='NESW')
# # inputtxt1 = Text(root, height=3,
# #                 width=100,
# #                 bg="light yellow")
# inputtxt1 = Entry(root, show="*", width=15)
# inputtxt1.grid(row=4, column=0, columnspan=10, sticky='NESW')
# inputtxt1.insert(END,"judge444")
# l2 = Label(text="what do you looking for?")
# l2.grid(row=5, column=0, columnspan=10, sticky='NESW')
# inputtxt2 = Text(root, height=3,
#                 width=100,
#                 bg="light yellow")
# inputtxt2.grid(row=6, column=0, columnspan=10, sticky='NESW')
#
#
# # Output = Text(root, height=50,
# #               width=100,
# #               bg="light cyan")
# # Output.configure(font='fangsongti')
# # Output.tag_configure("right", justify='right')
#
#
# Display = Button(root, height=2,
#                  width=20,
#                  text="Show",
#                  command=lambda: start_thread())
# Display.grid(row=7, column=0, columnspan=10, sticky='NESW')
# l3 = Label(text="תוכן פוסט")
# l3.grid(row=8, column=0, sticky='NESW')
#
# # separator1 = Separator(root, orient='vertical')
# # separator1.grid(row=8, column=1, sticky='NESW')
#
# l4 = Label(text="תאריך פוסט")
# l4.grid(row=8, column=1, sticky='NESW')
#
# # separator2 = Separator(root, orient='vertical')
# # separator2.grid(row=8, column=3, sticky='NESW')
#
# l5 = Label(text="כותב הפוסט")
# l5.grid(row=8, column=2, sticky='NESW')
#
# # separator3 =Separator(root, orient='vertical')
# # separator3.grid(row=8, column=5, sticky='NESW')
#
# l6 = Label(text="הערות לפוסט")
# l6.grid(row=8, column=3, sticky='NESW')
#
# # separator4 =Separator(root, orient='vertical')
# # separator4.grid(row=8, column=7, sticky='NESW')
#
# save_comment=Button(root,height=2,
#                  width=20,
#                  text="save",
#                  command=lambda: print_hi())
# save_comment.grid(row=8,column=4,sticky='NESW')
#
# # widget.pack()
# # lfirst.pack()
# # l.pack()
# # inputtxt.pack()
# # l1.pack()
# # inputtxt1.pack()
# # l2.pack()
# # inputtxt2.pack()
# # Display.pack()
# # Output.pack()
#
# mainloop()






