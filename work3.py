#ecoding=utf-8
import random

offices = [[],[],[]]

teachers = ["A","李","阳","D","E","F","G","H",]

for temp in teachers:
	index = random.randint(0,2)
	offices[index].append(temp)
	
#print offices

# i = 1
# for room in offices:
# 	print("====the room %d is==="%i)
# 	for teachersname in room:
# 		print teachersname
# 	i+=1	

i = 0
while i<3:
	temp = offices[i]
	print("====the room %d is==="%(i+1))
	for name in temp:
		print name
	i+=1




#ecoding=utf-8
class People(object):
	address = '山东' #类属性
	#实例方法
	def __init__(self):
		self.name = 'xiaowang' #实例属性
		self.__age = 20
	#类方法，不是实例方法
	@classmethod
	def setNewAddress(cls):
		cls.address = "内蒙古"

xiaowang = People()
# xiaowang.setNewAddress()
print(xiaowang.name)
print(xiaowang.age)
print(People.address)
print(xiaowang.address)
People.setNewAddress()
print("="*18)
print(xiaowang.address)
print(People.address)