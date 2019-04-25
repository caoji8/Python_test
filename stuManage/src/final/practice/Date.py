import json
#存储
def saveDate(date,filename = "user.json"):
    with open(filename, 'r', encoding='utf-8') as opp:
        model = json.load(opp)
    with open(filename, mode='w', encoding='utf-8') as sa:
        #将读出来的枚举作为一个列表append(注册函数提供的值)
        model.append(date)
        json.dump(model,sa)

#读取文件 并且对读取的进行拆解
def readDate(filename = "user.json"):
    with open(filename,mode="r",encoding='utf-8') as re:
       user_json = json.load(re)
    list_key = []
    list_value = []
    for i in user_json:
        for key,value in i.items():
            list_key.append(key)
            list_value.append(value)
    return list_key,list_value
