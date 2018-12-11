#coding=utf-8

from blog.combination import Combin
import unittest

class Testrlogin(unittest.TestCase):
    '''平台登录测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.login(2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.login(3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.login(4)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test04(self):
        self.reg = Combin()
        result = self.reg.login(5)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test05(self):
        self.reg = Combin()
        result = self.reg.login(6)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test06(self):
        self.reg = Combin()
        result = self.reg.login(7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test07(self):
        self.reg = Combin()
        result = self.reg.login(8)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test08(self):
        self.reg = Combin()
        result = self.reg.login(9)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test09(self):
        self.reg = Combin()
        result = self.reg.login(10)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test10(self):
        self.reg = Combin()
        result = self.reg.login(11)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test11(self):
        self.reg = Combin()
        result = self.reg.login(12)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test12(self):
        self.reg = Combin()
        result = self.reg.login(13)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test13(self):
        self.reg = Combin()
        result = self.reg.login(14)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test14(self):
        self.reg = Combin()
        result = self.reg.login(15)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test15(self):
        self.reg = Combin()
        result = self.reg.login(16)
        expect_result = False
        self.assertEqual(result, expect_result)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



