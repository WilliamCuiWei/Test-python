#ecoding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import numpy as np
url = "https://shenzhen.leyoujia.com/esf/"
send_head={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Connection":"keep-alive",
"Host": "shenzhen.leyoujia.com",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
req = urllib2.Request(url,headers = send_head)
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html,"html5lib")
yy = soup.select("div[class=list-box]")
uu = yy[0]
tt = uu.select("li")

i =0
while i<=len(tt):
	if i < 5:
		hh = tt[i].select("div[class=text]")
		rr =hh[0]
		bb = rr.select('p > a')
		print bb[0].string
		mm = rr.select('p > span')
		for pp in mm:
			print pp.string.strip(),
		i+=1
	# elif i >5:
	# 	hh = tt[i].select("div[class=text]")
	# 	rr =hh[0]
	# 	bb = rr.select('p > a')
	# 	print bb[0].string
	# 	mm = rr.select('p > span')
	# 	for pp in mm:
	# 		print pp.string.strip(),
	# 	i+=1

# work_path = "E:/do you learn/python/image/" + 'first' + ".jpg"
# urllib.urlretrieve(res,work_path)
# with open("E:/do you learn/python/image/image1.jpg" % path_name, "wb") as f:
#     f.write(response.read())

