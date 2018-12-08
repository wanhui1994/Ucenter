#coding=utf-8

from blog.combination import Combin
import unittest

class Testgetuser(unittest.TestCase):
    '''获取非登录用户信息测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.getUser(2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.getUser(3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.getUser(4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        self.reg = Combin()
        result = self.reg.getUser(5)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test05(self):
        self.reg = Combin()
        result = self.reg.getUser(6)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test06(self):
        self.reg = Combin()
        result = self.reg.getUser(7)
        expect_result = False
        self.assertEqual(result, expect_result)



    def test07(self):
        self.reg = Combin()
        result = self.reg.getUser(8)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test08(self):
        self.reg = Combin()
        result = self.reg.getUser(9)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test09(self):
        self.reg = Combin()
        result = self.reg.getUser(10)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test10(self):
        self.reg = Combin()
        result = self.reg.getUser(11)
        expect_result = False
        self.assertEqual(result, expect_result)



    def test11(self):
        self.reg = Combin()
        result = self.reg.getUser(12)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test12(self):
        self.reg = Combin()
        result = self.reg.getUser(13)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test13(self):
        self.reg = Combin()
        result = self.reg.getUser(14)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test14(self):
        self.reg = Combin()
        result = self.reg.getUser(15)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test15(self):
        self.reg = Combin()
        result = self.reg.getUser(16)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



