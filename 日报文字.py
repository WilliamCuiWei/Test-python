#ecoding=utf-8
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data = pd.read_excel('E:/do you learn/python/6 provice2020.xlsx')


X = data['Dec']/10000
Y = data['Dec_consum']/10000
X1 = data['Jan']/10000
Y1 = data['Jan_consum']/10000

i =  X1.count() - 1 
precent = ((data['Jan'] / data['Dec'])-1).loc[i]
precent_consum = ((data['Jan_consum'] / data['Dec_consum'])-1).loc[i]

if precent <= 0 and precent_consum <= 0:
    print('【客户端活跃简报】12月%d日，一级客户端当日活跃用户数%0.2f万，上月同期%0.2f万，同比下降%.2f%%；累计月活%0.1f万，上月同期%0.1f万，同比下降%0.2f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,abs(precent) * 100, Y1.loc[i] ,Y.loc[i], abs(precent_consum)*100))
elif precent <= 0 and precent_consum >= 0:
     print('【客户端活跃简报】12月%d日，一级客户端当日活跃用户数%0.2f万，上月同期%0.2f万，同比下降%.2f%%；累计月活%0.1f万，上月同期%0.1f万，同比上升%0.2f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,abs(precent) * 100, Y1.loc[i] ,Y.loc[i], precent_consum*100))
elif precent >= 0 and precent_consum <= 0:
     print('【客户端活跃简报】12月%d日，一级客户端当日活跃用户数%0.2f万，上月同期%0.2f万，同比上升%.2f%%；累计月活%0.1f万，上月同期%0.1f万，同比下降%0.2f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,precent * 100, Y1.loc[i] ,Y.loc[i], abs(precent_consum)*100))
else:
    print('【客户端活跃简报】12月%d日，一级客户端当日活跃用户数%0.2f万，上月同期%0.2f万，同比上升%.2f%%；累计月活%0.1f万，上月同期%0.1f万，同比上升%0.2f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,precent * 100, Y1.loc[i] ,Y.loc[i], precent_consum*100))