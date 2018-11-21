#coding=utf-8

from common.excel import Excelread


class Opendata():
    '''打开excel读取数据'''
    def openexcel(self,num,name):
        read = Excelread()
        read.open(r"..\file\ucenter接口设计.xlsx",name)
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
