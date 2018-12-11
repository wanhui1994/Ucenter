#coding=utf-8

import unittest
import HTMLTestRunner
import os

case_path=os.path.join('E:\\py-wh-lx\\Ucenter\\case')
report_path=os.path.join('E:\\py-wh-lx\\Ucenter\\report\\')

def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern='test_1_regis.py',top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    report_abspath = os.path.join(report_path, "test.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()