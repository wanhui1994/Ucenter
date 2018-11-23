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
        code=self.data.dykeys(data,'登陆','sysCode')
        sid = result['data']['sid']
        variable={'sid':sid,'sysCode':code}
        bindresult=self.data.combinationdict('/umis/user/bindUser.do',num,'绑定',variable)
        return bindresult

    def unbind(self,num,data):
        '''解除绑定接口'''
        result=self.regis(data) #绑定用户登录
        code=self.data.dykeys(data,'登陆','sysCode')
        sid = result['data']['sid']
        variable={'sid':sid,'sysCode':code}
        unbindresult=self.data.combinationdict('/umis/user/unbindUser.do',num,'解绑',variable)
        return unbindresult

    def onlinkuser(self,num,data):
        '''关联账号接口'''
        result=self.regis(data) #未关联用户登录
        code=self.data.dykeys(data,'登陆','sysCode')
        sid = result['data']['sid']
        variable={'sid':sid,'sysCode':code}
        onlinkresult=self.data.combinationdict('/user/realtionLinkUserAccount.do',num,'关联',variable)
        return onlinkresult

    def qxonlinkuser(self,num,data):
        '''取消关联账号接口'''
        result=self.regis(data) #已关联用户登录
        code=self.data.dykeys(data,'登陆','sysCode')
        sid = result['data']['sid']
        variable={'sid':sid,'sysCode':code}
        onlinkresult=self.data.combinationdict('/umis/user/cancelLinkUserAccount.do',num,'取消关联',variable)
        return onlinkresult



