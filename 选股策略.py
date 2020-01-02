#!/usr/bin/python
#coding=utf-8
import tushare as ts
import pandas as pd
import numpy as np
allIndex = ts.get_today_all()

XY = allIndex[allIndex['changepercent']<2]   #实时行情
JJ = XY[XY['turnoverratio']>2]
DD = JJ[JJ['volume']>np.mean(JJ['volume'])]
print DD