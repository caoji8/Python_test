#coding:utf-8
def login(name,password):
    flag = False
    if (name=="admin" and password=="admin"):
        flag = True
    else:
        flag = False
    return flag
        