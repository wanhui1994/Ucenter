# coding=utf-8

from common.uc_data import Ucenterdata

class Combin(Ucenterdata):
    data=Ucenterdata()
    def regis(self,num):
        '''注册接口'''
        variable={}
        result=self.data.combinationdict(1,num,'注册',variable)
        if result['code']== str(self.data.uccode(num,'注册')):
            return False
        else:
            return True

    def ucode(self,num):
        '''返回登录的sid'''
        variable={}
        result=self.data.combinationdict(2,num,'平台登录',variable)
        return result

    def login(self,num):
        '''平台登录接口'''
        variable={}
        result=self.data.combinationdict(2,num,'平台登录',variable)
        print(result)
        if result['code']== str(self.data.uccode(num,'平台登录')):
            return False
        else:
            return True

    def fblogin(self,num):
        '''封闭登录接口'''
        variable={}
        result=self.data.combinationdict(3,num,'封闭登录',variable)
        if result['code']== str(self.data.uccode(num,'封闭登录')):
            return False
        else:
            return True

    def out(self,num,data):
        '''退出接口'''
        ptsid=self.ucode(data)
        variable={'sid':ptsid['data']['sid']}
        result=self.data.combinationdict(4,num,'退出登录',variable)
        if result['code']== str(self.data.uccode(num,'退出登录')):
            return False
        else:
            return True

    def bindUser(self,num,data):
        '''绑定接口'''
        ptsid=self.ucode(data)
        variable={'sid':ptsid['data']['sid']}
        result=self.data.combinationdict(5,num,'绑定',variable)
        if result['code']== str(self.data.uccode(num,'绑定')):
            return False
        else:
            return True

    def unbindUser(self,num,data):
        '''解绑接口'''
        ptsid=self.ucode(data)
        variable={'sid':ptsid['data']['sid']}
        result=self.data.combinationdict(6,num,'解绑',variable)
        if result['code']== str(self.data.uccode(num,'解绑')):
            return False
        else:
            return True

    def realtionLink(self,num,data):
        '''关联接口'''
        ptsid=self.ucode(data)
        variable={'sid':ptsid['data']['sid']}
        result=self.data.combinationdict(7,num,'关联',variable)
        print(result)
        if result['code']== str(self.data.uccode(num,'关联')):
            return False
        else:
            return True

    def cancelLink(self,num,data):
        '''取消关联接口'''
        ptsid=self.ucode(data)
        variable={'sid':ptsid['data']['sid']}
        result=self.data.combinationdict(8,num,'取消关联',variable)
        print(result)
        if result['code']== str(self.data.uccode(num,'取消关联')):
            return False
        else:
            return True

    def checkUserPhone(self,num):
        '''校验手机号是否可以关联接口'''
        variable={}
        result=self.data.combinationdict(9,num,'校验手机号是否可以关联',variable)
        print(result)
        if result['code']== str(self.data.uccode(num,'校验手机号是否可以关联')):
            return False
        else:
            return True

    def createAndLink(self,num,data):
        '''手机号不存在创建帐号关联接口'''
        self.fblogin(data)
        variable={}
        result=self.data.combinationdict(10,num,'手机号不存在创建帐号关联',variable)
        print(result)
        if result['code']== str(self.data.uccode(num,'手机号不存在创建帐号关联')):
            return False
        else:
            return True

    def existAndLink(self,num,data):
        '''手机号存在关联接口'''
        self.fblogin(data)
        variable={}
        result=self.data.combinationdict(11,num,'手机号存在关联',variable)
        print(result)
        if result['code']== str(self.data.uccode(num,'手机号存在关联')):
            return False
        else:
            return True

    def getUser(self,num):
        '''获取非登录用户信息'''
        variable={}
        result=self.data.combinationdict(12,num,'非登录用户信息',variable)
        if result['code']== str(self.data.uccode(num,'非登录用户信息')):
            return False
        else:
            return True

    def getLogin(self,num):
        '''获取登录用户信息'''
        udata=self.ucode(num)
        sid=udata['data']['sid']
        user=udata['data']['userAccount']
        code=self.data.dykeys(num,'平台登录','sysCode')
        variable={'sid':sid,'sysCode':code,'userAccount':user}
        result=self.data.combinationdict1(13,variable)
        if result['code']== str(self.data.uccode(num,'平台登录')):
            return False
        else:
            return True

    def getSystemSource(self,num):
        '''获取来源系统下拉列表'''
        variable={}
        result=self.data.combinationdict(14,num,'系统来源',variable)
        if result['code']== str(self.data.uccode(num,'系统来源')):
            return False
        else:
            return True

    def updatePassword(self,num):
        '''找回密码'''
        variable={}
        result=self.data.combinationdict(16,num,'找回密码',variable)
        if result['code']== str(self.data.uccode(num,'找回密码')):
            return False
        else:
            return True