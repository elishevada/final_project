import time
import unittest
import login
import data_base_function as db

class TestDataBase(unittest.TestCase):

    def test_user(self):
        try:
            db.insert_user("test","passt","testname")
        except:
            print("userexist")
        print(db.select_users())
        db.update_pass_user("test","fffff")
        print((db.select_users()))
        db.del_user("test")
        print((db.select_users()))
        db.insert_user("test", "passt", "testname")
        print((db.select_users()))

    def test_topic(self):
        try:
            db.add_topic_try("ארון","test")
        except:
            db.add_topic("ארון","test")
        try:
            db.add_topic_try("מיטה","test")
        except:
            db.add_topic("מיטה","test")
        try:
            db.add_topic_try("ארון","test")
        except:
            db.add_topic("ארון","test")
        print(db.all_saved_topics("test"))
        db.del_topic("ארון","test")
        db.del_all_topics("test")
        print(db.all_saved_topics("test"))
        try:
            db.add_topic_try("ארון","test")
        except:
            db.add_topic("ארון","test")
        try:
            db.add_topic_try("ארון","test")
        except:
            db.add_topic("ארון","test")
        print(db.all_saved_topics("test"))

    def test_post(self):
        db.insert_post(2,[("1"),("2"),("3"),("4"),("5")],"מדף","test","hicomment")
        print(db.store_all_posts("test"))



if __name__ == '__main__':
    unittest.main()