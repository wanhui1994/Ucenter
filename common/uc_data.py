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

    def uccode(self,num,name):
        '''获取code的值'''
        c=Opendata()
        m=c.openexcel(num,name)
        p=m[-1] #获取数据
        return p

    def requestvalue(self,num):
        '''获取接口请求url的值'''
        c=Opendata()
        m=c.openexcel(num,'请求')
        p=m[2:] #获取数据
        return p



    def dykeys(self,num,name,ucdata):
        '''获取excel列表中keys对应的某一行的value值'''
        p = self.ucvalue(num,name)[self.uckeys(name).index(ucdata)] #页面中所需的数据值
        return p

    def combinationdict(self,urlnum,num,name,variable):
        '''
        urlnum：获取url的行数变量、num：是获取参数value的行数、name:打开的excel名称、variable:增加的字典变量名称
        key和value组合生成字典+请求地址生成url:
        '''
        pyload=dict(zip(self.uckeys(name),self.ucvalue(num,name)))
        pyload=dict(pyload, **variable)
        url1=self.requestvalue(urlnum)
        url=self.conf()+"".join(url1)
        r = requests.get(url,params=pyload)
        print(r.url)
        print(r.json())
        return r.json()

    def combinationdict1(self,urlnum,variable):
        '''直接传入参数，不靠excel列表获取'''
        url1=self.requestvalue(urlnum)
        pyload=variable
        url=self.conf()+"".join(url1)
        r = requests.get(url,params=pyload)
        print(r.url)
        return r.json()


    def deldata(self,urlnum,variable):
        '''用户删除接口'''
        url1=self.requestvalue(urlnum)
        pyload=variable
        url="http://ucms.test.faxuan.net"+"".join(url1)
        r = requests.get(url,params=pyload)
        print(r.url)
        return r.json()


