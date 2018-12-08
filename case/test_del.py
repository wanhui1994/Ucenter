#coding=utf-8

from blog.combination import Combin
import unittest

class Testdel(unittest.TestCase):
    '''删除增加的用户信息测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.DeleteUserForTest(2,'注册','userAccount','sysCode')
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.DeleteUserForTest(3,'注册','userAccount','sysCode')
        expect_result = False
        self.assertEqual(result, expect_result)

    def test03(self):
        self.reg = Combin()
        result = self.reg.DeleteUserForTest(4,'注册','userAccount','sysCode')
        expect_result = False
        self.assertEqual(result, expect_result)


    def test04(self):
        self.reg = Combin()
        result = self.reg.DeleteUserForTest(5,'注册','userAccount','sysCode')
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()