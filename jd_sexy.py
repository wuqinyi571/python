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
    pat1='div id="J_goodsList".+?<div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    print(result1)
    result1=result1[0]
    print(result1)
    pat2='<img width="220" height="220" class="err-product" data-img="1" src="//(.+?\.jpg)"'
    imageList=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imageList:
        imagename="D://Pythontest/sexy/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        print (imageurl)
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(1,6):
    url="http://search.jd.com/Search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&page="+str(i)
    #url="http://image.baidu.com/search/index?tn=baiduimage&word=xinggan"
    craw(url,i)
