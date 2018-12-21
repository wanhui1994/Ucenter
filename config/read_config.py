# coding=utf-8

import configparser
import os

class Conf():
    def wrl(self,sec,name,value):
        '''配置文件写入'''
        config = configparser.ConfigParser()
        config.read('Config.ini')
        try:
            config.add_section(sec)
            config.set(sec,name,value)

        except configparser.DuplicateSectionError:
            print("Section%salready exists"%sec)
        #写入配置文件
        config.write(open("Config.ini", "w"))


    def read1(self,sec,name):
        '''配置文件读取'''
        cf=configparser.ConfigParser()
        pwd = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        path=os.path.join(pwd,'config\Config.ini')
        print(path)
        cf.read(path)
        data=cf.get(sec,name)
        return data
