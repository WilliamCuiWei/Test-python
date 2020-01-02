#encoding=utf-8
# import tushare as ts 
# print ts.get_hist_data('600338')

# df = ts.get_realtime_quotes('603882')  #获取实时分笔数据，可以实时取得股票当前报价和成交信息
# print df[['code','name','price','bid','ask','volume','amount','time']]

# print ts.realtime_boxoffice()[['MovieName','movieDay','sumBoxOffice']] #票房排名

# print ts.top_list('2018-10-12') #龙虎榜
# print ts.guba_sina()  #新浪股吧
# df = ts.guba_sina(True)
# print df.iloc[0]['content']   #查看第2条消息的内容

# print ts.get_latest_news()['title'][:1] #默认获取最近80条新闻数据，只提供新闻类型、链接和标题
# print latest_content(url)

# from pyecharts import Pie
# pie = Pie("省公司与专业公司对比",title_pos='center')
# attr = ["省公司","专业公司"]
# v1 = [31,531]
# pie.add("",attr,v1,is_symbol = True,is_label_show = True,legend_pos='right')
# # pie.add("专业公司",attr,v1,is_symbol = True,is_label_show = True)

# pie.render()


# jupyter nbconvert --to=python chapter-1-notebook.ipynb
#ecoding=utf-8
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data = pd.read_excel('E:/do you learn/python/6 provice.xlsx')


X = data['Sep']/10000
Y = data['Sep_consum']/10000
X1 = data['Nov']/10000
Y1 = data['Nov_consum']/10000

i =  X1.count() - 1 
precent = ((data['Nov'] / data['Sep'])-1).loc[i]
precent_consum = ((data['Nov_consum'] / data['Sep_consum'])-1).loc[i]

if precent <= 0 and precent_consum <= 0:
    print('【客户端活跃简报】11月%d日，一级客户端当日活跃用户数%0.1f万，9月同期%0.1f万，同比下降%.1f%%；累计月活%0.1f万，9月同期%0.1f万，同比下降%0.1f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,abs(precent) * 100, Y1.loc[i] ,Y.loc[i], abs(precent_consum)*100))
elif precent <= 0 and precent_consum >= 0:
     print('【客户端活跃简报】11月%d日，一级客户端当日活跃用户数%0.1f万，9月同期%0.1f万，同比下降%.1f%%；累计月活%0.1f万，9月同期%0.1f万，同比上升%0.1f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,abs(precent) * 100, Y1.loc[i] ,Y.loc[i], precent_consum*100))
elif precent >= 0 and precent_consum <= 0:
     print('【客户端活跃简报】11月%d日，一级客户端当日活跃用户数%0.1f万，9月同期%0.1f万，同比上升%.1f%%；累计月活%0.1f万，9月同期%0.1f万，同比下降%0.1f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,precent * 100, Y1.loc[i] ,Y.loc[i], abs(precent_consum)*100))
else:
    print('【客户端活跃简报】11月%d日，一级客户端当日活跃用户数%0.1f万，9月同期%0.1f万，同比上升%.1f%%；累计月活%0.1f万，9月同期%0.1f万，同比上升%0.1f%%。' \
          % (i+1, X1.loc[i], X.loc[i] ,precent * 100, Y1.loc[i] ,Y.loc[i], precent_consum*100))

