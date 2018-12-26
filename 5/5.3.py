def isNum(s):
    try:
        n = eval(s)
    except:
        return False
    return True
s = input("")
if isNum(s):
    print("number")
else:
    print("not a number")

    
   import requests
import time
def getHTMLText(url,coding='gbk'):
    try:
        r=requests.get(url,timeout=30)
        r,raise_for_status()
        r.encoding=coding
        return r.test
    except:
        return""

def downloadImageFile(imgUrl, destUrl, fname=''):  #网址，下载地，另存地
    local_filename = imgUrl.split('/')[-1]
    print('Download Image File={}'.format(local_filename))
    try:
        r=requests.get(imgUrl,stream=True)
        r.raise_for_status()

        if len(fname)== 0:
            fname=local_filename
        print('fname={}'.format(fname))
        with open(destUrl + "/"+fname,'wb') as f:    #下载图片
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        return r.status_code
    except:
        return r.status_code




import json
import re

def getImg(html):
    imgre = re.compile('"thumbURL":"(.*?)"')
    imglist = re.findall(imgre,html)
    return imglist

def download(urls,path):
    index = 1
    for url in urls:
        print("Download Image from page:{}".format(url))
        status = downloadImageFile(url,path,str(index)+'.jpg')
        try:
            if str(status)[0] == '4':
                print("未下载成功{}".format(url))
                continue
        except Exception as e:
            print("未下载成功{}".format(url))
        index += 1


page = 'https://image.baidu.com/search/index?tn=baiduimage&word=杨幂'

html= getHTMLText(page)
download(getImg(html), 'd:/baidupic') 
