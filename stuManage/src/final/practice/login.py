#coding:utf-8
from stuManage.src.final.practice.Date import saveDate,readDate
def login(name,password):
    flag = False
    list_key,list_value = readDate()
    if (name in list_key and password in list_value):
        flag = True
        #判读该name是否在文件中
    elif(name in list_key and password not in list_value):
        user_choose = input("此用户不存在，是否注册. yes/no")
        if user_choose == "yes":
            logon_system()
            #注册函数
        else:
            pass
    else:
        flag = False
    return flag

#注册系统---数据处理成对象
def logon_system():
    new_logon = input("请输入用户名,密码").split(",")
    new_user = {}
    new_user[new_logon[0]]=new_logon[1]
    saveDate(new_user)