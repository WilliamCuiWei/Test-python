#ecoding=utf-8
i=0
while i<5:

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
	i+=1    



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#ecoding=utf-8
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
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
class Home:

	def __init__(self,area):
		self.area = area
		self.rongnaList = []
	def __str__(self):
		msg = "家可用面积是"  + str(self.area)
		if len(self.rongnaList) >0:
			msg += "；床的名字是"
			for temp in  self.rongnaList:
				msg = msg +  temp.getBedName() + '，'
			msg = msg.strip('，')
		return msg
	def containBed(self,item):
		bedArea = item.getBedArea()
		if self.area >= bedArea:
			self.rongnaList.append(item)
			self.area -= bedArea
			return self.area
		else:
			print("error: the area is not enough")

class Bed:

	def __init__(self,area,name):
		self.area = area
		self.name = name

	def getBedArea(self):
		return self.area

	def getBedName(self):
		return self.name

home = Home(180)
print(home)

bed = Bed(4,'小床')
home.containBed(bed)
print(home)

bed2 = Bed(166,'大床')
home.containBed(bed2)
print(home)
