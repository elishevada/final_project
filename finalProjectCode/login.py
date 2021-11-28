import threading
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.keys import Keys
name="default"

class login_facebook():#TK

    # Run page
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # options = webdriver.ChromeOptions()
        #
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())#options=options





    def login(self):
        global name
        print("Running into facebook")
        driver = self.driver
        # driver.maximize_window()
        driver.get("https://www.facebook.com")
        time.sleep(2)
        usernameEl = driver.find_element_by_xpath("//input[@id='email']")#//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5"]
        usernameEl.clear()
        usernameEl.send_keys(self.username)
        passwordEl = driver.find_element_by_id("pass")
        passwordEl.clear()
        passwordEl.send_keys(self.password)

        passwordEl.send_keys(Keys.RETURN)
        time.sleep(3)

    def check_validation(self):
        global name
        if(self.driver.current_url=="https://www.facebook.com/"):
            try:
                name = self.driver.find_elements_by_xpath(
                    "//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5']")[0].get_attribute(
                    "innerHTML")
            except:
                print("error finding the name at facebook")
            return True
        else:
            if(self.driver.current_url=="https://www.facebook.com/?sk=welcome"):#new user in facebook that didnt set his friends
                self.driver.get("https://www.facebook.com/")
                # time.sleep(5)
                try:
                    name = self.driver.find_elements_by_xpath(
                        "//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5']")[0].get_attribute("innerHTML")
                except:
                    print("error finding the name at facebook")
                print(name)
                return True
            return False



    def getName(self):
        global name
        return name

    def closeBrowser(self):

        self.driver.close()
        print("Browser quit")

    def getDriver(self):
        return self.driver