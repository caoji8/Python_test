from sqlite3 import connect
# dbname = "StudentMassage.db"
# # 连接数据库
# con = connect(dbname)
# # 获取游标
# cur = con.cursor()
# def createDb():
#     # 初次登陆创建数据库
#     try:
#         cur.execute('create table StudentMassage(name text,number integer,major text,grade text,score integer)')
#     except:
#         return False
# def insertDb(name,number,major,grade,score):
#     cur.execute('insert into StudentMassage(name,number,major,grade,score) values (?,?,?,?,?)',(name,number,major,grade,score))
#     # 上传提交
#     con.commit()
# def delDB(primary):
#     # 删除单个学生的所有信息    输入学号或者姓名
#     cur.execute('delete from StudentMassage where (name = ? or number =?)',(primary,primary))
#     con.commit()
# def selectDb(number):
#     # 搜索输入学号或者姓名
#     try:
#         row = cur.execute('select * from StudentMassage where (name = ? or number =?)',(number,number))
#         for i in row:
#             return print(i)
#     except:
#         print("未搜索到该内容")
#     finally:
#         con.close()
# def updateDb(choose,new_massage,number):
#     # 修改学生信息
#     # 增加一个用户选择 来更改对应的内容
#     # 修改名字
#     if choose==1:
#         cur.execute('update StudentMassage set name =? where (name =? or number = ?)',(new_massage,number,number))
#         con.commit()
#     # 修改学号
#     elif choose ==2:
#         cur.execute('update StudentMassage set number =? where (name =? or number = ?)', (new_massage, number, number))
#         con.commit()
#     # 修改学科
#     elif choose==3:
#         cur.execute('update StudentMassage set major =? where (name =? or number = ?)', (new_massage, number, number))
#         con.commit()
#     # 修改年级
#     elif choose==4:
#         cur.execute('update StudentMassage set grade =? where (name =? or number = ?)', (new_massage, number, number))
#         con.commit()
#     # 错误处理
#     else:
#         print("Error Choose")
class Datebase():
    def __init__(self,dbname):
        self.dbname = dbname
        # self.con = connect(self.dbname)
        # self.cur = self.con.cursor()
    def open(self):
        try:
            self.con = connect(self.dbname)
            self.cur = self.con.cursor()
        except:
            print("Error")
    def creatDatebase(self):
        self.open()
        try:
            self.cur.execute('create table user(username text,password text,age integer ,gender text,job text,telephone integer)')
        except:
            print('数据库已经创建')
            pass
        finally:
            self.close()
    #   未完成
    def inserMassage(self,username,password,age,gender,job,telephone):
        self.open()
        self.cur.execute('insert into user (username,password,age,gender,job,telephone) values (?,?,?,?,?,?)',(username,password,age,gender,job,telephone))
        self.con.commit()
        self.close()
    def selectAllMassage(self):
        self.open()
        row = self.cur.execute('select * from user')
        data = self.cur.fetchall()
        self.close()
        return data
    def selectPassword(self,username,password):
        self.open()
        row = self.cur.execute('select username,password from user where (username = ? and password = ?)',(username,password))
        data = self.cur.fetchall()
        self.close()
        if(len(data)==0):
            return False
        else:
            return True
    def deleteDb(self,key):
        self.open()
        self.cur.execute('delete from user where username = ?',(key,))
        self.con.commit()
        self.close()
    def close(self):
        self.cur.close()
        self.con.close()
# model = Datebase('test.db')
# model.creatDatebase()
# model.inserMassage(username='田所',password='big',age=24,gender='男',job='学生',telephone=114514)
# liss = model.selectPassword('小明',"big")
# print(liss)
