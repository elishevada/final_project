from tkinter import *
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from tkHyperLinkManager import HyperlinkManager
import webbrowser
# from functools import partial

root = Tk()
root.wm_attributes("-topmost", 1)
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
root.title(" automation ")
str="sof.iaa. muznacha"
print(type(str))
print(str.split('.')[0])

def callback(url):
    webbrowser.open_new(url)


def Take_input():
    # user_name = inputtxt1.get("1.0", "end-1c")
    # password = inputtxt2.get("1.0", "end-1c")
    # str = inputtxt3.get("1.0", "end-1c")



    url="https://www.facebook.com"


    driver =webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(url)

    print("Running into facebook")
    # url="https://www.facebook.com"



    user_name = inputtxt.get("1.0", "end-1c")
    password = inputtxt1.get()
    str = inputtxt2.get("1.0", "end-1c")

    if (url == "https://www.facebook.com"):
        # Output.delete("1.0", END)
        # Output.insert(END, f"getting the result to /{str}/")
        # Output.tag_add("right", "1.0", "end")


        element = driver.find_element_by_xpath("//input[@id='email']")
        element.send_keys(user_name)
        element = driver.find_element_by_id("pass")
        element.send_keys(password)

        element.send_keys(Keys.RETURN)
        time.sleep(3)
        # errors
        st1="privacy"
        st2="login_attempt"
        if (st1 in driver.current_url or st2 in driver.current_url):
            element=driver.find_element_by_class_name("_9ay7")
            # Output.delete("1.0",END)
            # Output.insert(END, element.text)
            # Output.tag_add("right", "1.0", "end")
            driver.quit()


        print(driver.current_url)
        # if driver.current_url=="https://www.facebook.com":
        #     print(driver.current_url)
        element = driver.find_element_by_xpath("//input[@placeholder='חפשי בפייסבוק']")
        element.clear()
        # element.send_keys("פוסטים")
        # element.send_keys(Keys.RETURN)

        element.send_keys(str)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        # element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5']")

        # element =driver.find_element_by_class_name("a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5")

        # webdriver.ActionChains(driver).double_click(driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5']")).perform()

        time.sleep(5)
        # element=driver.find_element_by_partial_link_text("פוסטים")
        #
        # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
        # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

        webdriver.ActionChains(driver).double_click(driver.find_element_by_partial_link_text("פוסטים")).perform()


        time.sleep(10)


        str=""
        liststr=[]
        listdate=[]
        j=0
        element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
        for el in element:
            if (len(el.text)>20):
                el.click()
                # time.sleep(2)
                postLink=driver.current_url
                driver.back()
                print(postLink)
                # print((el.text))
                # for let in el.text:

                # el.text=el.text.replace('\','')
                liststr.append(el.text)
                break

        print(liststr)
        date = ""
        # for el in liststr:
        for i in range(len(liststr)):
            for letter in liststr[i]:
                if (letter == '\n'):
                    print(date)
                    listdate.append(date)
                    liststr[i] = liststr[i].replace(date, "")
                    # print(el)
                    break
                date = date + letter
            for let in liststr[i]:
                if (let.isnumeric() == False and let.isdigit() == False and let.isalpha() == False and let != ' '):
                    # print(letter)
                    liststr[i] = liststr[i].replace(let, '_')

            # print(el)
        print(liststr[0])

        set = Text(root, height=5,
                   width=20,
                   bg="light cyan")

        set.configure(font='fangsongti')
        set.tag_configure("right", justify='right')
        set.grid(column=0, row=8, sticky='NESW')
        set.insert(END, liststr[0])

        set2 = Text(root, height=5,
                    width=20,
                    bg="light cyan")

        set2.configure(font='fangsongti')
        set2.tag_configure("right", justify='right')
        set2.grid(column=1, row=8, sticky='NESW')
        set2.insert(END, listdate[0])

        set3 =Label(root, text="link to post", fg="blue", cursor="hand2")

        set3.configure(font='fangsongti')
        # set3.tag_configure("right", justify='right')
        set3.grid(column=2, row=8, sticky='NESW')
        set3.bind("<Button-1>", lambda e: callback(postLink))



         # sb = Scrollbar(
        #     root,
        #     orient=VERTICAL
        # )
        #
        # sb.grid(row=8, column=1, sticky=NS)
        #
        # set.config(yscrollcommand=sb.set)
        # sb.config(command=set.yview)





        time.sleep(2)
        element = driver.find_elements_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p dkezsu63']/span")
        print(element[0].text)

        set4 = Text(root, height=5,
                    width=5,
                    bg="light cyan")

        set4.configure(font='fangsongti')
        set4.tag_configure("right", justify='right')
        set4.grid(column=3, row=8, sticky='NESW')
        set4.insert(END, element[0].text)

        comments = Text(root, height=10,
                         width=10,
                         bg="light yellow")
        comments.grid(row=8, column=4, sticky='NESW')

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


def start_thread():
    x.start()

x = threading.Thread(target=Take_input)

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
l1 = Label(text="password")
l1.grid(row=3, column=0, columnspan=10, sticky='NESW')
# inputtxt1 = Text(root, height=3,
#                 width=100,
#                 bg="light yellow")
inputtxt1 = Entry(root, show="*", width=15)
inputtxt1.grid(row=4, column=0, columnspan=10, sticky='NESW')
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


Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: start_thread())
Display.grid(row=7, column=0, columnspan=10, sticky='NESW')

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

mainloop()





























#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
#
# from tkinter import *
#
# root = Tk()
# root.geometry("300x300")
# root.title(" automation ")
#
#
#
#
# def facerun():
#     user_name = inputtxt1.get("1.0", "end-1c")
#     password = inputtxt2.get("1.0", "end-1c")
#     str = inputtxt3.get("1.0", "end-1c")
#
#
#     print("Running into facebook")
#     url="https://www.facebook.com"
#     # user_name =input("Enter userName\n")
#     # password=input("Enter password\n")
#     # str=input("what do  you want to look for\n")
#
#
#
#     driver =webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     driver.get(url)
#
#
#     if(url=="https://www.facebook.com"):
#         element = driver.find_element_by_xpath("//input[@id='email']")
#         element.send_keys(user_name)
#         element = driver.find_element_by_id("pass")
#         element.send_keys(password)
#         # element=driver.find_element_by_name("login")
#         # element.click()
#         element.send_keys(Keys.RETURN)
#         element = driver.find_element_by_xpath("//input[@placeholder='חפשי בפייסבוק']")
#         element.clear()
#         # element.send_keys("פוסטים")
#         # element.send_keys(Keys.RETURN)
#
#         element.send_keys(str)
#         element.send_keys(Keys.RETURN)
#
#
#         time.sleep(5)
#         # element=driver.find_element_by_partial_link_text("פוסטים")
#         #
#         # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
#         # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
#
#         webdriver.ActionChains(driver).double_click(driver.find_element_by_partial_link_text("פוסטים")).perform()
#
#
#         time.sleep(10)
#
#         # str="אופניים"
#         element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
#         for el in element:
#             if str in el.text:
#                 print(el.text)
#                 # el.click()
#
#         actions = webdriver.ActionChains(driver)
#         for i in range(3):
#             actions.send_keys(Keys.PAGE_DOWN).perform()
#             time.sleep(1)
#
#         element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
#         for el in element:
#             if str in el.text:
#                 print(el.text)
#                 Output.insert(END, el.text)
#
#
#
#
#
#     l = Label(text="post details")
#     l1 = Label(text="username:")
#     inputtxt1 = Text(root, height=2,
#                      width=25,
#                      bg="light yellow")
#     l2 = Label(text="password:")
#     inputtxt2 = Text(root, height=2,
#                      width=25,
#                      bg="light yellow")
#     l3 = Label(text="what keys do you want to look for:")
#     inputtxt3 = Text(root, height=2,
#                      width=25,
#                      bg="light yellow")
#
#     Output = Text(root, height=5,
#                   width=25,
#                   bg="light cyan")
#
#     Display = Button(root, height=2,
#                      width=20,
#                      text="Show",
#                      command=lambda: facerun())
#
#     l.pack()
#     l1.pack()
#     l2.pack()
#     l3.pack()
#     inputtxt1.pack()
#     inputtxt2.pack()
#     inputtxt3.pack()
#     Display.pack()
#     Output.pack()
#
#     mainloop()
