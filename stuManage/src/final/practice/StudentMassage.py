from sqlite3 import connect
dbname = "StudentMassage.db"
# 连接数据库
con = connect(dbname)
# 获取游标
cur = con.cursor()
def createDb():
    # 初次登陆创建数据库
    try:
        cur.execute('create table StudentMassage(name text,number integer,major text,grade text,score integer)')
    except:
        return False
def insertDb(name,number,major,grade,score):
    cur.execute('insert into StudentMassage(name,number,major,grade,score) values (?,?,?,?,?)',(name,number,major,grade,score))
    # 上传提交
    con.commit()
def delDB(primary):
    # 删除单个学生的所有信息    输入学号或者姓名
    cur.execute('delete from StudentMassage where (name = ? or number =?)',(primary,primary))
    con.commit()
def selectDb(number):
    # 搜索输入学号或者姓名
    try:
        row = cur.execute('select * from StudentMassage where (name = ? or number =?)',(number,number))
        for i in row:
            return print(i)
    except:
        print("未搜索到该内容")
    finally:
        con.close()
def updateDb(massage,new_massage,number):
    # 修改学生信息
    # 不正确
    cur.execute('update StudentMassage set ?=? where (name =? or number = ?)',(massage,new_massage,number,number))
    con.commit()
    con.close()
# updateDb("score",100,"小明")
# insertDb("小明",114,"云计算","一年级",95)
# insertDb(114,"小红","物联网","二年级",98)
rua = cur.execute('select score from StudentMassage where name = {}'.format("小明"))
for i in rua:
    print(i[0])
selectDb("小明")
