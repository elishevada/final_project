import threading
import time
from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox
from tkinter.ttk import Separator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from tkHyperLinkManager import HyperlinkManager
import webbrowser

from selenium.webdriver.common.keys import Keys


class store_post_information(Tk):

    # Run page
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def login(self):
        print("Running into facebook")
        driver = self.driver
        # driver.maximize_window()
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

    def check_validation(self):
        if(self.driver.current_url=="https://www.facebook.com/"):
            return True
        else:
            return False


    def closeBrowser(self):
        self.driver.close()
        print("Browser quit")