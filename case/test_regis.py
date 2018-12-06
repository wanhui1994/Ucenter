#coding=utf-8

from blog.combination import Combin
import unittest

class Testregister(unittest.TestCase):
    '''注册测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.regis(2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.regis(3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.regis(4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        self.reg = Combin()
        result = self.reg.regis(5)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test05(self):
        self.reg = Combin()
        result = self.reg.regis(6)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test06(self):
        self.reg = Combin()
        result = self.reg.regis(7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test07(self):
        self.reg = Combin()
        result = self.reg.regis(8)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test08(self):
        self.reg = Combin()
        result = self.reg.regis(9)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test09(self):
        self.reg = Combin()
        result = self.reg.regis(10)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test10(self):
        self.reg = Combin()
        result = self.reg.regis(11)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



