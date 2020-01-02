#ecoding=utf-8
#学生管理系统
import time
def studSystem():
    print("="*30)
    print("  学生管理系统V1.1 ")
    print("1、添加学生信息")
    print("2、删除学生信息")
    print("3、查询学生信息")
    print("4、修改学生信息")
    print("5、遍历学生信息")
    print("6、退出系统")
    print("="*30)
#添加信息
def addStudent(students):
    print("***您选择了添加学生信息选项***")
    studinfo = {}
    studinfo["name"] = raw_input("请输入学生姓名：")
    studinfo["age"] = raw_input("请输入学生年龄：")
    studinfo["ID"] = raw_input("请输入学生学号：")
    students.append(studinfo)
#遍历信息
def viewStud(students):
    print("***您选择了遍历学生信息选项***")
    print("***请稍后***")
    time.sleep(1)
    print(" 姓名    年龄    学号")
    for temp in students:
        print  ("%s   %s  %s"%(temp["name"],temp["age"],temp["ID"]))
#删除信息
def removeStud(students):
    print("***您选择了删除学生信息选项***")
    i = int(raw_input("请输入您要删除的序号"))
    del students[i-1]
    print("删除成功！删除后剩余学生如下：")
    print(" 姓名  年龄  学号")
    for temp in students:
        print  ("%s   %s  %s"%(temp["name"],temp["age"],temp["ID"]))
#查询信息
def findStud(students):
    nameFind = raw_input("请输入你要查询的学生姓名：")
    for student in students:
        if nameFind == student["name"]:
            print("您要查找学生（%s）的信息如下："%nameFind)
            print(" 姓名  年龄  学号")
            print student["name"], student["age"], student["ID"]
            tempjust = 0
            break
        else:
            tempjust = 1
# 定义一个变量让未找到学生给出提示
    if tempjust == 1:
        print("抱歉，没有找到该学生")
    else:
        pass
#修改信息
def changeStud(students):
    nameTemp = raw_input("请输入你要修改学生的姓名：")
    for student in students:
        if student["name"] == nameTemp:
            tempStud = int(raw_input("请在（1.姓名；2.年龄；3.学号）中选择一项修改："))
            if tempStud == 1:
                newName = raw_input("请输入修改后的姓名:")
                student["name"] = newName
            elif tempStud == 2:
                newAge = raw_input("请输入修改后的年龄:")
                student["age"] = newAge
            elif tempStud == 3:
                newID = raw_input("请输入修改后的学号：")
                student["ID"] = newID
            else:
                print ("输入有误，请重新输入！")
            print ("修改成功！")
            print(student["name"], student["age"], student["ID"])
            tempjust = 0
            break
        else:
            tempjust = 1
#定义一个变量让未找到学生给出提示
    if tempjust == 1:
        print("抱歉，没有找到该学生，请重新输入")
    else:
        pass
#退出系统,这里不建议使用函数
# def breakStud():
#     out = raw_input("你确定要退出系统吗？呜呜呜~~（yes/no）:")
#     if out == "yes":
#         print("后会有期！")

students = []
while True:
    studSystem()
    num = int(raw_input("请输入你要操作的选项："))
    if num==1:
        addStudent(students)
    elif num==2:
        removeStud(students)
    elif num == 3:
        findStud(students)
    elif num == 4:
        changeStud(students)
    elif num == 5:
        viewStud(students)
    elif num == 6:
        out = raw_input("你确定要退出系统吗？呜呜呜~~（yes/no）:")
        if out == "yes":
            print("后会有期！")
            break
    else:
        print("输入有误，请重新输入！")

