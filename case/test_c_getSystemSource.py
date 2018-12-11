#coding=utf-8

from blog.combination import Combin
import unittest

class Testsystemsource(unittest.TestCase):
    '''获取来源系统下拉列表'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.getSystemSource(2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.getSystemSource(3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.getSystemSource(4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        self.reg = Combin()
        result = self.reg.getSystemSource(5)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



