#ecoding=utf-8
# password = raw_input('密码:') 
# if password == '12345': 
#     print('Login success!')  
# else:   
#     print('Wrong password or invalid input!')


#0石头 1剪刀 2布
import random
#玩家和电脑输入信息
player=int(raw_input('what is your choice:'))
comp=random.randint(0,2)
#判定
if (player==0 and comp==1) or (player==1 and comp==2) or (player==2 and comp==0):                 #赢了
	print('you win!')
elif player==comp:              #平局
	print('the same!')
else:                           #输了
    print('you are a loser!')
      
# 如果安装有 python3, 则需要明确 pip 版本
# py -2 -m pip install sth
# py -3 -m pip install sth 


字符串操作：mystr = 'tangcweo'
查找：find或者index；rfind或者rindex
计数：count
替换：replace   mystr.replace('j','J')
切分：mystr.split('j')
字符串首字母大写：capitalize
每个单词首字母大写：title
所有大写变小写：lower------upper
检查字符串是否以XX开始或结束：startswith endswith
左右添加10个空格：mystr.ljust(10) rjust(10)
加10个空格使字符串居中：mystr.center(10)
删除左右末尾空白字母：mystr.lstrip() mystr.rstrip()
同时删除两边空白:mystr.strip()
切分之后中间无消耗:mystr.partition()   rpartition  只切一次
去除换行符(/n) ：mystr.splitlines() 
判断是否全是字母:mystr.isalpha()  
判断是否全是数字:mystr.isdigit() 
判断是否既有数字又有字母:mystr.isalnum() 
判断字符串是否为纯空格:mystr.isspace() 
重新连接字符串:mystr.join("123")




列表的操作
增：append("dongGe")   insert(下标,"abc")
    a = [1,2,3]
    b = ["a","b"]
    a.extend(b)-------->[1,2,3,"a","b"]
删:
    
	del movieNames[0] 				可以按下标删
	movieNames.pop()        		删除最后一个
	movieNames.remove("加勒比海盗") 按名字元素值删除

改：movieNames[2] = "指环王"

查：0,1表示标志位
   in   if "abc" in names:
	   	   print("找到了")

   not in 
   
   index()	a.index("a",1,3)  范围内查找

   count()  a.count("b")       查找数量


set  去重函数 
tang.sort()排序函数

自己编写来实现：在遍历过程中进行判断，如果找到了，那么就标记退出，如果没有找到那么也标记。

字典 c = {'name':'xiaoming','sex':'female',"QQ":1234}

增：c["age"] = 14

删：del c["name"]
    del c
    c.clear()
改：c["age"] = 18

查： c["name"]
     c.get("age",110) #110, 如果指定键的值不存在时，返回该默认值。
     c.get("name",110)  #python2,3

字典常用操作：info = {'name':'xiaoming','sex':'female',"QQ":1234}
len(info)
info.keys()
info.values()
info.items()
info..update()
for i,j in info.items():
	print("key=%s,value=%s"%(i,j))

判断 info.has_key("weight")  #python2

帮助文档 help(info)

data_science = dict(zip(range(10), reversed(range(10)))) 
data_science

字典遍历
i = 0
for x in info:
	print(i,x)
	i+=1

for i,y in enumerate(info):
	print(i,y)

枚举enumerate() 打印下标 不用定义新变量 


函数：具有独立功能的代码块 def printFoZu():

1、库函数 2、自定义函数
步骤：
1、按照原来的代码编写方式 先写上
2、定义函数，把第一步的代码放进去

函数名要-->见名知意

函数中有return ，作用是把后面的变量的结果保存
1、无参数无返回值   往往直接打印
2、无参数有返回值
3、有参数无返回值
4、有参数有返回值

函数做了很复杂的事，且需要这个结果，则有return
如果仅需要函数打印，则没有return

写函数的时候先写大体的框架，再看是否需要参数或者返回值，不要一步到位。想一步做一步。

修改代码时，不要修改之前的原函数，最好采用调用原函数的方式

1.局部变量：
  在函数里面定义的变量，就叫做 局部变量
  只在定义它的函数内有效，出了函数就没有了
  形参也是 局部变量
 2.全局变量：
  在函数外面定义的变量，就叫做 全局变量
  如果在函数中直接修改全局变量，那么会产生异常
  需要修改全局变量，那么可以在函数里面进行声明 global

引用
  可变类型 ：贴标签
  列表list
  字典dict

  不可变类型，值不可以改变
  数值类int ,long,bool,float
  字符串str
  元组tuple

如果全局变量是可变类型，即列表或字典，那么可以在函数中直接修改，
而不可变类型，比如int，不能直接在函数中修改，需要加上global

注意：
a+=1#直接修改
a = 100#因为全局变量a不能改，所以此时是定义了一个变量

如果全局变量和一个局部变量名字相同，那么函数中用的是局部变量
优先级：局部变量>全局变量

#g_a = 200，为了和局部变量防止名字相同，加上下划线区分

如果一个函数中有多个return,那么程序只要执行一个return,
剩下的所有return都不会被执行。
return一旦被调用，会立即结束当前的函数
类似于break，直接结束，只不过是结束函数

return返回多个返回值
1、直接加逗号返回多个值，结果是一个元组
2、列表、元组、字典均可以
在最后调用的时候可以直接生成多个变量。

编写程序的思路：
1、搭框架，顺推和倒推

缺省参数：缺省参数必须放在后面，没缺省的在前面
不定长参数:第一个参数必须要传，后面的可以不传

def test2(a,*b,**c):
	print a
	print b
	print c
test2(1,22,33,5,m=23,n=56)

原来的时候为了好理解，所以a+=a<==>a=a+a
其实a+=a是在数据上修改，a=a+a是先定义一个变量再修改


栈：先进后出，后进先出
队列：先进先出


####复习#####：
1.怎样存储数据
	1.变量 num age
	2.字符串 "hello world"
	3.列表
		1.[11,"xiaowang",3.14]
	4.元组
		1.(11,22,33,0.36,"xiaowang")
		2.元组数据不能修改
	5.字典
		1.{}
		2.{"name":"xiaowang","age":18}
		3.xxx["name"]----->xxx.get("name")不报错	
2.怎样使用数据
	1.+ - * / % // **
		num%3
		num/3
		num//3
	2.if判断
		if xxxx:
			满足时做的事情
		True--->表示满足条件
		False--->表示不满足
	3.while循环
		i=0
		while i<n:
			xxxxx
			i+=1
		while True:
			xxxxx
3.函数
 	def 函数名():
 		执行的语句
 	1.无参数 无返回值
 	2.无参数 有返回值
 	3.有参数 无返回值
 	4.有参数 有返回值

 	5.定义一个全局变量，所有的函数都可以使用（不可变类型修改需要加global）
 	6.不使用全局变量，而是局部变量，采用传参数的方式进行
 	7.先把函数设定无参数无返回值的形式，根据实际需求再改。
 	def 函数1():
 		xxxx
 	def 函数2():
 		xxxx
 	def 函数3():
 		xxxx
 	def main():
 		result = 函数1()
 		函数2(result)
 		函数3()
 	main()


 	属性---数据
 	+
 	方法---函数（行为）
 	=
 	类

 	类名要用大驼峰法命名

 	当调用对象是，python解释器默认把这个对象作为self传入，
 	开发者只需传剩下的参数即可。

 	禁止使用对象直接修改属性，而应该封装一个方法来进行修改。

 作业：
 家、床  定义str方法

 API 应用编程接口 可以调用数据，但不可更改

 思想：

 1.面向过程
 	1.提示用户输入
 	2.获取两个数
 	3.计算
 	4.输出
 	把数据保存起来---->变量（int、列表、元组、字典）
 	把一块代码保存起来---->函数
 	把数据和代码保存起来当做一个整体---->对象
 2.面向对象
 	1.创建一个对象
 	2.对象.方法/属性

 class 类1：

 	def 方法1()
 		xxx

对象 = 类1()
对象.方法1()

#如果有(object)叫 新式类，之前的叫 经典类

引用计数

__del__   python解释器管理内存的方法，用于结束语

继承
class Person(object):
	def __init__(self, name ='ren', age='10'):
		self.__name = name
		self.__age = age
	def __str__(self):
		msg = 'his name is '+self.__name +';and his age is' + self.__age
		return msg
	def namePrint(self,vioce = "fsdfsdf"):
		print self.__name
		print self.__age
		return vioce		
class Male(Person):	
	def maleHeight(self):
		print('height is 180cm')
	def __def__(self):
		print 'It always go end'		
# xiaoming = Person("xiaoming",18)
# print xiaoming.namePrint()
xiaowang = Male(name = "xiaoming",age = "118")
print (xiaowang)
# xiaowang.maleHeight()
# xiaowang.namePrint()

父类  子类  
如果是通过继承来的方法来访问父类的私有属性是可以的
如果是在子类中，自定义了一个方法，此方法不能访问父类的私有属性		
私有属性不会被继承

如果在方法名前面有2个下划线，这个方法就成了私有方法，也不能继承。

调用父类的方法

class Animal(object):
			
	def bark(self):
		print("啊啊啊啊")

class Cat(Animal):
	def bark(self):
		Animal.bark(self)   #加self
		super(Cat,self).bark()      #不加self
		print("喵喵、、")
tom = Cat()
tom.bark()

广度遍历

类属性：类对象里面，方法外面
实例属性：跟着对象走，方法里面
一块代码---类对象
实际创建----实例对象
可以通过类名的方式来获取类属性，
但是不能通过类名获取实例属性，只能先创建一个对象
类属性可以通过类名修改

class People(object):
	address = '山东' #类属性
	#实例方法
	def __init__(self):
		self.name = 'xiaowang' #实例属性
		self.age = 20
	#类方法
	@classmethod
	def setNewAddress(cls):
		cls.address = "内蒙古"

# People.setNewAddress()
print(People.address)
xiaoming = People()
xiaoming.setNewAddress()
print xiaoming.address
类对象可以调用类属性和类方法；但不允许调用实例属性，也不允许调用实例方法
实例对象可以获取实例属性和类属性的值，但只能修改实例属性，不能修改类属性
它也可以调用实例方法和类方法


捕获异常
try:
	可能出现异常的代码
except nameError,errorMsg:
	如果出现了一种异常，这里会执行
else:
	没有出现异常，这里会执行
finally:
	不管有没有异常，这里都会被执行
例子：
try:
	num = 100
	num = hihi
	print num
except nameError,errorMsg:
	print("产生错误了：%s"%errorMsg)
else:
	print("没有捕获到错误，真高兴")
finally:
	print("我一定会执行哦！")



html:显示数据的内容
css：显示数据的样子颜色  三种方式：外联式、嵌入式、内联式
js  javascript:访问html的数据，检测和操作相关的登录、密码

根据标签(label)、ID(井号id)、类(.类名)来进行选择颜色格式



模块测试：
def main():
	print "we are in %s"%__name__
	
if __name__ == '__main__':
	main()

直接执行__name__,结果为__main__
被调用的时候结果为test


包：含有__init__.py的文件


爬虫：

BeautifulSoup 
soup.select() 选择器
1.按标签找 soup.select('a') 
2.按类找(.) soup.select('.sister') 点
3.按id找  soup.select('#link1')    井号
4.组合方法查找  soup.select('p #link1')
5.直接子标签查找   soup.select('head > title')
6.按照属性查找  soup.select('a[class = sister]')

7.最后找属性的值 aa['href']  
8.获取文字   aa.string   test[0].string


网址拼装 parament = urlencode({'t':'b','w':"ios"})
get方法： urlopen(url)
post方法： 
xxxx = urlencode({'t':'b','w':"ios"})
urlopen(url,xxxx)


一、numpy包
#numpy独特取数方法
import numpy as np
X = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20]])  
print X[1:3] 
print X[1:3,:] 

1、生成随机数     values = np.random.randn(10,2)，np.random.rand(10)均为正数 或者A = np.random.random((10,2))或者np.random.randint(2,10,size = 10)
2、生成整数       hi = np.random.random_integers(8,size = 10)或者np.random.random_integers(8, 10)
3、生成标准正态分布   samples = np.random.standard_normal(50)或者np.random.standard_normal((50,2))或者高斯分布 np.random.normal(loc=0，scale=1,size=(4,4))
4、生成固定区间数  A = np.linspace(-6,6,4)或者 A = np.arange(36).reshape(9,4) （适用于整数）
5、生成数组       B = np.array((-1,1))


fancy = np.arange(36).reshape(9,4) 
print fancy
fancy[[1,4,3,2],[3,2,1,0]]
fancy[[1, 4, 3, 2]][:, [0, 1, 2, 3]]

ra = np.random.randn(5,5)
print ra
print np.where(ra>0, 1, -1) 

print "The sum are :{}".format(np.sum(fancy, axis =0)) #0 列求和；1 行求和
print fancy.sum(0)  #同上
fancy.cumsum(0)  #0 列累计求和；1 行累计求和
fancy.sort() #升序
frame2.sort_index(axis = 0)
np.unique(fancy)  或者  set(personals) # 去重返回唯一值  
np.in1d(personals, ['Manu']) #'Manu'返回True

from numpy.linalg import inv, qr
dot()函数是矩阵乘，而*则表示逐个元素相乘
np.linalg.qr() 计算矩阵的QR分解。把矩阵A作为QR，q是正交的，r是上三角形。
np.linalg.inv() 矩阵求逆
np.linalg.det() 矩阵求行列式（标量）

一、pandas包

两种数据结构：
Series 
DataFrame
india[['Population', 'Language']]           筛选列
india.ix[['a','b'], ['State','Language']]   ix用来筛选index行


apply()    当想让方程作用在一维的向量上时，可以使用apply来完成
	f = lambda x: x.max() - x.min()
	frame.apply(f)
applymap() 如果想让方程作用于DataFrame中的每一个元素，可以使用applymap()
	format = lambda x: '%.2f' % x
	frame.applymap(format)
map()  只要是作用将函数作用于一个Series的每一个元素
	frame['e'].map(format)



df.drop_duplicates('instance_id','first',True） 去重函数