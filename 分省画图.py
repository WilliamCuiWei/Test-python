#ecoding=utf-8
from __future__ import unicode_literals

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from pyecharts import Bar,Line,Map,Page,Grid

data2 = pd.read_excel('E:/do you learn/python/all provice live.xlsx')
data4 = data2.iloc[:,4]
data5 = data2.iloc[:,5]
dataName = data2.iloc[:,0]

datatotle =  pd.Series(data2.iloc[:,0], name='Name')
datatotle = pd.Series.to_frame(datatotle)
datatotle['Apr'] = pd.Series(data2.iloc[:,4])
datatotle['May'] = pd.Series(data2.iloc[:,5])
datatotle = datatotle.sort_values(by = 'May',ascending=False)

#分省画柱状图
bar2 = Bar("分省4月-5月份月活柱状图",title_pos='center',background_color = 'white', width=2000, height=800)   
# month = ["{}日".format(i) for i in range(1,32)] 
# bar2.add("8月月活",list(dataName),dataAug,is_stack=True)
bar2.add("4月月活",list(datatotle['Name']),datatotle['Apr'],is_stack=True,legend_pos = '70%')
bar2.add("5月月活",list(datatotle['Name']),datatotle['May'],mark_point=["min", "max"],mark_point_symbolsize=90,legend_pos = '70%')
bar2.render(path='C:/Users/lenovo/Downloads/provice.png')
