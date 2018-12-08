#coding=utf-8

from blog.combination import Combin
import unittest

class Testregister(unittest.TestCase):
    '''退出测试用例'''
    def setUp(self):
        self.reg = Combin()


    def test01(self):
        self.reg = Combin()
        result = self.reg.out('1',2,2)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test02(self):
        self.reg = Combin()
        result = self.reg.out('1',3,3)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test03(self):
        self.reg = Combin()
        result = self.reg.out('2',2,4)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test04(self):
        self.reg = Combin()
        result = self.reg.out('1',2,5)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test05(self):
        self.reg = Combin()
        result = self.reg.out('1',2,6)
        expect_result = False
        self.assertEqual(result, expect_result)


    def test06(self):
        self.reg = Combin()
        result = self.reg.out('1',2,7)
        expect_result = False
        self.assertEqual(result, expect_result)

    def test07(self):
        self.reg = Combin()
        result = self.reg.out('1',2,8)
        expect_result = False
        self.assertEqual(result, expect_result)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



