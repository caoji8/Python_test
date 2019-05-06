from sqlite3 import connect
dbname = "StudentMassage.db"
# 连接数据库
con = connect(dbname)
# 获取游标
cur = con.cursor()
def createDb():
    try:
        cur.execute('create table StudentMassage(name text,number integer,major text,grade text,score integer)')
    except:
        return False
def insertDb(name,number,major,grade,score):
    cur.execute('insert into StudentMassage(name,number,major,grade,score) values (?,?,?,?,?)',(name,number,major,grade,score))
    # 上传提交
    con.commit()
    con.close()
