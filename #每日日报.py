#ecoding=utf-8
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
#导入数据
data = pd.read_excel('E:/do you learn/python/6 provice.xlsx')

#日活指标定义	
X = data['July']/10000
X1 = data['Aug']/10000
Y = data['July_consum']/10000
Y1 = data['Aug_consum']/10000
#新增用户数和安装量指标
New1 = data['New_peo']/10000
Install = data['Install']/10000
#计算日活和累计月活环比
i =  X1.count() - 1 
precent = ((data['Aug'] / data['July'])-1).loc[i]
precent_consum = ((data['Aug_consum'] / data['July_consum'])-1).loc[i]
#判断和输出过程
if precent <= 0 and precent_consum <= 0:
    print('【客户端活跃简报-8月%d日】\n 一级客户端当日活跃用户数%0.1f万，上月同期%0.1f万，同比下降%.1f%%；累计月活%0.1f万，上月同期%0.1f万，同比下降%0.1f%%。当日新增用户数%0.1f万，当日APP新增安装量%0.1f万。' \
          % (i+1, X1.loc[i], X.loc[i] ,abs(precent) * 100, Y1.loc[i] ,Y.loc[i], abs(precent_consum)*100,New1.loc[i],Install.loc[i]))
elif precent <= 0 and precent_consum >= 0:
     print('【客户端活跃简报-8月%d日】\n 一级客户端当日活跃用户数%0.1f万，上月同期%0.1f万，同比下降%.1f%%；累计月活%0.1f万，上月同期%0.1f万，同比上升%0.1f%%。当日新增用户数%0.1f万，当日APP新增安装量%0.1f万。' \
          % (i+1, X1.loc[i], X.loc[i] ,abs(precent) * 100, Y1.loc[i] ,Y.loc[i], precent_consum*100,New1.loc[i],Install.loc[i]))
elif precent >= 0 and precent_consum <= 0:
     print('【客户端活跃简报-8月%d日】\n 一级客户端当日活跃用户数%0.1f万，上月同期%0.1f万，同比上升%.1f%%；累计月活%0.1f万，上月同期%0.1f万，同比下降%0.1f%%。当日新增用户数%0.1f万，当日APP新增安装量%0.1f万。' \
          % (i+1, X1.loc[i], X.loc[i] ,precent * 100, Y1.loc[i] ,Y.loc[i], abs(precent_consum)*100,New1.loc[i],Install.loc[i]))
else:
    print('【客户端活跃简报-8月%d日】\n 一级客户端当日活跃用户数%0.1f万，上月同期%0.1f万，同比上升%.1f%%；累计月活%0.1f万，上月同期%0.1f万，同比上升%0.1f%%。当日新增用户数%0.1f万，当日APP新增安装量%0.1f万。' \
          % (i+1, X1.loc[i], X.loc[i] ,precent * 100, Y1.loc[i] ,Y.loc[i], precent_consum*100,New1.loc[i],Install.loc[i]))

