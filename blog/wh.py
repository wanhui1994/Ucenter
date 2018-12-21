#coding=utf-8
f = open("C:\\Users\\admin\\Desktop\\jc\\cc.txt",'w')
for i in range(1,500):
     str3='{\"area\":\"110000\",\"fee\":\"0.01\",\"fieldName\":\"13、11、消费维权\",\"imageUrl\":\"http://192.168.10.239/user/userAccount/xhlvshi02/xhlvshi021543818477917.png\",\"lawfirm\":\"事务所\",\"lawyerName\":\"测试律师\",\"priceUnit\":\"30分钟\",\"realType\":0,\"score\":-1,\"sort\":4.8,\"userAccount\":\"wh20181201\"}'
     f.write(str3)
     f.write(",")
print('ok')
f.close()