#ecoding=utf-8
import pandas as pd
from pandas import Series,DataFrame
from pyecharts import Bar,Line,Grid

data = pd.read_excel('E:/do you learn/python/6 provice.xlsx')
data0 = data['Aug']
data1 = data['Sep']
data2 = data['Nov']
data3 = data['Aug_consum']
data4 = data['Sep_consum']
data5 = data['Nov_consum']

line = Line("8-10月日活用户数比较",title_pos="center",background_color = 'white')
attr = ['{}日'.format(i) for i in range(1,32)]
line.add("8月",attr,data0,line_opacity =1.9,is_symbol = True,legend_pos = '70%')
line.add("9月",attr,data1,is_smooth = True,legend_pos = '70%')
line.add("10月",attr,data2,line_opacity =1.9,area_opacity=0.6,is_symbol = True,legend_pos = '70%')


line1 = Line("8-10月月活用户数比较",title_top="50%",title_pos="center",background_color = 'white')
attr = ['{}日'.format(i) for i in range(1,32)]
line1.add("8月",attr,data3,line_opacity =1.9,is_symbol = True,legend_pos = '70%')
line1.add("9月",attr,data4,is_smooth = True,legend_pos = '70%')
line1.add("10月",attr,data5,line_opacity =1.9,area_opacity=0.6,is_symbol = True,legend_pos = '70%')
grid = Grid(width=900,height=600)
grid.add(line1, grid_top="60%", grid_left="15%")
grid.add(line, grid_bottom="60%", grid_left="15%")
grid.render(path='C:/Users/lenovo/Downloads/Active.png', pixel_ratio=3)