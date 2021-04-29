

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

    # element = driver.find_element_by_partial_link_text("ח")
    # element.click()

    # element=driver.find_element_by_xpath("//div[@class='ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 nnctdnn4 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr']")
    # element.click()

    # driver.get("https://www.facebook.com/search/posts/?q=%D7%A4%D7%95%D7%A1%D7%98%D7%99%D7%9D")

    # element=driver.find_element_by_xpath("//div[@data-visualcompletion='ignore-dynamic']")#//div[@class='qzhwtbm6 knvmm38d']
    # element.click()




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
    # element = driver.find_element_by_partial_link_text("אישורים")
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





