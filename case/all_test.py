#coding=utf-8

import os

os.system("python ./test_regis.py")  #用户注册
os.system("python ./test_bindUser.py")  #用户绑定
os.system("python ./test_updateUserContactWay.py")  #修改手机号、邮箱、qq
os.system("python ./test_login.py")  #平台登录
os.system("python ./test_unbindUser.py")  #用户解绑
os.system("python ./test_checkUserPhone.py")  #校验手机号是否可以关联


# os.system("python ./test_bindUser.py")  #用户绑定
# os.system("python ./test_unbindUser.py")  #用户解绑
# os.system("python ./test_realtionLink.py")  #用户关联
# os.system("python ./test_realtionLink.py")  #修改手机号
