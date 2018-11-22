# coding=utf-8

from common.uc_data import Ucenterdata

class Combin1(Ucenterdata):
    data=Ucenterdata()
    def regis(self,num):
        '''注册接口'''
        variable={}
        regisresult=self.data.combinationdict('/umis/user/bindUser.do',num,'注册',variable)
        return regisresult

    def login(self,num):
        '''平台登录接口'''
        variable={}
        loginresult=self.data.combinationdict('/umis/user/loginUser.do',num,'登陆',variable)
        return loginresult

    def fblogin(self,num):
        '''封闭登录接口'''
        variable={}
        fbloginresult=self.data.combinationdict('/umis/user/loginFBUser.do',num,'封闭登陆',variable)
        return fbloginresult

    def out(self,data,num,ucdata):
        '''退出登录接口'''
        result=self.login(data) #平台用户登录,data变量指的是要登录哪一行的数据
        outresult={}
        if ucdata == '1':
            '''正常退出'''
            code=self.data.dykeys(data,'登陆','sysCode')
            variable={'sid':result['data']['sid'],
                      'userAccount':result['data']['userAccount'],
                      'sysCode':code}
            outresult=self.data.combinationdict1('/umis/user/logoutUser.do',variable)
        elif ucdata == '2':
            '''异常退出'''
            variable={}
            outresult=self.data.combinationdict('/umis/user/logoutUser.do',num,'退出',variable)
        return outresult

    def bind(self,num,data):
        '''绑定接口'''
        result=self.regis(data) #未绑定用户登录
        sid = result['data']['sid']
        variable={'sid':sid}
        bindresult=self.data.combinationdict('/umis/user/bindUser.do',num,'绑定',variable)
        return bindresult