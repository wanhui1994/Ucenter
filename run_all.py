# coding=utf-8
import unittest
import HTMLTestRunner
import os,time

# 获取文件路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "case")
reportpath = os.path.join(curpath, "report\\")

def all_case(case_path=casepath, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover


if __name__ == "__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_abspath =reportpath+now+"result.html"
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()

