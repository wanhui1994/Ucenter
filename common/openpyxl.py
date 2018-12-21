#coding=utf-8

from common.excel import Excelread
import os

class Opendata():
    '''打开excel读取数据'''
    def openexcel(self,num,name):
        read = Excelread()
        pwd=(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #获取当前路径的上上级路径
        path=os.path.join(pwd,'file\数据设计.xlsx')
        read.open(path,name)
        data=read.lines(num)
        modifydata=[]
        for i in range(0,len(data)):
            if type(data[i])==str:
                modifydata.append(data[i])
            elif type(data[i])==float:
                modifydata.append(int(data[i]))
            else:
                print('此参数列表中没有哦！')
        return modifydata
