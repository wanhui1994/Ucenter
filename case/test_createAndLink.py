#coding=utf-8

from blog.combination import Combin
import unittest

class Testregister(unittest.TestCase):
    '''手机号不存在创建帐号关联测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        result = self.reg.createAndLink(2,2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        result = self.reg.createAndLink(2,3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        result = self.reg.createAndLink(2,4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        result = self.reg.createAndLink(2,5)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test05(self):
        result = self.reg.createAndLink(2,6)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test06(self):
        result = self.reg.createAndLink(2,7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def  test07(self):
        '''删除关联的账号登录'''
        result=self.reg.DeleteUserForTest(2,'手机号不存在创建帐号关联','fbUserAccount','sysCode')
        expect_result = False
        self.assertEqual(result, expect_result)

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()



