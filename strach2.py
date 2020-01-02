#ecoding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
url = "http://http://www.meizitu.com/"
send_head={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Connection":" keep-alive",
"Host": "www.meizitu.com",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}
req = urllib2.Request(url,headers = send_head)
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html,"html5lib")
yy = soup.select("div[class=postContent]")
for ii in yy:
	hh = ii.select("img")
	qq = hh[0]
	res = qq['src']
	print res
work_path = "E:/do you learn/python/image/" + 'first' + ".jpg"
# urllib.urlretrieve(res,work_path)
# with open("E:/do you learn/python/image/image1.jpg" % path_name, "wb") as f:
#     f.write(response.read())