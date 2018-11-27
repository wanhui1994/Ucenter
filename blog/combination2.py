# coding=utf-8

from common.uc_data import Ucenterdata

class Combin(Ucenterdata):
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

    def out(self,data):
        '''退出登录接口'''
        result=self.login(data,num) #平台用户登录,data变量指的是要登录哪一行的数据
        if a == num:
            code=self.data.dykeys(data,'登陆','sysCode')
            variable={'sid':result['data']['sid'],
                      'userAccount':result['data']['userAccount'],
                      'sysCode':code}
            outresult=self.data.combinationdict1('/umis/user/logoutUser.do',variable)
            return outresult
        else:
            outresult=self.data.combinationdict('/umis/user/logoutUser.do',num,'关联',variable)



    def onlinkuser(self,num,data):
        '''关联账号接口'''
        result=self.regis(data) #未关联用户登录
        sid = result['data']['sid']
        variable={'sid':sid}
        onlinkresult=self.data.combinationdict('/user/realtionLinkUserAccount.do',num,'关联',variable)
        return onlinkresult

    def qxonlinkuser(self,num,data):
        '''取消关联账号接口'''
        result=self.regis(data) #已关联用户登录
        sid = result['data']['sid']
        variable={'sid':sid}
        onlinkresult=self.data.combinationdict('/umis/user/cancelLinkUserAccount.do',num,'取消关联',variable)
        return onlinkresult


    def bind(self,num,data):
        '''绑定接口'''
        result=self.regis(data) #未绑定用户登录
        sid = result['data']['sid']
        variable={'sid':sid}
        bindresult=self.data.combinationdict('/umis/user/bindUser.do',num,'绑定',variable)
        return bindresult

    def unbind(self,num,data):
        '''解除绑定接口'''
        result=self.regis(data) #绑定用户登录
        sid = result['data']['sid']
        variable={'sid':sid}
        unbindresult=self.data.combinationdict('/umis/user/unbindUser.do',num,'解绑',variable)
        return unbindresult

    def checkuserphone(self,num):
        '''校验手机号是否可以关联接口'''
        variable={}
        checkphoneresult=self.data.combinationdict('/umis/user/checkUserPhone.do',num,'手机号是否可以关联',variable)
        return checkphoneresult

    def createAndLinkUser(self,num,data):
        '''手机号不存在创建帐号关联接口'''
        fbresult=self.regis(data) #绑定用户登录
        if fbresult['code']=='306':
                return self.data.combinationdict('/umis/user/createAndLinkUser.do',num,'手机号不存在关联',{})
        elif fbresult['code']=='200':  #解除关联
            sid=fbresult['data']['sid']
            user=fbresult['data']['userAccount']
            pyload={'sysCode':'FX001','userAccount':user,'sid':sid}
            self.data.combinationdict1('/umis/user/cancelLinkUserAccount.do',pyload)#取消关联
            pyload1={'sysCode':'FX003','userAccount':user,'sid':sid}
            self.data.combinationdict1('/umis/user/cancelLinkUserAccount.do',pyload1) #用户退出
            fbresult=self.regis(data)
            if fbresult['code']=='306':
                return self.data.combinationdict('/umis/user/createAndLinkUser.do',num,'手机号不存在关联','null')


    def existAndLinkUser(self,num,data):
        '''手机号存在关联接口'''
        fbresult=self.regis(data) #绑定用户登录
        if fbresult['code']=='306':
                return self.data.combinationdict('/umis/user/existAndLinkUser.do',num,'手机号不存在关联','null')
        elif fbresult['code']=='200':  #解除关联
            sid=fbresult['data']['sid']
            user=fbresult['data']['userAccount']
            pyload={'sysCode':'FX001','userAccount':user,'sid':sid}
            self.data.combinationdict1('/umis/user/cancelLinkUserAccount.do',pyload)#取消关联
            pyload1={'sysCode':'FX003','userAccount':user,'sid':sid}
            self.data.combinationdict1('/umis/user/cancelLinkUserAccount.do',pyload1) #用户退出
            fbresult=self.regis(data)
            if fbresult['code']=='306':
                return self.data.combinationdict('/umis/user/existAndLinkUser.do',num,'手机号不存在关联','null')








