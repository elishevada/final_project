import unittest


import data_base_function as db

class TestPro(unittest.TestCase):

    def test_min(self):
        list=["fffffffffffffffff","fffffffffffffffff","ttt","fffh4","fffffff"]
        self.assertEqual(db.find_min(list), "fffh4")
        list = ["fffffffffffffffff", "fffffffffffffffff", "ttt", "fffttttttttttttttth4", "fffffff"]
        self.assertEqual(db.find_min(list), "fffttttttttttttttth4")
    def test_valid(self):
        self.assertEqual(db.valid("$"), 1)
        self.assertEqual(db.valid(""), 1)
        self.assertEqual(db.valid("hi"), 0)




if __name__ == '__main__':
    unittest.main()


