#coding=utf-8

import re
import urllib.request

#定义一个getHtml()函数
def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def craw(url,page):
    html1=getHtml(url)
    html1=str(html1)
    pat1="http://.*?jpg"
    #result1=re.compile(pat1).findall(html1)
    #result1=result1[0]
    #pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imageList=re.compile(pat1).findall(html1)
    x=1
    for imageurl in imageList:
        imagename="D://Pythontest/sexy/"+str(page)+str(x)+".jpg"
        print(imageurl)

        #imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e)
                x+=1
            if hasattr(e,"reason"):
                print(e)
                x+=1
        x+=1

for i in range(1,6):
    url="http://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    #url="http://image.baidu.com/search/index?tn=baiduimage&word=zhangzhen"
    craw(url,i)
