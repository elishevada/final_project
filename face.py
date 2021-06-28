from tkinter import *
import time
from mysql.connector import connect, Error

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title(" automation ")


def Take_input():
    # user_name = inputtxt1.get("1.0", "end-1c")
    # password = inputtxt2.get("1.0", "end-1c")
    # str = inputtxt3.get("1.0", "end-1c")



    url="https://www.facebook.com"


    driver =webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(url)

    print("Running into facebook")
    url="https://www.facebook.com"



    user_name = inputtxt.get("1.0", "end-1c")
    password = inputtxt1.get("1.0", "end-1c")
    str = inputtxt2.get("1.0", "end-1c")

    if (url == "https://www.facebook.com"):
        Output.delete("1.0", END)
        Output.insert(END, f"getting the result to /{str}/")
        Output.tag_add("right", "1.0", "end")


        element = driver.find_element_by_xpath("//input[@id='email']")
        element.send_keys(user_name)
        element = driver.find_element_by_id("pass")
        element.send_keys(password)

        element.send_keys(Keys.RETURN)
        time.sleep(3)
        st1="privacy"
        st2="login_attempt"
        if (st1 in driver.current_url or st2 in driver.current_url):
            element=driver.find_element_by_class_name("_9ay7")
            Output.delete("1.0",END)
            Output.insert(END, element.text)
            Output.tag_add("right", "1.0", "end")
            driver.quit()


        print(driver.current_url)
        # if driver.current_url=="https://www.facebook.com":
        #     print(driver.current_url)
        element = driver.find_element_by_xpath("//input[@placeholder='חפשי בפייסבוק']")
        element.clear()
        # element.send_keys("פוסטים")
        # element.send_keys(Keys.RETURN)

        element.send_keys(str)
        element.send_keys(Keys.RETURN)


        time.sleep(5)
        # element=driver.find_element_by_partial_link_text("פוסטים")
        #
        # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
        # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

        webdriver.ActionChains(driver).double_click(driver.find_element_by_partial_link_text("פוסטים")).perform()


        time.sleep(10)

        # str="אופניים"
        element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
        for el in element:
            print(el.text)
            Output.insert(END, el.text)
            Output.insert(END, "\n")
            Output.tag_add("right", "1.0", "end")
            # if str in el.text:
            #     print(el.text)
            #     Output.insert(END, el.text)
            #     Output.tag_add("right", "1.0", "end")


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


lfirst = Label(text="running into facebook")
widget = Entry(root, show="*", width=15)
l = Label(text="username")
inputtxt = Text(root, height=3,
                width=100,
                bg="light yellow")
l1 = Label(text="password")
inputtxt1 = Text(root, height=3,
                width=100,
                bg="light yellow")
l2 = Label(text="what do you looking for?")
inputtxt2 = Text(root, height=3,
                width=100,
                bg="light yellow")

Output = Text(root, height=50,
              width=100,
              bg="light cyan")
Output.configure(font='fangsongti')
Output.tag_configure("right", justify='right')


Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: Take_input())

widget.pack()
lfirst.pack()
l.pack()
inputtxt.pack()
l1.pack()
inputtxt1.pack()
l2.pack()
inputtxt2.pack()
Display.pack()
Output.pack()

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
