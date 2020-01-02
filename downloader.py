
import os 
import requests
import re
import datetime


def getPageImgUrl(url):
    headers = {
        'use_agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
    }
    res = requests.get(url,headers=headers).content
    pattern = re.compile(r'data-progressive="(.*?)"')
    urls = re.findall(pattern, str(res))
    return urls


def getAllUrl(page_cnt):
    l = []
    for i in range(1,1+page_cnt):
        url = 'https://bing.ioliu.cn/?p={}'.format(i)
        u = getPageImgUrl(url)
        l += u
    return l



def DownloadImg(url, dir):
    headers = {
        'use_agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
    }
    r = requests.get(url,headers=headers)
    pattern = re.compile(r'/bing/(.*?)_1920')
    filename_raw = re.findall(pattern, url)
    if filename_raw:

        filename = str(filename_raw[0]) + '.jpg'
    
        # while not filename in os.listdir(dir):
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(r.content)
    else:
        pass


if __name__ == "__main__":
    output_dir = 'E:/songs/Wallpapers'
    try:
        os.makedirs(output_dir)
    except:
        pass

    # urls = getAllUrl(10)
    # for page_no, page_url in enumerate(urls):
    #     print("Processing page: %s of %s. %s" % (page_no, 10, datetime.datetime.now()))
    #     img_urls = getPageImgUrl(page_url)
    #     for img_no, img_url in enumerate(img_urls):
    #         print("Processing page: %s of %s, pic_no: %s. %s" % (page_no, 10, img_no, datetime.datetime.now()))
    #         DownloadImg(img_url, output_dir)

    img_urls = getAllUrl(5)
    img_cnt = len(img_urls)
    for img_no, img_url in enumerate(img_urls):
        print("Processing pic_no: %s of %s. %s" % (img_no, img_cnt, datetime.datetime.now()))
        DownloadImg(img_url, output_dir)