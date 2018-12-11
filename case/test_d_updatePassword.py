#coding=utf-8

from blog.combination import Combin
import unittest

class Testupdatepas(unittest.TestCase):

    '''找回密码测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.updatePassword(2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.updatePassword(3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.updatePassword(4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        self.reg = Combin()
        result = self.reg.updatePassword(5)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test05(self):
        self.reg = Combin()
        result = self.reg.updatePassword(6)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test06(self):
        self.reg = Combin()
        result = self.reg.updatePassword(7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test07(self):
        self.reg = Combin()
        result = self.reg.updatePassword(8)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test08(self):
        self.reg = Combin()
        result = self.reg.updatePassword(9)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



