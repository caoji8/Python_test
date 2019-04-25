#coding:utf-8
from stuManage.src.final.practice.student import Student
class MsgPrint(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # self._krgs = krgs

    #开始 第一层选择菜单
    def mainMenu(self):
        print("*************欢迎使用学生成绩管理系统*************\n\
              1、学生管理\n\
              2、学生查找\n\
              3、成绩管理\n\
            请输入编号进入相应菜单")
        choose = input(">")
        choose = int(choose)
        if choose == 1:
            #管理模块
            self.ManagementChoose()
            # self.studentManageMenu()
        elif choose == 2:
            #查找模块
            self.StudentSeek()
        elif choose == 3:
            #成绩模块
            self.Score_management()
        else:
            print("Error choose")

    def Score_management(self):
        print("*************欢迎使用学生管理系统*************\n\
                      1、成绩修改\n\
                      2.专业排名\n\
                    请输入编号进入相应菜单")
        Score_choose = input(">")
        Score_choose = int(Score_choose)
        if Score_choose == 1:
            # 成绩修改
            stu_score = Student()
            stu_score.alert()
        elif Score_choose == 2:
            # 专业排名
            stu_score = Student()
            stu_score.alertScore()
        else:
            print("Error")

    #查找模块
    def StudentSeek(self):
        print("*************欢迎使用学生管理系统*************\n\
                      1、学号查找\n\
                      2、专业查找\n\
                      3、年级查找\n\
                    请输入编号进入相应菜单")
        choose = input(">")
        choose = int(choose)
        if choose == 1:
            #学号查找
            stu_seek = Student()
            stu_seek.select()
            # self.studentManageMenu()
        elif choose == 2:
            # 专业查找
            major_Seek = Student()
            major_Seek.keyword_search("major")
        elif choose == 3:
            #年级查找
            grade_seek =Student()
            grade_seek.keyword_search("grade")
        else:
            print("Error choose")
    def ManagementChoose(self):
        print("*************欢迎使用学生管理系统*************\n\
              1、添加\n\
              2、删除\n\
              3、修改\n\
            请输入编号进入相应菜单")
        Management_choose = input(">")
        Management_choose = int(Management_choose)
        if Management_choose == 1:
            #添加
            self.studentManageMenu()
        elif Management_choose == 2:
            #删除
            stu_delete = Student()
            stu_delete.delete_input()
        elif Management_choose == 3:
            #修改
            stu_modify = Student()
            stu_modify.alert()
        else:
            print("Error")


    def studentManageMenu(self):
        print("*************欢迎使用学生管理功能模块*************\n\
    请输入学生信息：姓名，学号，专业，年级，成绩")
        studentManage_inpnt = input(">").split(",")
        if len(studentManage_inpnt)==5:
            #存储
            student = Student(studentManage_inpnt[0],studentManage_inpnt[1],studentManage_inpnt[2],studentManage_inpnt[3],studentManage_inpnt[4])
            estimate = student.add()
            #判断是否添加成功
            if estimate:
                print("添加成功")
            else:
                print("添加错误")
        else:
            print("Error input")

            #打印查找功能
    def studentManageInfo(self):
        if isinstance(self._krgs, dict):
            nametitle = "{0: ^15}".format("姓名")
            notitle = "{0: ^21}".format("学号")
            majortitle = "{0: ^16}".format("专业")
            gradetitle = "{0: ^16}".format("年级")
            scoretitle = "{0: ^21}".format("成绩")
            title = nametitle+"|"+notitle+"|"+majortitle+"|"+gradetitle+"|"+scoretitle+"|"
            print(title)
            for stu in self._krgs["key"]:
                name = "{0: ^15}".format(stu["name"])
                no = "{0: ^15}".format(stu["no"])
                major = "{0: ^15}".format(stu["major"])
                grade = "{0: ^15}".format(stu["grade"])
                score = "{0: ^15}".format(stu["score"])
                stu_info = "{0}|{1}|{2}|{3}|{4}|"
                stu_info=stu_info.format(name,no,major,grade,score)
                print(stu_info)
        else:
            print("the input must be dict!")
        

                
            
        
        