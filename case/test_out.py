#coding=utf-8

from blog.wh import Combin
import unittest

class Testregister(unittest.TestCase):
    '''退出测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.out(2,2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.out(3,2)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.out(4,2)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()


