# #encoding=utf-8
import pandas as pd
from pandas import Series,DataFrame
from matplotlib import pyplot as plt
import numpy as np 
from pyecharts import Bar,Line,Grid

data = pd.read_excel('E:/do you learn/python/6 provice.xlsx')

data0 = data['Jun']
data1 = data['July']
data2 = data['Aug']
data3 = data['Jun_consum']
data4 = data['July_consum']
data5 = data['Aug_consum']

#pyecharts作图
line = Line("6月-8月客户端日活比较",title_pos="center",background_color = 'white')
attr = ['{}日'.format(i) for i in range(1,32)]
line.add("6月",attr,data0,line_opacity =1.9,is_symbol = True,legend_pos = '70%')
line.add("7月",attr,data1,is_smooth = True,legend_pos = '70%')
line.add("8月",attr,data2,line_opacity =1.9,area_opacity=0.6,is_symbol = True,legend_pos = '70%')


line1 = Line("6月-8月客户端月活比较",title_top="50%",title_pos="center",background_color = 'white')
attr = ['{}日'.format(i) for i in range(1,32)]
line1.add("6月",attr,data3,line_opacity =1.9,is_symbol = True,legend_pos = '70%')
line1.add("7月",attr,data4,is_smooth = True,legend_pos = '70%')
line1.add("8月",attr,data5,line_opacity =1.9,area_opacity=0.6,is_symbol = True,legend_pos = '70%')
grid = Grid(width=900,height =600)
grid.add(line1, grid_top="60%", grid_left="15%")
grid.add(line, grid_bottom="60%", grid_left="15%")
grid.render(path='C:/Users/lenovo/Downloads/Active.png')


# #累计月活图
# f,ax = plt.subplots(figsize = (8,16),nrows=2)
# # ax[0].plot(data1,'g.-',label = 'Aug')
# ax[0].plot(data3,'y.-',label = 'Mar')
# ax[0].plot(data4,'b.-',label = 'Apr')
# ax[0].plot(data5,'r.-',label = 'May')
# ax[0].legend(loc = 'best')
# ax[0].set_title("Monthly live")
# # ax[0].set_xlabel('Time')
# ax[0].set_ylabel('Nums_consum')
# ticks = ax[0].set_xticks(range(0,31))
# labels = ax[0].set_xticklabels(range(1,32),fontsize = 'small')

# #日活图
# i = 10
# colors = np.array(['r','b','g','y'])
# while i<=12:
#     data[i] = data.iloc[:,i]
#     ax[1].plot(data[i],'.-',label = '%d Month'%i,color = colors[11-i])   
#     i+=1
# ax[1].legend(loc = 'best')
# ax[1].set_title("Daily live")
# ax[1].set_xlabel('Time')
# ax[1].set_ylabel('Nums')
# ticks = ax[1].set_xticks(range(0,31))
# labels = ax[1].set_xticklabels(range(1,32),fontsize = 'small')
# plt.show()



