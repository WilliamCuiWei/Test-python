#ecoding=utf-8
# count=0
# while True:
#     print 'Repeat this line !'
#     count=count+1
#     if count==5:
#         break
#
#
# import time
#
# name=raw_input("请输入姓名:")
# qq=raw_input("请输入QQ:")
# tel=raw_input("请输入电话:")
#
# print ("系统正在打印中。。。")
# time.sleep(2)
#
# print("==============================")
# print ("您的姓名是：%s"%name)
# print ("您的QQ是：%s"%qq)
# print ("您的电话是：%s"%tel)
# print("==============================")

#if循环的嵌套
name=raw_input('请输入您的用户名:')
password = raw_input('请输入您的密码:')
if name=='xiaoming' and password == '12345':
    print('登录成功!')
elif name=='xiaoming' or password=='12345':
    print('您的密码或者用户名错误，请重新输入!')
else:
    print ('密码用户名都错啦')

#if循环的嵌套
password = raw_1input('Password:')
if password =='12345':
    print('Login success!')
else:
    print('Wrong password or invalid input!')


#1-100偶数和
i = 1
sum=0
while i<=100:
    if i%2==0:
        sum=sum+i
    i+=1
    print ('%d 循环第%d次'%(sum,i))


#九九乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        print ('%d*%d=%-2d'%(j,i,i*j)),
        j+=1
    print ('\n')
    i+=1

#break:结束整个循环
#continue:结束本次循环，继续进行下一次的循环

fileName = ["01.py","023.c","0344.doc","04123.html","05551.php","0.java"]
for temp in fileName:
    weizhi = temp.rfind(".")
    print weizhi
    print temp[weizhi:]
    print "="*8



#1~任意值的求和
def printNum(num):
    i = 1
    sum = 0
    while i<=num:
        sum=sum+i
        i+=1
    return sum

num = int(raw_input("请输入需要求和的数字："))

result = printNum(num)
print("="*12)
print("计算的结果是：%d"%result)
print("="*12)




def namePrint():
    for name in nameList:
        return name
result = namePrint()

print("="*20)
print("您输入的姓名是：%s"%result)
print("="*20)



#登录系统，没有参数没有返回值
def printSystem():
    print ("-"*20)
    print("名片系统V9.9：")
    print("1.添加名片：")
    print("2.删除名片：")
    print("3.修改名片：")
    print("4.查询名片：")
    print("5.遍历名片：")
    print("6.退出系统：")
    print ("-"*20)

#获取用户信息,没有参数有返回值
def nameInput():
    num = int(raw_input("请输入序号（1-2-3-4-5）："))
    return num

#遍历名字,有参数无返回值
def namePrint(nameTemp):
    print("=" * 20)
    for temp in nameTemp:
        print temp
    print("=" * 20)

nameList = []
addList = []

i = 0
while i<10:
    printSystem()
    lum = nameInput()
    if lum==1:
        print("您选择了添加名片功能")
        name = raw_input("请输入您的姓名：")
        nameList.append(name)
    elif lum==5:
        namePrint(nameList)
    else:
        print("输入有误，请重新输入")
    i+=1

#打印给定行数的直线
def printLine():
    print("-"*30)

def printLine_2(n):
    i = 0
    while i<n:
        printLine()
        i+=1
num = int(raw_input("请输入要打印的行数:"))
printLine_2(num)

#写一个函数求三个数的和
def printSum(num):
    numSum = 0
    i = 0
    while i<num:
        numSum = numSum+list[i]
        i+=1
    return numSum
#求三个数的平均数
def printAve(num):
    result = printSum(num)
    Average = result/num
    reminder = result%num
    return Average,reminder
    #tempList = [Average,reminder]
    #return tempList
    #result = {"average":Average,"reminds":reminder}#推荐使用字典方式
    #return result

list = []
n = int(raw_input("请输入数字个数："))
i = 0
while i<n:
    list.append(int(raw_input("请输入第%d个数字："%(i+1))))
    i+=1

result = printSum(n)
print("求和的结果是：%d"%result)

a,b = printAve(n)
print("平均数整数是：%d"%a)
print("平均数余数是：%d"%b)
# temp = printAve(n)
# print("平均数整数是：%d"%temp.get("average"))
# print("平均数余数是：%d"%temp.get("reminds"))


#写一个函数求三个数的和
def printSum(a,b,c):
    result = a+b+c
    return result

#求平均值
def printAver(a,b,c):
    result = printSum(a,b,c)
    average = result/3
    return average
iii = printAver(44,55,66)
print(iii)


#不定长参数的用法
def test(a,*b):
    #print a
    #print b
    sum = 0
    for i in b:
        sum=i+sum
    result = sum+a
    return result
resultTemp = test(1,2,33,3,3,1,3)
print (resultTemp)

#不定长参数的用法
def test(a,*b,**c):
    print a
    print b
    print c

test(1,2,33,3,m=3,n=1,h=3)

#递归  指定数求1~n的和
def test(num):
	if num>1:
		result = num+test(num-1)
	else:
		result = 1
	return result


result = test(3)
print (result)

#创建类
class Dog:
    def __init__(self,newName,newWeight,newColor):
        self.weight = newWeight
        self.color = newColor
        self.name = newName
    def bark(self):
        print("狗在叫：旺旺。。")
    def run(self):
        print("狗在跑、、、")
    def eat(self):
        print("狗在吃东西、、")
        self.weight += 4
    def printName(self):
        print("名字是%s"%self.name)
xiaogou = Dog("大白",5,'黄色')
xiaogou.printName()
print xiaogou.weight
print xiaogou.color


wangcai = Dog("小黑",10,'黑色')
wangcai.printName()
print wangcai.weight
print wangcai.color


#烤地瓜
class SweetPatatos:
	def __init__(self):
		self.Levels = 0
		self.Strings = "生的 "
		self.Ingredients = []

	def __str__(self):
		msg = "地瓜的状态是:" + self.Strings
		if len(self.Ingredients)>0:
			msg += ',添加的作料为：'
			for temp in self.Ingredients:
				msg = msg + temp + ', '
			msg = msg.strip(', ')
		return msg

	def cook(self, time):
		self.Levels += time
		if self.Levels > 8:
			self.Strings = "烤糊了"
		elif self.Levels > 5:
			self.Strings = "烤熟了"
		elif self.Levels > 3:
			self.Strings = "半生不熟"
		else:
			self.Strings = "生的"
	def cookIngredients(self,temp):
		self.Ingredients.append(temp)

digua = SweetPatatos()
digua.cook(2)
print (digua)
print("="*30)
digua.cook(2)
digua.cookIngredients("番茄酱")
digua.cookIngredients("芝麻酱")
print (digua)
print("="*30)
digua.cook(2)
print (digua)
print("="*30)
digua.cook(3)
print (digua)


class Home:
    def __init__(self, area):
        self.area = area
        self.rongnaList = []
        self.light = 'off'

    def __str__(self):
        msg = '家当前使用面积为' + str(self.area) + "平方米。" + '灯的状态是：' + self.light + '；'
        if len(self.rongnaList) > 0:
            msg += "当前已有的床有："
            for temp in self.rongnaList:
                msg = msg + temp.getBedName() + '、'
            msg = msg.strip('、')
        return msg

    def containItem(self, item):
        bedName = item.getBedName()
        bedArea = item.getBedArea()
        if self.area >= bedArea:
            self.rongnaList.append(item)
            self.area -= bedArea
            print("当前添加物品[%s]成功,家当前可用面积为：%d" % (bedName, self.area))
        # msg = "当前已有的床："
        # for temp in self.rongnaList:
        # 	msg = msg + temp.getBedName() +'、'
        # msg = msg.strip('、')
        # print msg
        else:
            print("error:当前物品添加[%s]的面积大于家的面积,添加失败" % bedName)

    def turnLightOn(self):
        self.light = 'on'
        for temp in self.rongnaList:
            temp.turnBedLight()

    def turnLightOff(self):
        self.light = 'off'
        for temp in self.rongnaList:
            temp.turnBedOff()


class Bed:
    def __init__(self, area, name):
        self.area = area
        self.name = name
        self.light = 'off'

    def __str__(self):
        msg = '我有一张床叫' + self.name + "，占用面积" + str(self.area) + "平方米。" + "当前明暗状态是：" + self.light
        return msg

    def getBedArea(self):
        return self.area

    def getBedName(self):
        return self.name

    def turnBedLight(self):
        self.light = 'on'

    def turnBedOff(self):
        self.light = 'off'


home = Home(180)
print(home)

bed = Bed(4, '席梦思')
print(bed)

print('=' * 40)
home.containItem(bed)
print(home)

print('=' * 40)
bed2 = Bed(10, '木板床')
home.containItem(bed2)
print(home)

print('=' * 40)
bed3 = Bed(196, '超大床')
home.containItem(bed3)
print(home)

print('=' * 40)
home.turnLightOn()
print(home)
print bed
print bed2
print bed3

print('=' * 40)
home.turnLightOff()
print(home)
print bed
print bed2
print bed3


#保护属性的方法
class Person(object):
    def __init__(self, name, age):
        self.__name = name  #私有属性
        self.__age = age    #私有属性
        self.height = 180   #公有属性
    def __str__(self):
        return "年龄是：" + str(self.age)
    def setNewAge(self,newAge):#设置属性
        if newAge >0 and newAge < 80:
            self.age = newAge
    def getAge(self):        #获取属性
        return self.__age
xiaoming = Person("xiaoming",18)
print(xiaoming)

xiaoming.setNewAge(119)
print(xiaoming)
