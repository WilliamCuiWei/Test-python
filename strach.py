import urllib2
import re
from BeautifulSoup import *
url = "http://douyu.com"
send_headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "dy_did=282a193824605986f54c8bd200051501; acf_did=282a193824605986f54c8bd200051501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1529587062,1529624566; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1529624566",
"Host": "www.douyu.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}
req = urllib2.Request(url,headers = send_headers)
response = urllib2.urlopen(req)
print response.getcode()
html = response.read()
imagelist = re.findall(r'src="(.*?\.jpg)"',html)
print imagelist
urllib.urlretrieve(imagelist[4],filename="E:/do you learm/python/image/car4.jpg")
		



