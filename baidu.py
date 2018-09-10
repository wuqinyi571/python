import urllib.request

url = "http://www.baidu.com/"
keyword = "性感"
key_code= urllib.request.quote(keyword)
filename = "D://PythonTest/1.html"
search_url = url + "s?wd=" + key_code
req = urllib.request.Request(search_url)
data = urllib.request.urlopen(req).read()
#data = data.decode('UTF-8')
#print(data)
fhandle = open(filename,"wb")
fhandle.write(data)
fhandle.close()