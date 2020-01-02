#!/usr/bin/python
#coding=utf-8
#!/usr/bin/python

from __future__ import unicode_literals
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
data2 = pd.read_excel('E:/do you learn/python/all provice live.xlsx')
dataOct = data2.iloc[:,10]
dataSep = data2.iloc[:,9]
dataAug = data2.iloc[:,8]
dataName = data2.iloc[:,0]
ziDian = dict(zip(dataName,range(1,32)))

input_name=raw_input(u'省份：'.encode('gbk'))
pro_code=ziDian.get(input_name.decode('utf-8'))   #获取省份信息

proData = list(data2.iloc[pro_code-1,1:])
from pyecharts import Bar
bar = Bar("2018年一级客户端{}活跃用户变化趋势".format(data2.iloc[pro_code-1,0]),title_pos = 'center',width=750)
month = ['{}月'.format(i) for i in range(1,11)]
bar.add("", month, proData, mark_line=['min','max'])
bar.render()
