#ecoding=utf-8
class Animal(object):
    def __init__(self,name = "原始动物",color = "白色"):
        self.__name = name
        self.__color = color
    def __str__(self):
        msg = '这种动物名字是：' + self.__name +'；'+'颜色为：'+self.__color + self.eat() +str(self.run()) +str(self.bark())
        return msg
    def eat(self,food = "；是食草动物"):
        return food
    def bark(self,vioce= ";叫声是：呜呜呜、、、"):
        return vioce
    def run(self,step = ";跑步速度一般"):
       return step


class Horse(Animal):
    horseNum = 0
    def bark(self,vioce = "；叫声是：嘿嘿嘿、、、"):
        return vioce
    def run(self,step = "；跑步速度很快"):
       return step

class Donkey(Animal):
    def bark(self):
        print("咩咩咩、、、")
    def run(self):
       print "跑步速度很慢"

class HanxueBaoma(Horse):
    def setColor(self,newcolor):
        self.color =newcolor
        print newcolor
    def bark(self):
        print("哈哈哈、、、")
    def run(self):
       print "跑步速度一般"

class  Mule(Horse,Donkey):
    def bark(self):
        print("嘘嘘嘘、、、")
    def run(self):
       print "跑步速度超级慢"


def animalBark(temp):
    temp.bark()

bailongma =Horse(name="白龙马",color= "BAI色")
# Tom.setColor("血红色")
# Tom.bark()
# Tom.eat()
print (bailongma)
Horse.horseNum +=1
print(bailongma.horseNum)


chituma =Horse(name="赤兔马",color= "血红色")
Horse.horseNum +=1
print(chituma.horseNum)
print (chituma)
# chituma.setHorseNum()



