#coding:utf-8
class Student(object):
    '''
            学生类
    '''
    '''全局变量，存放学生信息'''
    list_students = [{"name":"张三","number":1234567890,"major":"物联网","grade":"一年级","score":90},
                     {"name":"王五","number":1234567891,"major":"云计算","grade":"二年级","score":90}]


    def __init__(self,name=None,number=None,speciality=None,grade=None,score=None):
        '''学生实例初始方法
                                 输入：属性（姓名、学号、专业、年级、成绩）
                                   输出：无                      
        '''
        self.name = name
        self.number =number
        self.speciality =speciality
        self.grade = grade
        self.score = score
    
    def add(self):
        '''学生信息添加方法
                                 输入：姓名、学号、专业、年级、成绩
                                输出：true/false                      
        '''
        stu_obj = {}
        stu_obj["name"] = self.name
        stu_obj["number"] = self.number
        stu_obj["speciality"] = self.speciality
        stu_obj["grade"] = self.grade
        stu_obj["score"] = self.score
        self.list_students.append(stu_obj)
        print("添加成功")
        printtest = MsgPrint()
        printtest.mainMenu()

    def delete_input(self):
        '''学生信息删除方法
                                 输入：学号
                                输出：true/false                      
        '''
        delete_input = input("请输入要删除学号")
        delete_input = int(delete_input)
        index = 0
        for i in self.list_students:

            for key, value in i.items():
                # print(key,value)
                if key == "number":
                    if value == delete_input:
                        self.list_students.pop(index)
                    else:
                        pass
            index += 1
        print("删除成功")

    def alert(self):

        '''学生信息修改方法
                                 输入：姓名、学号、专业、年级
                                输出：true/false                      
        '''
        modify_input = input("请输入您的姓名，修改的类别和内容").split(",")
        for i in self.list_students:
            for key, value in i.items():
                # 判断是否在全局变量中
                if value == modify_input[0]:
                    # 键值对来直接更改
                    i[modify_input[1]] = modify_input[2]
                    print("修改成功")


    def select(self):
        '''学生信息查找方法
                                 输入：学号、专业、年级
                                输出：学生信息                      
        '''
        user = input("请输入学号或者姓名").split()
        for i in self.list_students:
            if user[0] in i.values():
                print(i)
    #关键字查找 查找专业年纪
    def keyword_search(self,choose):
        user = input("请输入姓名").split()
        for i in self.list_students:
            if user[0] in i.values():
                print(i[choose])
        #传入的参数用来复用时判断查找类型

    def alertScore(self):
        '''学生成绩排名方法
                                 输入：学号、成绩
                                输出：true/false                      
        '''
        list = []
        user = input("请输入姓名").split()
        for i in self.list_students:
            for key, value in i.items():
                if key == "score":
                    list.append(value)
                if value == user[0]:
                    a = i["score"]
                    print(a,"分")
        list.sort()
        print("第",list.index(a) + 1,"名")
        list.sort()


    def rankScore(self):
        '''学生成绩修改方法
                                 输入：专业
                                输出：学生信息                      
        '''
        pass
