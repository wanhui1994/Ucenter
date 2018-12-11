#coding=utf-8

from blog.combination import Combin
import unittest

class TestupdateUserContactWay(unittest.TestCase):
    '''修改手机号、邮箱、qq测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(3,5)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test05(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(3,6)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test06(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(3,7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test07(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,8)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test08(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,9)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test09(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,10)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test10(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,11)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test11(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,12)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test12(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,13)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test13(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(2,14)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test14(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(3,15)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test15(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(3,16)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test16(self):
        self.reg = Combin()
        result = self.reg.updateUserContactWay(3,17)
        expect_result = False
        self.assertEqual(result, expect_result)



    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



