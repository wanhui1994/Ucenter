#coding=utf-8

from blog.combination import Combin
import unittest

class Testunbinduser(unittest.TestCase):
    '''解绑测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.unbindUser(2,2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.unbindUser(2,3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.unbindUser(2,4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        self.reg = Combin()
        result = self.reg.unbindUser(3,5)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test05(self):
        self.reg = Combin()
        result = self.reg.unbindUser(3,6)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test06(self):
        self.reg = Combin()
        result = self.reg.unbindUser(3,7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test07(self):
        self.reg = Combin()
        result = self.reg.unbindUser(3,8)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test08(self):
        self.reg = Combin()
        result = self.reg.unbindUser(3,9)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test09(self):
        self.reg = Combin()
        result = self.reg.unbindUser(3,10)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



