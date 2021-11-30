import time
import unittest
import login
import data_base_function as db

class TestSelenium(unittest.TestCase):



    # initialization of webdriver
    def setUp(self):
        self.FS = login.login_facebook("user", "pass")
        self.FS.login()
        self.driver=self.FS.getDriver()


    def test_login(self):
        assert self.FS.check_validation() == True
        assert self.FS.getName() == "Shirley"



    # Test case method. It should always start with test_
    def test_date(self):
        driver = self.driver
        driver.get("https://www.facebook.com/search/posts/?q=ארון")
        posts = driver.find_elements_by_xpath(
            "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']")
        posts = [elem.get_attribute('href') for elem in
                 posts]
        print(len(posts))
        driver.get(posts[0])
        try:
            dateTags = driver.find_elements_by_xpath(
                "//span[@class='j1lvzwm4 stjgntxs ni8dbmo4 q9uorilb gpro0wi8']/b/b")
            print(len(dateTags))
            list_classes = []
            for tag in dateTags:
                list_classes.append(tag.get_attribute("class"))


            shortest_string = db.find_min(list_classes)
            print(shortest_string)
            place_of_short_string = list_classes.index(shortest_string)
            date = dateTags[place_of_short_string].text
            print(date)
        except:
            date = driver.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi b1v8xokw m9osqain hzawbc8m']/span/span[2]/span")[0].text
            print(date)

    def test_posts_len(self):
        driver = self.driver
        driver.get("https://www.facebook.com/search/posts/?q=מחשבים")
        time.sleep(2)
        b=driver.find_element_by_tag_name("body")
        b.click()
        posts=[]
        if(len(posts)<10):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            posts = driver.find_elements_by_xpath(
                "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']")
        print(len(posts))
        assert len(posts)>=3




    # cleanup method called after every test performed
    def tearDown(self):
        self.FS.closeBrowser()



if __name__ == '__main__':
    unittest.main()


