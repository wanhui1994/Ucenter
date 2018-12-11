#coding=utf-8

from blog.combination import Combin
import unittest

class Testupdataelgpas(unittest.TestCase):
    '''修改密码测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.updateLoginPassword(2,2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.updateLoginPassword(2,3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.updateLoginPassword(2,4)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test04(self):
        self.reg = Combin()
        result = self.reg.updateLoginPassword(2,5)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test05(self):
        self.reg = Combin()
        result = self.reg.updateLoginPassword(2,6)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test06(self):
        self.reg = Combin()
        result = self.reg.updateLoginPassword(2,7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test07(self):
        self.reg = Combin()
        result = self.reg.updateLoginPassword(2,8)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test08(self):
        '''找回密码，将修改的后的密码修改为原密码'''
        self.reg = Combin()
        result = self.reg.updatePassword(9)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



