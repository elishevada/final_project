import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


url=input("Please enter the url of the web you want to work on! \n")
user_name =input("Enter userName\n")
password=input("Enter password\n")
if(url=="https://ps.btl.gov.il/#/login"):
    id=input("Enter id\n")



driver =webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
if(url=="https://yedion.jce.ac.il/yedion/fireflyweb.aspx"):
    element = driver.find_element_by_xpath("//input[@id='R1C1']")
    element.send_keys(user_name)
    element = driver.find_element_by_xpath("//input[@id='R1C2']")
    element.send_keys(password)
    element=driver.find_element_by_id("loginbtn")
    element.click()
    element=driver.find_element_by_partial_link_text("הגשת עבודות")
    element.click()
    element=driver.find_element_by_name("B5")
    element.click()
    element=driver.find_elements_by_tag_name("h2")
    print(len(element))#8
    for i in range(len(element)):
        element[i].click()
        i+=1
    e=driver.find_elements_by_name("Button_1")
    for i in range(len(e)):
        e[i].click()



if(url=="https://www.facebook.com"):
    element = driver.find_element_by_xpath("//input[@id='email']")
    element.send_keys(user_name)
    element = driver.find_element_by_id("pass")
    element.send_keys(password)
    # element=driver.find_element_by_name("login")
    # element.click()
    element.send_keys(Keys.RETURN)
    element = driver.find_element_by_xpath("//input[@placeholder='חפשי בפייסבוק']")
    element.clear()
    element.send_keys("פוסטים")
    element.send_keys(Keys.RETURN)


    time.sleep(10)
    element=driver.find_element_by_partial_link_text("פוסטים")
    # element.click()
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

    time.sleep(10)

    str="שבוע טוב"
    element = driver.find_elements_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
    for el in element:
        if str in el.text:
            print(el.text)
            el.click()


# a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7
# d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v knj5qynh m9osqain







if(url=="https://ps.btl.gov.il/#/login"):
    e=driver.find_element_by_id("vm_userZehut")
    e.send_keys(id)
    e=driver.find_element_by_id("vm_userName")
    e.send_keys(user_name)
    e=driver.find_element_by_id("vm_password")
    e.send_keys(password)
    e=driver.find_element_by_name("btnLogin")
    e.click()
    # element = driver.find_element_by_partial_link_text("גבייה")
    # element.click()
    time.sleep(5)
    element = driver.find_element_by_partial_link_text("אישורים")
    element.click()
    time.sleep(2)
    element=driver.find_elements_by_tag_name("button")
    print(len(element))
    element[15].click()
    time.sleep(10)
    element = driver.find_element_by_id("download")
    element.click()
    # element=driver.find_element_by_css_selector('button.btn btn-default')
    # element.click()
    # element = driver.find_element_by_partial_link_text("לחץ להצגת המסמך אישור על מעמד לא עובד")
    # element.click()
    # e=driver.find_element_by_id("topNav_1")
    # e.click()
    # e=driver.find_element_by_xpath("//button[@class='btn btn-default']")
    # e.click()
    # e = driver.find_element_by_xpath("//button[@title='הורדה']")
    # e.click()


# wait=WebDriverWait(driver, 9000000)



# element.close()




# element = driver.find_element_by_xpath("//input[@id='email']")
# element.send_keys(user_name)
# element = driver.find_element_by_id("pass")
# element.send_keys(password)
#
# element.send_keys(Keys.RETURN)
# element = driver.find_element_by_xpath("//input[@placeholder='חפשי בפייסבוק']")
# element.send_keys("פוסטים")
# element.send_keys(Keys.RETURN)





