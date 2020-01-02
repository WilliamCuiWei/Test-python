#ecoding=utf-8
import urllib2
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd 
url = "http://data.10jqka.com.cn/financial/yjyg/"
send_head= {
"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Connection": "keep-alive",
"Host": "data.10jqka.com.cn",
"User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}
req = urllib2.Request(url,headers = send_head)
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html,"html5lib")
hh = soup.select("body")
xx = hh[0]
yy = xx.select("div[id=J-ajax-main]")
pp = yy[0]
kk = pp.select("tr")
i =1
while i<=5:
	tt = kk[i]
	px = tt.select("td")
	for xi in px:
		po = xi.select("a")
		if po != []:
			mes = po[0].string
			print mes,
	precent = px[-3].string
	pre =str(precent.strip())
	print '。利润增长：' + pre
	i+=1
