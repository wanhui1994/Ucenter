#conding=utf-8

from common.openpyxl import Opendata
from config.read_config import Conf
import requests


class Ucenterdata():
    '''通过excel生成请求的url'''
    def conf(self):
        '''获取配置文件'''
        configread = Conf()
        self.readconf=configread.read1('ip-test','ip')
        return self.readconf

    def uckeys(self,name):
        '''获取key的值'''
        c=Opendata()
        m=c.openexcel(1,name)
        p=m[3:-1] #获取数据
        return p

    def ucvalue(self,num,name):
        '''获取value的值'''
        c=Opendata()
        m=c.openexcel(num,name)
        p=m[3:-1] #获取数据
        return p

    def dykeys(self,num,name,ucdata):
        '''获取excel列表中keys对应的某一行的value值'''
        p = self.ucvalue(num,name)[self.uckeys(name).index(ucdata)] #页面中所需的数据值
        return p

    def combinationdict(self,url1,num,name,variable):
        '''
        key和value组合生成字典+请求地址生成url:
        tyep:判断是否增加参数的标识
        '''
        pyload=dict(zip(self.uckeys(name),self.ucvalue(num,name)))
        pyload=dict(pyload, **variable)
        url=self.conf()+url1
        r = requests.get(url,params=pyload)
        return r.json()

    def combinationdict1(self,url1,variable):
        '''直接传入参数，不靠excel列表获取'''
        pyload=variable
        url=self.conf()+url1
        r = requests.get(url,params=pyload)
        return r.json()

