#ecoding=utf-8
import urllib2
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd 
url = "https://ec.hq.10086.cn/oap/palmHallActionAction!kpiActiveUserDay.shtml?reportId=222"
send_head= {
"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Connection": "keep-alive",
"Host": "ec.hq.10086.cn",
"User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
req = urllib2.Request(url,headers = send_head)
response = urllib2.urlopen(req)
html = response.read()
print html