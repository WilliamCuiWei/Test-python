#ecoding=utf-8
import numpy as np 
import pandas as pd 
green = pd.DataFrame(pd.read_excel('green14.xlsx', header = None))
union = pd.DataFrame(pd.read_excel('union14.xlsx', header = None))
result = pd.merge(green,union,how = 'inner')
result2 = pd.merge(union,green,how = 'outer')
print ("共同号码数是：%d"%len(result))
print ("不同的号码数是：%d"%len(result2))

# result.to_csv('same14.csv', encoding = "utf-8", index =True)
result2.to_csv('difference14_new.csv', encoding = "utf-8", index =True)
